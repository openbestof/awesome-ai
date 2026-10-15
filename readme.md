# Awesome AI

A curated list of AI tools, frameworks, APIs, software, and resources.

Last reviewed: 2026-10-15. All destination links were checked. Product features, pricing, and maintenance status can change.
Archived projects are labeled where known. Check each project's documentation before adoption.

## Table of Contents
- [Awesome AI](#awesome-ai)
  - [Table of Contents](#table-of-contents)
  - [AI API](#ai-api)
  - [AI Cloud](#ai-cloud)
  - [LLMs Backend](#llms-backend)
  - [LLMs ChatUI](#llms-chatui)
  - [Image Generation & Editing](#image-generation--editing)
  - [Code Assistant](#code-assistant)
  - [Autonomous Agents](#autonomous-agents)
  - [Knowledge Manager](#knowledge-manager)
  - [LLMs Eval](#llms-eval)
  - [LLMs Framework](#llms-framework)
  - [LLMs Training](#llms-training)
  - [Vector Database](#vector-database)
  - [AI Course](#ai-course)
  - [Audio AI](#audio-ai)

## AI API
| Name | Description | Repos |
|------|-------------|-------|
| [Hugging Face](https://github.com/huggingface/transformers) | Hugging Face hosts and shares models, datasets, and AI applications; this link points to its Transformers library. | ![GitHub Repo stars](https://img.shields.io/github/stars/huggingface/transformers) |
| [CivitAI](https://github.com/civitai/civitai) | Explore thousands of high-quality Stable Diffusion models, share your AI-generated art, and engage with a vibrant community of creators. | ![GitHub Repo stars](https://img.shields.io/github/stars/civitai/civitai) |
| [Mistral AI](https://github.com/mistralai/mistral-inference) | Open and portable generative AI for devs and businesses. | ![GitHub Repo stars](https://img.shields.io/github/stars/mistralai/mistral-inference) |
| [Anthropic](https://github.com/anthropics/claude-cookbooks) | Anthropic is an AI safety and research company that&#x27;s working to build reliable, interpretable, and steerable AI systems. | ![GitHub Repo stars](https://img.shields.io/github/stars/anthropics/claude-cookbooks) |
| [Groq](https://github.com/groq/groq-api-cookbook) | Groq provides fast inference APIs for AI models; this link points to its API cookbook. | ![GitHub Repo stars](https://img.shields.io/github/stars/groq/groq-api-cookbook) |
| [OpenAI](https://github.com/openai/openai-cookbook) | OpenAI Platform API for accessing new AI models developed by OpenAI. | ![GitHub Repo stars](https://img.shields.io/github/stars/openai/openai-cookbook) |
| [Perplexity](https://docs.perplexity.ai/docs/getting-started/overview) | Perplexity's developer documentation for its search and model APIs. | - |
| [OpenRouter](https://openrouter.ai/developers) | Unified API access to models from multiple providers. | - |
| [Gemini API](https://github.com/GoogleCloudPlatform/generative-ai) | Experience Google's largest and most capable AI model. | ![GitHub Repo stars](https://img.shields.io/github/stars/GoogleCloudPlatform/generative-ai) |
| [Cohere](https://github.com/cohere-ai/cohere-python) | Cohere provides industry-leading large language models (LLMs) and RAG capabilities. | ![GitHub Repo stars](https://img.shields.io/github/stars/cohere-ai/cohere-python) |
| [Anyscale](https://github.com/anyscale/endpoint-cookbook) | Anyscale provides infrastructure for building and serving AI applications with Ray. | ![GitHub Repo stars](https://img.shields.io/github/stars/anyscale/endpoint-cookbook) |
| [Stability AI](https://github.com/Stability-AI/generative-models) | Stability AI Developer Platform Explore the possibilities of generative AI | ![GitHub Repo stars](https://img.shields.io/github/stars/Stability-AI/generative-models) |
| [LiteLLM](https://github.com/BerriAI/litellm) | LiteLLM handles loadbalancing, fallbacks and spend tracking across 100+ LLMs. All in the OpenAI format. | ![GitHub Repo stars](https://img.shields.io/github/stars/BerriAI/litellm) |

## AI Cloud
| Name | Description | Repos |
|------|-------------|-------|
| [Together AI](https://github.com/togethercomputer/together-python) | Build gen AI models with Together AI. Benefit from the fastest and most cost-efficient tools and infra. | ![GitHub Repo stars](https://img.shields.io/github/stars/togethercomputer/together-python) |
| [Vertex AI](https://github.com/googleapis/python-aiplatform) | Vertex AI is a fully-managed, unified AI development platform for building and using generative AI. | ![GitHub Repo stars](https://img.shields.io/github/stars/googleapis/python-aiplatform) |
| [Amazon SageMaker](https://github.com/aws/amazon-sagemaker-examples) | Amazon SageMaker is AWS's managed service for building, training, and deploying machine learning models. | ![GitHub Repo stars](https://img.shields.io/github/stars/aws/amazon-sagemaker-examples) |
| [Azure OpenAI](https://github.com/Azure-Samples/azure-ai) | Azure OpenAI Service. Build your own copilot and generative AI applications | ![GitHub Repo stars](https://img.shields.io/github/stars/Azure-Samples/azure-ai) |
| [RunDiffusion](https://www.rundiffusion.com/) | RunDiffusion is a hosted workspace for generative image and video tools. | - |
| [Replicate](https://github.com/replicate/cog) | Run and fine-tune open-source models. Deploy custom models at scale. All with one line of code. | ![GitHub Repo stars](https://img.shields.io/github/stars/replicate/cog) |
| [Paperspace](https://github.com/Paperspace/cli) | Build & Run AI/ML Models on NVIDIA H100 GPUs. Develop, train, and deploy AI applications. | ![GitHub Repo stars](https://img.shields.io/github/stars/Paperspace/cli) |
| [Bedrock](https://github.com/aws-samples/amazon-bedrock-workshop) | The easiest way to build and scale generative AI applications with foundation models. | ![GitHub Repo stars](https://img.shields.io/github/stars/aws-samples/amazon-bedrock-workshop) |
| [Workers AI](https://github.com/cloudflare/cloudflare-docs) | Run machine learning models, powered by serverless GPUs, on Cloudflare’s global network. | ![GitHub Repo stars](https://img.shields.io/github/stars/cloudflare/cloudflare-docs) |
| [Scaleway](https://github.com/scaleway/docs-content) | Discover European sovereign cloud services to scale your AI projects from A to Z. | ![GitHub Repo stars](https://img.shields.io/github/stars/scaleway/docs-content) |

## LLMs Backend
| Name | Description | Repos |
|------|-------------|-------|
| [Llama.cpp](https://github.com/ggml-org/llama.cpp) | The main goal of llama.cpp is to run the LLaMA model using 4-bit integer quantization on a MacBook. | ![GitHub Repo stars](https://img.shields.io/github/stars/ggml-org/llama.cpp) |
| [Mudler LocalAGI](https://github.com/mudler/LocalAGI) | LocalAGI is a small virtual assistant that you can run locally, made by the LocalAI author and powered by it. | ![GitHub Repo stars](https://img.shields.io/github/stars/mudler/LocalAGI) |
| [Ollama](https://github.com/ollama/ollama) | Ollama is LLMs Backend that allow you to get up and running with large language models locally. | ![GitHub Repo stars](https://img.shields.io/github/stars/ollama/ollama) |
| [Mudler LocalAI](https://github.com/mudler/LocalAI) | Drop-in replacement for OpenAI running on consumer-grade hardware. No GPU required. | ![GitHub Repo stars](https://img.shields.io/github/stars/mudler/LocalAI) |
| [KoboldCpp](https://github.com/LostRuins/koboldcpp) | KoboldCpp is an easy-to-use AI text-generation software for GGML and GGUF models. | ![GitHub Repo stars](https://img.shields.io/github/stars/LostRuins/koboldcpp) |
| [gpt4all](https://github.com/nomic-ai/gpt4all) | Open-source large language models that run locally on your CPU and nearly any GPU. | ![GitHub Repo stars](https://img.shields.io/github/stars/nomic-ai/gpt4all) |
| [KoboldCpp ROCm](https://github.com/YellowRoseCx/koboldcpp-rocm) | AI Inferencing at the Edge. A simple one-file way to run various GGML models with KoboldAI's UI with AMD ROCm offloading. | ![GitHub Repo stars](https://img.shields.io/github/stars/YellowRoseCx/koboldcpp-rocm) |
| [Text Generation WebUI](https://github.com/oobabooga/textgen) | Oobabooga Text Generation WebUI is a Gradio browser interface for Large Language Models. Supports transformers, GPTQ, AWQ, EXL2, llama.cpp (GGUF), Llama models. | ![GitHub Repo stars](https://img.shields.io/github/stars/oobabooga/textgen) |
| [vLLM](https://github.com/vllm-project/vllm) | A high-throughput and memory-efficient inference and serving engine for LLMs. | ![GitHub Repo stars](https://img.shields.io/github/stars/vllm-project/vllm) |
| [ExLlama](https://github.com/turboderp-org/exllamav2) | A fast inference library for running LLMs locally on modern consumer-class GPUs. | ![GitHub Repo stars](https://img.shields.io/github/stars/turboderp-org/exllamav2) |
| [SGLang](https://github.com/sgl-project/sglang) | High-performance serving framework for language and multimodal models. | ![GitHub Repo stars](https://img.shields.io/github/stars/sgl-project/sglang) |

## LLMs ChatUI
| Name | Description | Repos |
|------|-------------|-------|
| [Local AI](https://github.com/louisgv/local.ai) | Local AI is a desktop app for local, private, secured AI experimentation. | ![GitHub Repo stars](https://img.shields.io/github/stars/louisgv/local.ai) |
| [Serge](https://github.com/serge-chat/serge) | Serge is a chat interface crafted with llama.cpp for running GGUF models. No API keys, entirely self-hosted. | ![GitHub Repo stars](https://img.shields.io/github/stars/serge-chat/serge) |
| [Llama2 WebUI](https://github.com/liltom-eth/llama2-webui) | Run any Llama 2 locally with gradio UI on GPU or CPU from anywhere (Linux/Windows/Mac). | ![GitHub Repo stars](https://img.shields.io/github/stars/liltom-eth/llama2-webui) |
| [Dialoqbase](https://github.com/n4ze3m/dialoqbase) | Dialoqbase is an open-source application designed to facilitate the creation of custom chatbots using a personalized knowledge base. | ![GitHub Repo stars](https://img.shields.io/github/stars/n4ze3m/dialoqbase) |
| [SillyTavern](https://github.com/SillyTavern/SillyTavern) | SillyTavern is a Chat UI that allows you to interact with text generation AIs and chat/roleplay with characters you or the community create. | ![GitHub Repo stars](https://img.shields.io/github/stars/SillyTavern/SillyTavern) |
| [Alpaca Electron](https://github.com/ItsPi3141/alpaca-electron) | Alpaca Electron is built from the ground-up to be the easiest way to chat with the alpaca AI models. No command line or compiling needed. | ![GitHub Repo stars](https://img.shields.io/github/stars/ItsPi3141/alpaca-electron) |
| [LM Studio](https://github.com/lmstudio-ai/model-catalog) | LM Studio is a desktop application for discovering and running Large Language Models locally. | ![GitHub Repo stars](https://img.shields.io/github/stars/lmstudio-ai/model-catalog) |
| [LobeHub](https://github.com/lobehub/lobehub) | Lobe Chat is an open-source, high-performance chatbot framework that supports speech synthesis, multimodal, and extensible Function Call plugin system. | ![GitHub Repo stars](https://img.shields.io/github/stars/lobehub/lobehub) |
| [LibreChat](https://github.com/LibreChat-AI/LibreChat) | LibreChat brings together the future of assistant AIs with the revolutionary technology of OpenAI's ChatGPT. | ![GitHub Repo stars](https://img.shields.io/github/stars/LibreChat-AI/LibreChat) |
| [Maid](https://github.com/danemadsen/Maid) | Maid is a cross-platform Flutter app for interfacing with GGUF / llama.cpp models locally, and with Ollama models remotely. | ![GitHub Repo stars](https://img.shields.io/github/stars/danemadsen/Maid) |
| [NextPy](https://github.com/dot-agent/nextpy) | NextPy is a Pythonic Web App framework For Humans & LLMs, Simple like Streamlit + Fast and Flexible like Next.js. | ![GitHub Repo stars](https://img.shields.io/github/stars/dot-agent/nextpy) |
| [Tavern AI](https://github.com/TavernAI/TavernAI) | TavernAI is an atmospheric frontend for chat and storywriting, compatible with many backends. | ![GitHub Repo stars](https://img.shields.io/github/stars/TavernAI/TavernAI) |
| [Bionic GPT](https://github.com/bionic-gpt/bionic-gpt) | BionicGPT is an on-premise replacement for ChatGPT, offering the advantages of Generative AI while maintaining strict data confidentiality. | ![GitHub Repo stars](https://img.shields.io/github/stars/bionic-gpt/bionic-gpt) |
| [Anse](https://github.com/anse-app/anse) | Supercharged experience for multiple models such as ChatGPT, DALL-E and Stable Diffusion. | ![GitHub Repo stars](https://img.shields.io/github/stars/anse-app/anse) |
| [ShellGPT](https://github.com/TheR1D/shell_gpt) | A command-line productivity tool powered by AI large language models like GPT-4, will help you accomplish your tasks faster and more efficiently. | ![GitHub Repo stars](https://img.shields.io/github/stars/TheR1D/shell_gpt) |
| [JanAI](https://github.com/janhq/jan) | Open-source ChatGPT alternative that runs 100% offline on your computer. | ![GitHub Repo stars](https://img.shields.io/github/stars/janhq/jan) |
| [Noi](https://github.com/lencx/Noi) | Noi is an AI-enhanced, customizable browser designed to streamline your digital experience | ![GitHub Repo stars](https://img.shields.io/github/stars/lencx/Noi) |
| [Open WebUI](https://github.com/open-webui/open-webui) | Open WebUI is an extensible, feature-rich, and user-friendly self-hosted WebUI designed to operate entirely offline. | ![GitHub Repo stars](https://img.shields.io/github/stars/open-webui/open-webui) |
| [Enchanted](https://github.com/gluonfield/enchanted) | Open-source chat client for local and hosted language models. | ![GitHub Repo stars](https://img.shields.io/github/stars/gluonfield/enchanted) |

## Image Generation & Editing
| Name | Description | Repos |
|------|-------------|-------|
| [Fooocus](https://github.com/lllyasviel/Fooocus) | Fooocus is an image generating software (based on Gradio). Fooocus is a rethinking of Stable Diffusion and Midjourney’s designs. | ![GitHub Repo stars](https://img.shields.io/github/stars/lllyasviel/Fooocus) |
| [Krita AI](https://github.com/Acly/krita-ai-diffusion) | Streamlined interface for generating images with AI in Krita. Inpaint and outpaint with optional text prompt, no tweaking required. | ![GitHub Repo stars](https://img.shields.io/github/stars/Acly/krita-ai-diffusion) |
| [VoltaML](https://github.com/VoltaML/voltaML-fast-stable-diffusion) | Volta ML is Beautiful and Easy to use a Stable Diffusion WebUI with an API accelerated by AITemplate. | ![GitHub Repo stars](https://img.shields.io/github/stars/VoltaML/voltaML-fast-stable-diffusion) |
| [InvokeAI](https://github.com/invoke-ai/InvokeAI) | InvokeAI is a creative engine for Stable Diffusion models, empowering people to generate and create visual media using the latest AI-driven technologies. | ![GitHub Repo stars](https://img.shields.io/github/stars/invoke-ai/InvokeAI) |
| [SHARK](https://github.com/nod-ai/AMD-SHARK-Studio) | Shark is an Stable Diffusion Backend optimised for Rocm and AMD GPUs that you can use with Blender and Kobold.cpp. | ![GitHub Repo stars](https://img.shields.io/github/stars/nod-ai/AMD-SHARK-Studio) |
| [Face Fusion](https://github.com/facefusion/facefusion) | Face Fusion is the next generation face swapper and enhancer that use Stable Diffusion as backend. | ![GitHub Repo stars](https://img.shields.io/github/stars/facefusion/facefusion) |
| [Stable Studio](https://github.com/Stability-AI/StableStudio) | StableStudio is Stability AI’s official open-source variant of DreamStudio. It is a web-based application that allows users to create and edit generated images. | ![GitHub Repo stars](https://img.shields.io/github/stars/Stability-AI/StableStudio) |
| [SD Next](https://github.com/vladmandic/sdnext) | SD Next is a Stable Diffusion implementation with advanced features. | ![GitHub Repo stars](https://img.shields.io/github/stars/vladmandic/sdnext) |
| [Fooocus MRE](https://github.com/MoonRide303/Fooocus-MRE) | Fooocus-MRE is an image generating software (based on Gradio), an enhanced variant of the original Fooocus dedicated for a bit more advanced users. | ![GitHub Repo stars](https://img.shields.io/github/stars/MoonRide303/Fooocus-MRE) |
| [Stability Matrix](https://github.com/LykosAI/StabilityMatrix) | Stability Matrix is a Multi-Platform Package Manager and Inference UI for Stable Diffusion. | ![GitHub Repo stars](https://img.shields.io/github/stars/LykosAI/StabilityMatrix) |
| [A1111 WebUI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | Stable Diffusion Web UI is a Gradio browser interface for the Generative AI model Stable Diffusion.  | ![GitHub Repo stars](https://img.shields.io/github/stars/AUTOMATIC1111/stable-diffusion-webui) |
| [ComfyUI](https://github.com/Comfy-Org/ComfyUI) | ComfyUI is a stable diffusion GUI and backend that let you design and execute advanced stable diffusion pipelines using a graph/nodes/flowchart based interface. | ![GitHub Repo stars](https://img.shields.io/github/stars/Comfy-Org/ComfyUI) |
| [ImaginAIry](https://github.com/brycedrennan/imaginAIry) | Pythonic AI generation of images and videos. | ![GitHub Repo stars](https://img.shields.io/github/stars/brycedrennan/imaginAIry) |
| [SlingRING](https://github.com/Blizaine/SlingRING) | SlingRING is an open-source web application designed to streamline and simplify controlling and accessing various AI applications on your local system. | ![GitHub Repo stars](https://img.shields.io/github/stars/Blizaine/SlingRING) |
| [Dreamfusion](https://github.com/ashawkey/stable-dreamfusion) | Stable Dreamfusion is a pytorch implementation of the text-to-3D model Dreamfusion, powered by the Stable Diffusion text-to-2D model. | ![GitHub Repo stars](https://img.shields.io/github/stars/ashawkey/stable-dreamfusion) |
| [IOPaint](https://github.com/Sanster/IOPaint) | IOPaint is an open-source image inpainting and editing tool, formerly LaMa Cleaner. | ![GitHub Repo stars](https://img.shields.io/github/stars/Sanster/IOPaint) |
| [Three Studio](https://github.com/threestudio-project/threestudio) | Threestudio is an unified framework for 3D content creation from text prompts, single images, and few-shot images, by lifting 2D text-to-image generation models. | ![GitHub Repo stars](https://img.shields.io/github/stars/threestudio-project/threestudio) |
| [Dream Textures](https://github.com/carson-katri/dream-textures) | Dream Textures let you create textures, concept art, background assets, and more with a simple text prompt on Blender. | ![GitHub Repo stars](https://img.shields.io/github/stars/carson-katri/dream-textures) |
| [PhotoMaker](https://github.com/TencentARC/PhotoMaker) | PhotoMaker let you customize Realistic Human Photos via Stacked ID Embedding. | ![GitHub Repo stars](https://img.shields.io/github/stars/TencentARC/PhotoMaker) |
| [Diffusers](https://github.com/huggingface/diffusers) | Library of pretrained diffusion models and generation pipelines. | ![GitHub Repo stars](https://img.shields.io/github/stars/huggingface/diffusers) |

## Code Assistant
| Name | Description | Repos |
|------|-------------|-------|
| [Refact](https://github.com/smallcloudai/refact) | Refact is an open-source AI coding assistant with blazing-fast code completion, powerful code improvement tools, and chat. | ![GitHub Repo stars](https://img.shields.io/github/stars/smallcloudai/refact) |
| [Draw a UI](https://github.com/SawyerHood/draw-a-ui) | Draw a mockup and generate html for it using AI. | ![GitHub Repo stars](https://img.shields.io/github/stars/SawyerHood/draw-a-ui) |
| [Continue](https://github.com/continuedev/continue) | Continue is an open-source autopilot for VS Code and JetBrains—the easiest way to code with any LLM. | ![GitHub Repo stars](https://img.shields.io/github/stars/continuedev/continue) |
| [Sweep AI](https://github.com/sweepai/sweep) | Sweep is an AI junior developer that turns bugs and feature requests into code changes. | ![GitHub Repo stars](https://img.shields.io/github/stars/sweepai/sweep) |
| [Cody Dev](https://sourcegraph.com/docs/cody) | Sourcegraph's coding assistant uses codebase context for chat, completions, and edits. | - |
| [Aider](https://github.com/Aider-AI/aider) | Aider is a command line tool that lets you pair program with GPT-3.5/GPT-4, to edit code stored in your local git repository. | ![GitHub Repo stars](https://img.shields.io/github/stars/Aider-AI/aider) |
| [AutoPR](https://github.com/irgolic/AutoPR) | AutoPR provides an automated pull request workflow. It's designed to help automate tasks in a pull request process. | ![GitHub Repo stars](https://img.shields.io/github/stars/irgolic/AutoPR) |
| [Bloop](https://github.com/BloopAI/bloop) | bloop is ChatGPT for your code. Ask questions in natural language, search for code and generate patches using your existing codebase as context. | ![GitHub Repo stars](https://img.shields.io/github/stars/BloopAI/bloop) |
| [ChatDev](https://github.com/OpenBMB/ChatDev) | ChatDev stands as a virtual software company that operates through various intelligent agents holding different roles. | ![GitHub Repo stars](https://img.shields.io/github/stars/OpenBMB/ChatDev) |
| [Cody Assistant](https://github.com/ajhous44/cody) | Cody is your AI Coding Assistant designed to let you interactively query your codebase using natural language. | ![GitHub Repo stars](https://img.shields.io/github/stars/ajhous44/cody) |
| [GPT Engineer](https://github.com/AntonOsika/gpt-engineer) | Specify what you want it to build, the AI asks for clarification, and then builds it. | ![GitHub Repo stars](https://img.shields.io/github/stars/AntonOsika/gpt-engineer) |
| [GPT Migrate](https://github.com/joshpxyne/gpt-migrate) | Easily migrate your codebase from one framework or language to another. | ![GitHub Repo stars](https://img.shields.io/github/stars/joshpxyne/gpt-migrate) |
| [GPT Pilot](https://github.com/Pythagora-io/gpt-pilot) | GPT Pilot is a true AI developer that writes code, debugs it, talks to you when it needs help, etc. | ![GitHub Repo stars](https://img.shields.io/github/stars/Pythagora-io/gpt-pilot) |
| [OpenAI Codex](https://github.com/openai/codex) | Coding agent that can work in a local development environment. | ![GitHub Repo stars](https://img.shields.io/github/stars/openai/codex) |
| [Claude Code](https://github.com/anthropics/claude-code) | Agentic coding tool for terminals and IDEs. | ![GitHub Repo stars](https://img.shields.io/github/stars/anthropics/claude-code) |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | Open-source terminal agent powered by Gemini. | ![GitHub Repo stars](https://img.shields.io/github/stars/google-gemini/gemini-cli) |
| [OpenHands](https://github.com/OpenHands/OpenHands) | Open-source platform for software development agents. | ![GitHub Repo stars](https://img.shields.io/github/stars/OpenHands/OpenHands) |
| [Cline](https://github.com/cline/cline) | Coding agent extension for VS Code. | ![GitHub Repo stars](https://img.shields.io/github/stars/cline/cline) |
| [Roo Code](https://github.com/RooCodeInc/Roo-Code) | Open-source coding agent extension for VS Code. | ![GitHub Repo stars](https://img.shields.io/github/stars/RooCodeInc/Roo-Code) |

## Autonomous Agents
| Name | Description | Repos |
|------|-------------|-------|
| [pinokio](https://github.com/pinokiocomputer/pinokio) | Pinokio is a browser that lets you install, run, and automate any AI applications and models automatically and effortlessly. | ![GitHub Repo stars](https://img.shields.io/github/stars/pinokiocomputer/pinokio) |
| [AgentGPT](https://github.com/reworkd/AgentGPT) | AgentGPT allows you to configure and deploy Autonomous AI agents. Name your own custom AI and have it embark on any goal imaginable. | ![GitHub Repo stars](https://img.shields.io/github/stars/reworkd/AgentGPT) |
| [SuperAGI](https://github.com/TransformerOptimus/SuperAGI) | SuperAGI is a dev-first open source autonomous AI agent framework enabling developers to build, manage & run useful autonomous agents. | ![GitHub Repo stars](https://img.shields.io/github/stars/TransformerOptimus/SuperAGI) |
| [LocalGPT](https://github.com/PromtEngineer/localGPT) | Chat with your documents on your local device using GPT models. No data leaves your device and 100% private. | ![GitHub Repo stars](https://img.shields.io/github/stars/PromtEngineer/localGPT) |
| [Agentlabs](https://github.com/agentlabs-dev/agentlabs) | Open-source universal frontend for your AI Agents that you can control with a realtime bidirectional streaming SDK from your backend. | ![GitHub Repo stars](https://img.shields.io/github/stars/agentlabs-dev/agentlabs) |
| [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | AutoGPT is the vision of accessible AI for everyone, to use and to build on. It provide the tools, so that you can focus on what matters. | ![GitHub Repo stars](https://img.shields.io/github/stars/Significant-Gravitas/AutoGPT) |
| [Baby AGI](https://github.com/yoheinakajima/babyagi) | BabyAGI is an AI-powered task management system using OpenAI and vector databases to create, prioritize, and execute tasks. | ![GitHub Repo stars](https://img.shields.io/github/stars/yoheinakajima/babyagi) |
| [CrewAI](https://github.com/crewAIInc/crewAI) | Crew AI is a cutting-edge framework for orchestrating role-playing, autonomous AI agents for tackling complex tasks. | ![GitHub Repo stars](https://img.shields.io/github/stars/crewAIInc/crewAI) |
| [Adala](https://github.com/HumanSignal/Adala) | Adala offers a robust framework for implementing agents specialized in data processing, with an emphasis on diverse data labeling tasks. | ![GitHub Repo stars](https://img.shields.io/github/stars/HumanSignal/Adala) |
| [Agent4Rec](https://github.com/LehengTHU/Agent4Rec) | Agent4Rec, a recommender system simulator with 1,000 LLM-empowered generative agents initialized from the MovieLens-1M dataset. | ![GitHub Repo stars](https://img.shields.io/github/stars/LehengTHU/Agent4Rec) |
| [AgentForge](https://github.com/DataBassGit/AgentForge) | AgentForge is a low-code framework tailored for the rapid development, testing, and iteration of AI-powered autonomous agents and Cognitive Architectures. | ![GitHub Repo stars](https://img.shields.io/github/stars/DataBassGit/AgentForge) |
| [AI Waves Agents](https://github.com/aiwaves-cn/agents) | AI Waves Agents is an open-source library/framework for building autonomous language agents  by simply filling in a config file in natural language. | ![GitHub Repo stars](https://img.shields.io/github/stars/aiwaves-cn/agents) |
| [AgentVerse](https://github.com/OpenBMB/AgentVerse) | AgentVerse is designed to facilitate the deployment of multiple LLM-based agents in various applications providing two frameworks: task-solving and simulation. | ![GitHub Repo stars](https://img.shields.io/github/stars/OpenBMB/AgentVerse) |
| [AutoGen](https://github.com/microsoft/autogen) | AutoGen is a framework that enables the development of LLM applications using multiple agents that can converse with each other to solve tasks. | ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/autogen) |
| [BambooAI](https://github.com/pgalko/BambooAI) | BambooAI is a lightweight library that leverages Language Models (LLMs) to enable natural language interactions, allowing you to source and converse with data. | ![GitHub Repo stars](https://img.shields.io/github/stars/pgalko/BambooAI) |
| [BeeBot](https://github.com/erik-megarad/beebot) | BeeBot is your personal worker bee, an Autonomous AI Assistant designed to perform a wide range of practical tasks autonomously. | ![GitHub Repo stars](https://img.shields.io/github/stars/erik-megarad/beebot) |
| [BondAI](https://github.com/krohling/bondai) | BondAI is an open source, AI-powered assistant with a lightweight, versatile API for seamless integration into your own applications. | ![GitHub Repo stars](https://img.shields.io/github/stars/krohling/bondai) |
| [Camel AI Agent](https://github.com/camel-ai/camel) | CAMEL AI: Communicative Agents for “Mind” Exploration of Large Language Model Society. | ![GitHub Repo stars](https://img.shields.io/github/stars/camel-ai/camel) |
| [GenIA](https://github.com/genia-dev/GeniA) | Meet your new AI platform engineering team member, it is able to work alongside you in your production environment, executing tasks on your behalf. | ![GitHub Repo stars](https://img.shields.io/github/stars/genia-dev/GeniA) |
| [GPT Researcher](https://github.com/assafelovic/gpt-researcher) | GPT Researcher is an autonomous agent designed for comprehensive online research on a variety of tasks. | ![GitHub Repo stars](https://img.shields.io/github/stars/assafelovic/gpt-researcher) |
| [IX Platform](https://github.com/kreneskyp/ix) | IX is a platform for designing and deploying autonomous and semi-autonomous LLM powered agents and workflows. | ![GitHub Repo stars](https://img.shields.io/github/stars/kreneskyp/ix) |
| [Jarvis](https://github.com/microsoft/JARVIS) | The mission of JARVIS is to explore artificial general intelligence (AGI) and deliver cutting-edge research to the whole community. | ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/JARVIS) |
| [Letta](https://github.com/letta-ai/letta) | Letta provides stateful agents and memory management; formerly MemGPT. | ![GitHub Repo stars](https://img.shields.io/github/stars/letta-ai/letta) |
| [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | MetaGPT is a Multi-Agent Framework. Assign different roles to GPTs to form a collaborative software entity for complex tasks. | ![GitHub Repo stars](https://img.shields.io/github/stars/FoundationAgents/MetaGPT) |
| [MiniAGI](https://github.com/muellerberndt/mini-agi) | MiniAGI is a simple autonomous agent compatible with GPT-3.5-Turbo and GPT-4. | ![GitHub Repo stars](https://img.shields.io/github/stars/muellerberndt/mini-agi) |
| [OpenAgents](https://github.com/xlang-ai/OpenAgents) | OpenAgents is an open platform for using and hosting language agents in the wild of everyday life. | ![GitHub Repo stars](https://img.shields.io/github/stars/xlang-ai/OpenAgents) |
| [Open Interpreter](https://github.com/openinterpreter/openinterpreter) | Let language models run code on your computer. An open-source, locally running implementation of OpenAI's Code Interpreter. | ![GitHub Repo stars](https://img.shields.io/github/stars/openinterpreter/openinterpreter) |
| [PromethAI Backend](https://github.com/topoteretes/PromethAI-Backend) | PromethAI is a Python AGI project that recommends choices based on a user's goals and preferences and can modify its recommendations based on user feedback. | ![GitHub Repo stars](https://img.shields.io/github/stars/topoteretes/PromethAI-Backend) |
| [SuperAgent](https://github.com/superagent-ai/superagent) | SuperAgent is an open-source agent framework that enables any developer to integrate production-ready AI Assistants into any application in a matter of minutes. | ![GitHub Repo stars](https://img.shields.io/github/stars/superagent-ai/superagent) |
| [X Agent](https://github.com/OpenBMB/XAgent) | XAgent is an open-source experimental Large Language Model (LLM) driven autonomous agent that can automatically solve various tasks. | ![GitHub Repo stars](https://img.shields.io/github/stars/OpenBMB/XAgent) |
| [Pydantic AI](https://github.com/pydantic/pydantic-ai) | Python framework for building typed AI agents. | ![GitHub Repo stars](https://img.shields.io/github/stars/pydantic/pydantic-ai) |
| [LangGraph](https://github.com/langchain-ai/langgraph) | Framework for stateful agent workflows. | ![GitHub Repo stars](https://img.shields.io/github/stars/langchain-ai/langgraph) |
| [MCP Servers](https://github.com/modelcontextprotocol/servers) | Reference implementations of Model Context Protocol servers. | ![GitHub Repo stars](https://img.shields.io/github/stars/modelcontextprotocol/servers) |

## Knowledge Manager
| Name | Description | Repos |
|------|-------------|-------|
| [Anything LLM](https://github.com/Mintplex-Labs/anything-llm) | Open-source ChatGPT equivalent experience for both open and close source LLMs, embedders, and vector databases. | ![GitHub Repo stars](https://img.shields.io/github/stars/Mintplex-Labs/anything-llm) |
| [Docs GPT](https://github.com/arc53/docsgpt) | DocsGPT is a cutting-edge open-source solution that streamlines the process of finding information in the project documentation. | ![GitHub Repo stars](https://img.shields.io/github/stars/arc53/docsgpt) |
| [Quivr](https://github.com/The-Vibe-Company/quivr) | Quivr, your second brain, utilizes the power of GenerativeAI to be your personal assistant. | ![GitHub Repo stars](https://img.shields.io/github/stars/The-Vibe-Company/quivr) |
| [Chaindesk](https://github.com/gmpetrov/databerry) | The no-code platform for building custom LLM Agents that provides a solution to quickly setup a semantic search system over your personal data. | ![GitHub Repo stars](https://img.shields.io/github/stars/gmpetrov/databerry) |
| [Solid GPT](https://github.com/AI-Citizen/SolidGPT) | Chat with your code repository, ask repository-level code questions, and discuss your requirements. | ![GitHub Repo stars](https://img.shields.io/github/stars/AI-Citizen/SolidGPT) |
| [Examor](https://github.com/codeacme17/examor) | Examor is a web application that allows you to take exams based on your knowledge notes. Let you really remember what you have learned and written. | ![GitHub Repo stars](https://img.shields.io/github/stars/codeacme17/examor) |
| [Second Brain](https://github.com/flepied/second-brain-agent) | Second Brain AI Agents offer a way to seamlessly index, search and interact with all your contents, markdown files, videos, web pages, and PDFs. | ![GitHub Repo stars](https://img.shields.io/github/stars/flepied/second-brain-agent) |
| [Gerev](https://github.com/GerevAI/gerev) | Gerev is an AI-powered enterprise search engine that let you find any conversation, doc, or internal page in seconds. | ![GitHub Repo stars](https://img.shields.io/github/stars/GerevAI/gerev) |
| [PrivateGPT](https://github.com/zylon-ai/private-gpt) | PrivateGPT is a production-ready AI project that allows you to ask questions about your documents using the power of Large Language Models (LLMs). | ![GitHub Repo stars](https://img.shields.io/github/stars/zylon-ai/private-gpt) |
| [TxtAI](https://github.com/neuml/txtai) | txtAI is an all-in-one embeddings database for semantic search, LLM orchestration and language model workflows. | ![GitHub Repo stars](https://img.shields.io/github/stars/neuml/txtai) |
| [Swirl](https://github.com/swirlai/swirl-search) | Swirl is an open source software that simultaneously searches multiple content sources and returns AI ranked results. | ![GitHub Repo stars](https://img.shields.io/github/stars/swirlai/swirl-search) |
| [Onyx](https://github.com/onyx-dot-app/onyx) | Onyx is a self-hosted search and AI assistant for organizational knowledge; formerly Danswer. | ![GitHub Repo stars](https://img.shields.io/github/stars/onyx-dot-app/onyx) |

## LLMs Eval
| Name | Description | Repos |
|------|-------------|-------|
| [AlpacaEval](https://github.com/tatsu-lab/alpaca_eval) | An automatic evaluator for instruction-following language models. Human-validated, high-quality, cheap, and fast. | ![GitHub Repo stars](https://img.shields.io/github/stars/tatsu-lab/alpaca_eval) |
| [FastChat](https://github.com/lm-sys/FastChat) | FastChat is a benchmark platform for large language models (LLMs) that features anonymous, randomized battles in a crowdsourced manner. | ![GitHub Repo stars](https://img.shields.io/github/stars/lm-sys/FastChat) |
| [BigCode Eval](https://github.com/bigcode-project/bigcode-evaluation-harness) | BigCode Evaluation Harness is a framework for the evaluation of autoregressive code generation language models. | ![GitHub Repo stars](https://img.shields.io/github/stars/bigcode-project/bigcode-evaluation-harness) |
| [Promptfoo](https://github.com/promptfoo/promptfoo) | Test your prompts, models, RAGs. Evaluate and compare LLM outputs, catch regressions, and improve prompt quality. | ![GitHub Repo stars](https://img.shields.io/github/stars/promptfoo/promptfoo) |
| [Ragas](https://github.com/vibrantlabsai/ragas) | Evaluation framework for retrieval-augmented generation and LLM applications. | ![GitHub Repo stars](https://img.shields.io/github/stars/vibrantlabsai/ragas) |
| [DeepEval](https://github.com/confident-ai/deepeval) | Open-source testing and evaluation framework for LLM applications. | ![GitHub Repo stars](https://img.shields.io/github/stars/confident-ai/deepeval) |
| [Langfuse](https://github.com/langfuse/langfuse) | Open-source LLM observability, prompt management, and evaluation platform. | ![GitHub Repo stars](https://img.shields.io/github/stars/langfuse/langfuse) |
| [Phoenix](https://github.com/Arize-ai/phoenix) | Open-source tracing and evaluation for AI applications. | ![GitHub Repo stars](https://img.shields.io/github/stars/Arize-ai/phoenix) |

## LLMs Framework
| Name | Description | Repos |
|------|-------------|-------|
| [Pezzo](https://github.com/pezzolabs/pezzo) | Pezzo is an open-source, developer-first LLMOps platform designed to streamline prompt design, version management, instant delivery, observability and more. | ![GitHub Repo stars](https://img.shields.io/github/stars/pezzolabs/pezzo) |
| [Lunary](https://github.com/appl-team/lunary) | Lunary provides observability, prompt management, and evaluation for LLM applications. | ![GitHub Repo stars](https://img.shields.io/github/stars/appl-team/lunary) |
| [Ludwig](https://github.com/ludwig-ai/ludwig) | Ludwig is a low-code framework for building custom AI models like LLMs and other deep neural networks. | ![GitHub Repo stars](https://img.shields.io/github/stars/ludwig-ai/ludwig) |
| [Langdroid](https://github.com/langroid/langroid) | Langroid is an intuitive, lightweight, extensible and principled Python framework to easily build LLM-powered applications, from ex-CMU and UW-Madison researchers. | ![GitHub Repo stars](https://img.shields.io/github/stars/langroid/langroid) |
| [LangChain](https://github.com/langchain-ai/langchain) | Langchain is aimed at assisting in the development of apps merging both LLMs and other sources of knowledge. | ![GitHub Repo stars](https://img.shields.io/github/stars/langchain-ai/langchain) |
| [LLMware](https://github.com/llmware-ai/llmware) | Llmware is a unified framework for developing LLM-based application patterns including Retrieval Augmented Generation (RAG). | ![GitHub Repo stars](https://img.shields.io/github/stars/llmware-ai/llmware) |
| [LLM App](https://github.com/pathwaycom/serviette) | LLM App is a production framework for building and serving AI applications and LLM-enabled real-time data pipelines. | ![GitHub Repo stars](https://img.shields.io/github/stars/pathwaycom/serviette) |
| [Dify](https://github.com/langgenius/dify) | Dify allows you to deploy your own version of Assistants API and GPTs, based on any LLMs. | ![GitHub Repo stars](https://img.shields.io/github/stars/langgenius/dify) |
| [NeumAI](https://github.com/NeumTry/NeumAI) | Neum AI is a data platform that helps developers leverage their data to contextualize Large Language Models through Retrieval Augmented Generation (RAG). | ![GitHub Repo stars](https://img.shields.io/github/stars/NeumTry/NeumAI) |
| [DB-GPT](https://github.com/eosphoros-ai/DB-GPT) | DB-GPT is an open-source framework designed for the realm of large language models (LLMs) within the database field. | ![GitHub Repo stars](https://img.shields.io/github/stars/eosphoros-ai/DB-GPT) |
| [Flowise](https://github.com/FlowiseAI/Flowise) | Flowise is a Drag & Drop UI to build your customized LLM automation flow. | ![GitHub Repo stars](https://img.shields.io/github/stars/FlowiseAI/Flowise) |
| [DSPy](https://github.com/stanfordnlp/dspy) | Framework for programming and optimizing language model pipelines. | ![GitHub Repo stars](https://img.shields.io/github/stars/stanfordnlp/dspy) |
| [Haystack](https://github.com/deepset-ai/haystack) | Framework for search, retrieval, and AI applications. | ![GitHub Repo stars](https://img.shields.io/github/stars/deepset-ai/haystack) |
| [LlamaIndex](https://github.com/run-llama/llama_index) | LlamaIndex is a data framework for LLM-based applications to ingest, structure, and access private or domain-specific data. | ![GitHub Repo stars](https://img.shields.io/github/stars/run-llama/llama_index) |
| [MindsDB](https://github.com/mindsdb/mindshub) | MindsDB connects data sources and AI models to build data-driven applications. | ![GitHub Repo stars](https://img.shields.io/github/stars/mindsdb/mindshub) |

## LLMs Training
| Name | Description | Repos |
|------|-------------|-------|
| [Colossal AI](https://github.com/hpcaitech/ColossalAI) | Maximize the runtime performance of your large neural networks with distributed techniques of Colossal-AI. | ![GitHub Repo stars](https://img.shields.io/github/stars/hpcaitech/ColossalAI) |
| [Megatron LM](https://github.com/NVIDIA/Megatron-LM) | Megatron is a large, powerful transformer developed by the Applied Deep Learning Research team at NVIDIA. | ![GitHub Repo stars](https://img.shields.io/github/stars/NVIDIA/Megatron-LM) |
| [DeepSpeed](https://github.com/deepspeedai/DeepSpeed) | DeepSpeed is a deep learning optimization library that makes distributed training and inference easy, efficient, and effective. | ![GitHub Repo stars](https://img.shields.io/github/stars/deepspeedai/DeepSpeed) |
| [Unsloth](https://github.com/unslothai/unsloth) | Unsloth is an open-source framework which allow you to unslow finetuning for Large Language Models. | ![GitHub Repo stars](https://img.shields.io/github/stars/unslothai/unsloth) |

## Vector Database
| Name | Description | Repos |
|------|-------------|-------|
| [Weaviate](https://github.com/weaviate/weaviate) | Weaviate is an open source vector database that is robust, scalable, cloud-native, and fast. | ![GitHub Repo stars](https://img.shields.io/github/stars/weaviate/weaviate) |
| [Milvus](https://github.com/milvus-io/milvus) | Milvus is an open-source vector database built to power embedding similarity search and AI applications. | ![GitHub Repo stars](https://img.shields.io/github/stars/milvus-io/milvus) |
| [Qdrant](https://github.com/qdrant/qdrant) | Qdrant is a vector similarity search engine and vector database. | ![GitHub Repo stars](https://img.shields.io/github/stars/qdrant/qdrant) |
| [Deep Lake](https://github.com/activeloopai/deeplake) | Deep Lake is a Database for AI powered by a storage format optimized for deep-learning applications. | ![GitHub Repo stars](https://img.shields.io/github/stars/activeloopai/deeplake) |
| [Chroma](https://github.com/chroma-core/chroma) | Chroma is the open-source embedding database. Chroma makes it easy to build LLM apps by making knowledge, facts, and skills pluggable for LLMs. | ![GitHub Repo stars](https://img.shields.io/github/stars/chroma-core/chroma) |
| [LanceDB](https://github.com/lancedb/lancedb) | Embedded database for vector search and multimodal data. | ![GitHub Repo stars](https://img.shields.io/github/stars/lancedb/lancedb) |
| [pgvector](https://github.com/pgvector/pgvector) | Vector similarity search extension for PostgreSQL. | ![GitHub Repo stars](https://img.shields.io/github/stars/pgvector/pgvector) |

## AI Course
| Name | Description | Repos |
|------|-------------|-------|
| [Microsoft AI Lab](https://github.com/microsoft/ailab) | AI Lab helps our large fast-growing community of developers get started on AI. | ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/ailab) |
| [ML Course Notes](https://github.com/dair-ai/ML-Course-Notes) | A place to collaborate and share lecture notes on all topics related to machine learning, NLP, and AI. | ![GitHub Repo stars](https://img.shields.io/github/stars/dair-ai/ML-Course-Notes) |
| [PE Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) | Prompt Engineering Guide is Github repo containing guides, papers, lecture, notebooks and resources for prompt engineering. | ![GitHub Repo stars](https://img.shields.io/github/stars/dair-ai/Prompt-Engineering-Guide) |
| [GenAI Lessons](https://github.com/microsoft/generative-ai-for-beginners) | A 12 Lesson course teaching everything you need to know to start building Generative AI applications. | ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/generative-ai-for-beginners) |
| [ML Youtube](https://github.com/dair-ai/ML-YouTube-Courses) | ML Youtube Courses is a Github repo indexing and organizing some of the best and most recent machine learning courses available on YouTube. | ![GitHub Repo stars](https://img.shields.io/github/stars/dair-ai/ML-YouTube-Courses) |
| [ML Papers](https://github.com/dair-ai/ML-Papers-Explained) | ML Papers Explained is a Github repo with explanations of the key concepts in Machine Learning. | ![GitHub Repo stars](https://img.shields.io/github/stars/dair-ai/ML-Papers-Explained) |
| [LLM Course](https://github.com/mlabonne/llm-course) | Course to get into Large Language Models (LLMs) with roadmaps and Colab notebooks. | ![GitHub Repo stars](https://img.shields.io/github/stars/mlabonne/llm-course) |
| [HF Courses](https://github.com/huggingface/course) | The Hugging Face  course teaches you about applying Transformers to various tasks in natural language processing and beyond. | ![GitHub Repo stars](https://img.shields.io/github/stars/huggingface/course) |

## Audio AI
| Name | Description | Repos |
|------|-------------|-------|
| [Bark UI](https://github.com/C0untFloyd/bark-gui) | BarkUI is a Gradio Web UI for text-prompted Generative Audio Model. | ![GitHub Repo stars](https://img.shields.io/github/stars/C0untFloyd/bark-gui) |
| [Tiny Diffusion](https://github.com/crlandsc/tiny-audio-diffusion) | Tiny Audio Diffusion is a repository for generating short audio samples and training waveform diffusion models on a consumer-grade GPU with less than 2GB VRAM. | ![GitHub Repo stars](https://img.shields.io/github/stars/crlandsc/tiny-audio-diffusion) |
| [Audio WebUI](https://github.com/gitmylo/audio-webui) | Audio WebUI is a webui for different audio related Neural Networks. | ![GitHub Repo stars](https://img.shields.io/github/stars/gitmylo/audio-webui) |
| [whisper.cpp](https://github.com/ggml-org/whisper.cpp) | High-performance inference of OpenAI's Whisper automatic speech recognition (ASR) model. Port of OpenAI's Whisper model in C/C++.    | ![GitHub Repo stars](https://img.shields.io/github/stars/ggml-org/whisper.cpp) |
| [F5-TTS](https://github.com/SWivid/F5-TTS) | Open-source text-to-speech system. | ![GitHub Repo stars](https://img.shields.io/github/stars/SWivid/F5-TTS) |
| [Whisper](https://github.com/openai/whisper) | Speech recognition and transcription model. | ![GitHub Repo stars](https://img.shields.io/github/stars/openai/whisper) |
| [Riffusion](https://github.com/riffusion/riffusion-app-hobby) | Riffusion is an app for real-time music generation with stable diffusion. | ![GitHub Repo stars](https://img.shields.io/github/stars/riffusion/riffusion-app-hobby) |
