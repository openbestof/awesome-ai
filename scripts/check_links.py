"""Check the destination link for every README table entry."""

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import re
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

README = Path(__file__).resolve().parents[1] / "readme.md"
ENTRY = re.compile(r"^\| \[([^]]+)\]\((https?://[^)]*)\) \|")


def check(item):
    name, url = item
    for method in ("HEAD", "GET"):
        try:
            request = Request(url, method=method, headers={"User-Agent": "awesome-ai-link-check/1.0"})
            with urlopen(request, timeout=15) as response:
                return name, url, response.status, response.url
        except HTTPError as error:
            if method == "HEAD" and error.code in (403, 405):
                continue
            return name, url, error.code, error.geturl()
        except (URLError, TimeoutError) as error:
            if method == "HEAD":
                continue
            return name, url, "ERROR", str(error.reason if isinstance(error, URLError) else error)
    return name, url, "ERROR", "No response"


entries = [match.groups() for line in README.read_text(encoding="utf-8").splitlines() if (match := ENTRY.match(line))]
with ThreadPoolExecutor(max_workers=8) as executor:
    results = list(executor.map(check, entries))

bad = [result for result in results if result[2] != 200]
redirects = [result for result in results if result[2] == 200 and result[1].rstrip("/") != result[3].rstrip("/")]
print(f"Checked {len(results)} links: {len(bad)} failures, {len(redirects)} redirects")
for name, url, status, destination in bad + redirects:
    print(f"{status}\t{name}\t{url}\t{destination}")
raise SystemExit(bool(bad))
