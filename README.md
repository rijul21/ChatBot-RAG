# ChatBot-RAG

**ChatBot-RAG** is a Retrieval-Augmented Generation (RAG) based conversational agent that leverages **LangChain**, **FAISS**, and **Streamlit** to enable context-aware Q&A from custom data sources. This project demonstrates how to ingest documents, generate embeddings, store them in a vector database, and query them during chatbot interactions.

---

## Tech Stack

- **LangChain** – Language model orchestration  
- **FAISS** – Fast vector similarity search for document retrieval  
- **Streamlit** – Interactive UI for the chatbot  
- **OpenAI / HuggingFace** – LLM backbone (can be swapped)  
- **Python** – Primary programming language

---

## Directory Structure

```
ChatBot-RAG/
├── data/                         # Input documents (.txt files)
├── vectorstore/db_faiss/        # Persisted FAISS index
├── bot.py                       # Streamlit frontend for chatbot
├── create_memory_for_llm.py     # Embeds and indexes documents
├── connect_memory_with_llm.py   # Chains vector memory with LLM
├── test.py                      # Test scripts and utilities
└── requirements.txt             # Python dependencies
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/rijul21/ChatBot-RAG.git
cd ChatBot-RAG
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> Ensure you have Python ≥ 3.7 and an OpenAI or HuggingFace API key set via environment variable.

### 3. Prepare Data

Place `.txt` documents inside the `data/` directory.

---

## Create Vector Memory

Run the script to generate vector embeddings and build the FAISS index.

```bash
python create_memory_for_llm.py
```

---

## Connect Memory with LLM

Set up LangChain with the indexed data:

```bash
python connect_memory_with_llm.py
```

---

## Launch Chatbot UI

Launch the chatbot with Streamlit frontend:

```bash
streamlit run bot.py
```

You’ll get an interactive UI where you can ask questions grounded in your uploaded documents.

---

## Testing (Optional)

Run `test.py` to verify embedding and retrieval logic:

```bash
python test.py
```

---

## Use Cases

- Internal knowledge base assistants  
- Academic document Q&A bots  
- Domain-specific helpdesks  
- Custom data-aware chat interfaces

---


