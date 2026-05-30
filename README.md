# Multi-LLM Context Routing System

## Overview

The Multi-LLM Context Routing System is an AI orchestration platform that manages long-running conversations across multiple Large Language Models (LLMs). The system monitors conversation growth, compresses historical context through summarization, and automatically routes conversations between different AI providers while preserving conversational continuity.

This project demonstrates concepts used in modern AI agents, workflow automation systems, and context management platforms.

---

## Features

* Multi-LLM Routing (Gemini ↔ Groq Llama)
* Token Usage Monitoring
* Automatic Context Summarization
* Persistent Conversation Memory
* Context Transfer Across Models
* JSON-Based Memory Storage
* Configurable Routing Thresholds
* Interactive Command-Line Interface

---

## System Architecture

User
↓
Memory Manager
↓
Token Monitor
↓
Router Engine
↓
Gemini / Groq
↓
Response

When the conversation exceeds a predefined threshold:

1. Conversation history is analyzed.
2. Historical context is summarized.
3. Important information is retained.
4. Context is transferred to another model.
5. The conversation continues seamlessly.

---

## Workflow

### Normal Flow

User Query
↓
Gemini
↓
Response

### Routing Flow

User Query
↓
Token Threshold Reached
↓
Conversation Summarization
↓
Context Packaging
↓
Groq (Llama)
↓
Response

---

## Technologies Used

* Python
* Google Gemini API
* Groq API
* JSON
* Prompt Engineering
* REST API Concepts

---

## Project Structure

```text
llm-router/

├── app.py
├── config.py
├── memory.py
├── providers.py
├── router.py
├── summarizer.py
├── token_monitor.py
├── chat_history.json
├── summary.json
├── requirements.txt
└── .env
```

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd llm-router
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

## Running the Application

```bash
python3 app.py
```

---

## Available Commands

| Command | Description                |
| ------- | -------------------------- |
| exit    | Close application          |
| quit    | Close application          |
| bye     | Close application          |
| clear   | Clear conversation history |

---

## Key Concepts Implemented

### Token Monitoring

The system continuously estimates conversation size and tracks context growth.

### Context Compression

Historical conversations are compressed into structured summaries while preserving:

* User goals
* Project information
* Technical decisions
* Future tasks

### Context Transfer

The router transfers:

* Conversation Summary
* Recent Messages
* Current User Query

between models to maintain continuity.

### Dynamic Routing

Requests are routed automatically when conversation size exceeds a configurable threshold.

---

## Future Enhancements

* FastAPI Integration
* Postman API Testing
* Vector Database Memory (ChromaDB / FAISS)
* Intelligent Model Selection
* Web-Based User Interface
* Cost-Aware Routing
* Task-Specific Model Selection

---

## Resume Impact

This project demonstrates:

* AI Workflow Automation
* API Integration
* Prompt Engineering
* Context Management
* Multi-LLM Orchestration
* Memory Management Systems
* Python Development

---

## Author

Onkar Yende
