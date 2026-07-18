# Welcome to AI Engineer - Python LLM Learning Journey

This document outlines the structured roadmap, learning style, and curriculum for this Python LLM learning project.

---

## 💡 The Learning Style & Philosophy
This repository follows an **incremental, hands-on, and beginner-friendly** approach to mastering LLM applications. 

### 1. Hands-on First (Practical Over Heavy Theory)
Instead of deep-diving into the mathematical equations of neural networks, you start by writing code. Every concept is accompanied by a working python script that connects to a real LLM using the **Groq API**.

### 2. Day-by-Day Progression
Complex subjects are broken down into small, digestible daily tasks:
- **Modular Folders**: Each day has its own dedicated folder (e.g., `day1`, `day2`).
- **Focused Code**: Code examples are kept under 50-80 lines of code, focusing on exactly one concept at a time.
- **Isolated Environments**: Each day has its own `requirements.txt` and `.gitignore` file so that you can install only what is needed.

### 3. Clear & Structured Documentation
Every folder contains a detailed `README.md` that serves as a study note. It explains:
- **What** the concept is (in plain language).
- **Why** it is useful.
- **How** to implement it (with code blocks).
- **Important takeaways** to avoid common mistakes (like leaking API keys).

---

## 📅 The 9-Week Curriculum Roadmap

Here is the master plan for the learning journey, progressing from absolute fundamentals to production-ready agentic systems:

### 🚀 Phase 1: Foundations & Prompting
*   **Week 1: LLM Fundamentals + API Mastery**
    *   *Focus*: Initializing clients (Groq), handling environment variables (`.env`), understanding messages/roles (`system`, `user`, `assistant`), temperature settings, and handling tokens/finish reasons.
*   **Week 2: Prompt Engineering + Structured Outputs**
    *   *Focus*: Designing professional prompt templates (ROLE, TASK, CONSTRAINTS, EXAMPLES, FALLBACK). Forcing models to return structured data like JSON schemas using **Pydantic**.
    *   *Capstone Mini-Project*: Building a **Resume Evaluator** that parses documents and runs structured matching.

### 🧠 Phase 2: Knowledge Retrieval (RAG)
*   **Week 3: RAG Foundations**
    *   *Focus*: Building Retrieval-Augmented Generation systems. Learning how to chunk text, create embeddings, store them in vector databases, and retrieve context to answer queries.
*   **Week 4: Advanced RAG + Evaluation**
    *   *Focus*: Optimizing retrieval (hybrid search, re-ranking, query translation) and evaluating retrieval quality (using frameworks like Ragas or custom metrics).

### 🤖 Phase 3: Autonomous Agents
*   **Week 5: Agents + Tool Use**
    *   *Focus*: Teaching LLMs to use external tools (e.g., executing code, searching the web, calling APIs) based on user requests.
*   **Week 6: LangGraph + MCP + Multi-Agent**
    *   *Focus*: Designing complex state machines and multi-agent workflows using **LangGraph** and Model Context Protocol (MCP) for tool coordination.

### 🛡️ Phase 4: Production & Deployment
*   **Week 7: Observability + Guardrails + Security**
    *   *Focus*: Monitoring LLM applications (tokens, latency, traces), implementing safety guardrails (content moderation, prompt injection protection), and securing API endpoints.
*   **Week 8: Deployment + Fine-Tuning + Capstone**
    *   *Focus*: Deploying the models/pipelines to production, understanding when and how to fine-tune an LLM, and building a fully integrated capstone project.
*   **Bonus: Interview Prep + Resume Building**
    *   *Focus*: Preparing for industry-specific AI engineering roles, explaining system design for LLMs, and packaging this learning journey into a premium portfolio.

---

## 🛠️ How to Navigate This Workspace
1.  **Check out the days**: Go inside any day directory (e.g., `day1/`, `day2/`) to start learning.
2.  **Read the notes**: Read the local `README.md` first to understand the concepts.
3.  **Run the script**: Run the python script (e.g., `python hello.py` or `python prompt_eng.py`) to see it in action.
4.  **Experiment**: Modify variables, play with prompts, and see how the model's output changes!
