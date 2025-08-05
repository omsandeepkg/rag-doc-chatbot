# 🧠 GenAI Document Q&A System (RAG-based)

This is a beginner-friendly starter project that uses OpenAI + LangChain to create a document-based Q&A system using Retrieval-Augmented Generation (RAG).

## Features
- Upload a document (PDF/TXT)
- Ask questions in natural language
- Uses FAISS vector store to retrieve relevant chunks
- Powered by GPT-3.5 / GPT-4 via OpenAI API
- Built with Python + Streamlit

## Folder Structure
```
📁 data/         → Upload your documents here
📁 utils/        → Utility functions (embedding, parsing, etc.)
```

## To Run
```bash
pip install -r requirements.txt
streamlit run app.py
```
