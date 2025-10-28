Perfect 👍 — here’s a **ready-to-copy PowerShell-friendly, single block** you can paste straight into your terminal.
It creates a **beautiful, professional `README.md`** for your repo — no edits required.

---

```powershell
cd ~/workshop

@'
# 🤖 AWS AI Agents Workshop — Strands & MCP

A hands-on exploration of building **AI Agents** using **AWS Bedrock**, **Anthropic Claude**, **Strands SDK**, and the **Model Context Protocol (MCP)**.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![AWS](https://img.shields.io/badge/AWS-Bedrock-orange)
![Strands](https://img.shields.io/badge/Strands-Agents-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📚 Table of Contents
- [Overview](#overview)
- [Modules](#modules)
- [Architecture](#architecture)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Key Learnings](#key-learnings)
- [Technologies Used](#technologies-used)
- [Future Work](#future-work)
- [References](#references)
- [License](#license)
- [Contact](#contact)

---

## 🎯 Overview
This repository contains my work from the **AWS AI Agents Workshop**, focusing on creating **multi-agent systems** powered by **Claude 3.5 Haiku** and **Strands Agents SDK**.  
It demonstrates how to integrate tools, build modular agents, and enable persistent memory — all using **AWS Bedrock** and the **Model Context Protocol (MCP)**.

---

## ✅ Modules

### 🧮 Module 1: MCP Calculator Agent
- Built a FastMCP server for calculator operations  
- Connected client and tools using MCP protocol  
📂 `strands_examples/mcp_calculator_example/`

---

### 🌦️ Module 2: Weather Agent
- Fetches real-time weather using the National Weather Service API  
- Demonstrates multi-step reasoning with HTTP tools  
📂 `strands_examples/weather_interactive.py`

---

### 📘 Module 3: Knowledge Base Agent
- Implements local RAG-style document retrieval  
- Demonstrates semantic search and custom tools  
📂 `strands_examples/local_kb_agent.py`

---

### 🤝 Module 4: Multi-Agent Workflow
- 3-agent pipeline (Researcher → Analyst → Writer)  
- Enables agent-to-agent communication  
📂 `strands_examples/agents_workflow.py`

---

### 🧠 Module 5: Memory Agent
- Persistent conversational memory with fact storage  
- State tracking across sessions  
📂 `strands_examples/memory_agent.py`

---

### 🧩 Module 7: Advanced Multi-Agent System
#### Part 1: Teacher’s Assistant (Orchestrator)
Five specialized agents routed by an orchestrator:
- 🔢 Math Assistant  
- 📝 English Assistant  
- 🌍 Language Assistant  
- 💻 CS Assistant  
- 🤖 General Assistant  
📂 `strands_examples/teachers_assistant.py`

#### Part 2: Streamlit Web UI
- Real-time chat interface  
- Visual routing indicators  
📂 `strands_examples/teachers_assistant_ui.py`

#### Part 3: Memory Integration
- Combines multi-agent routing with persistent memory  
📂 `strands_examples/teachers_assistant_with_memory.py`

---

## 🏗️ Architecture
```

```
                ┌─────────────────────────┐
                │        User Query        │
                └───────────┬─────────────┘
                            │
                            ↓
                ┌─────────────────────────┐
                │  🎓 Teacher's Assistant │
                │   (Orchestrator Agent)  │
                └───────────┬─────────────┘
                            │
        ┌───────────────────┼────────────────────┐
        │                   │                    │
        ↓                   ↓                    ↓
┌──────────────┐    ┌──────────────┐     ┌──────────────┐
│ 🔢 Math      │    │ 📝 English   │     │ 💻 CS        │
│  Assistant   │    │  Assistant   │     │  Assistant   │
└──────────────┘    └──────────────┘     └──────────────┘
```

````

---

## 🔧 Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/aws-ai-agents-workshop.git
cd aws-ai-agents-workshop
````

### 2️⃣ Create a Virtual Environment

```bash
# Using uv (recommended)
uv venv && source .venv/bin/activate

# Or using venv
python3 -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure AWS

```bash
aws configure
# Add AWS Access Key ID, Secret, region (us-east-1), and output (json)
```

---

## 🚀 Usage

### Run Multi-Agent System (CLI)

```bash
cd strands_examples
python teachers_assistant.py
```

### Example Queries

```
> Solve x^2 + 5x + 6 = 0
> Translate "Hello" to French
> Write a Python function to reverse a string
```

### Run the Web UI

```bash
cd strands_examples
streamlit run teachers_assistant_ui.py
```

🌐 Visit: [http://localhost:8501](http://localhost:8501)

---

## 📁 Project Structure

```
aws-ai-agents-workshop/
├── README.md
├── requirements.txt
├── strands_examples/
│   ├── teachers_assistant.py
│   ├── teachers_assistant_ui.py
│   ├── teachers_assistant_with_memory.py
│   ├── math_assistant.py
│   ├── english_assistant.py
│   ├── language_assistant.py
│   ├── computer_science_assistant.py
│   ├── memory_agent.py
│   ├── local_kb_agent.py
│   ├── weather_interactive.py
│   └── agents_workflow.py
├── local_kb/
│   ├── company_info.txt
│   ├── products.txt
│   ├── contact_support.txt
│   └── faq.txt
└── my_mcp_example/
    ├── mcp_server.py
    └── mcp_client.py
```

---

## 🎓 Key Learnings

* **Model Context Protocol (MCP):** standardized interface for tool integration
* **Multi-Agent Design:** orchestration, specialization, communication
* **Memory & State:** persistent and contextual conversations
* **Prompt Engineering:** defining clear agent roles and behaviors
* **Tool Integration:** connecting agents with HTTP APIs and calculators

---

## ⚙️ Technologies Used

* **AWS Bedrock** — Claude 3.5 Haiku
* **Strands Agents SDK** — Agent framework
* **Model Context Protocol (MCP)** — Tool standard
* **FastMCP**, **Streamlit**, **Boto3**, **LiteLLM**, **Python REPL**

---

## 🚧 Future Work

* [ ] Integrate with S3 for document storage
* [ ] Add vector search via OpenSearch
* [ ] Deploy on ECS/Fargate
* [ ] Add authentication via Cognito
* [ ] Enable caching, monitoring & logging
* [ ] Build REST API endpoints
* [ ] Multi-user support

---

## 📖 References

* [AWS Bedrock Docs](https://docs.aws.amazon.com/bedrock/)
* [Strands Agents SDK](https://github.com/awslabs/strands)
* [Model Context Protocol](https://modelcontextprotocol.io/)
* [Anthropic Claude](https://www.anthropic.com/claude)

---

## 📄 License

This project is licensed under the **MIT License** — see the LICENSE file for details.

---

## 🙏 Acknowledgments

* AWS Samples Team — for excellent workshop content
* Anthropic — for Claude and Strands SDK
* Open Source Community — for supporting tools and libraries

---

## 📞 Contact

**Author:** Mansi Gambhir
Built during the **AWS AI Agents Workshop (October 2025)**

⭐ *If you found this helpful, please star the repository!*

---

## ⚡ Quick Start

```bash
pip install -r requirements.txt
aws configure
cd strands_examples
python teachers_assistant.py
```

---

Made with ❤️ using **AWS**, **Anthropic Claude**, and **Strands Agents**
'@ | Out-File -Encoding utf8 README.md



Would you like me to add **badges for GitHub stars, forks, and last commit date** at the top for a more “GitHub-pro” look?
