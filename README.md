# Custom Chat-bot — Personal RAG System

A personal Retrieval-Augmented Generation (RAG) chatbot that lets you upload **any PDF document** and ask natural-language questions about it. The system encodes the document into semantic embeddings and retrieves the most relevant sentences to answer your queries — all running locally without an external LLM API.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Setup & Running](#setup--running)
- [API Reference](#api-reference)

---

## Overview

This chatbot is built around a **sentence-transformer embedding + cosine similarity** retrieval pipeline. You load a PDF, and the system splits it into sentences, encodes each sentence into a 384-dimensional embedding, and stores them in memory. When you ask a question, it encodes the question the same way and finds the top-k most semantically similar sentences from the document.

---

## Features

- Upload any PDF and immediately start querying it
- Semantic search using `all-MiniLM-L6-v2` (SentenceTransformers)
- Cosine similarity-based retrieval, no keyword matching
- Returns top-k relevant passages with similarity scores
- Document statistics endpoint
- Flask REST API + HTML frontend

---

## Tech Stack

| Component | Technology |
|---|---|
| Backend | Python, Flask |
| Embedding Model | `sentence-transformers` — `all-MiniLM-L6-v2` |
| Similarity Search | `scikit-learn` cosine_similarity |
| PDF Parsing | PyPDF2 |
| Sentence Tokenization | NLTK `sent_tokenize` |
| Frontend | HTML/CSS/JS |

---

## Project Structure

```
Custom-Chat-bot/
├── README.md
└── rag_personal/
    ├── app.py                     # Flask API server
    ├── personal_rag_system.py     # Core RAG logic (PDF loading + retrieval)
    └── requirements.txt           # Python dependencies
```

---

## How It Works

### `PersonalRAGSystem` class (`personal_rag_system.py`)

| Method | Description |
|---|---|
| `load_pdf(pdf_path)` | Reads PDF, tokenizes into sentences with NLTK, encodes all sentences using SentenceTransformer |
| `answer_question(question, top_k=3)` | Encodes question, computes cosine similarity with all sentence embeddings, returns top-k passages + scores |
| `get_document_stats()` | Returns total sentences, embedding shape |

### Retrieval Flow

```
PDF file
   ↓  PyPDF2 text extraction
   ↓  NLTK sentence tokenization
   ↓  SentenceTransformer encoding → embeddings matrix (N × 384)
   
User question
   ↓  SentenceTransformer encoding → query vector (1 × 384)
   ↓  Cosine similarity against all sentence embeddings
   ↓  Top-k indices by similarity score
   → Relevant passage(s) returned
```

---

## Setup & Running

```bash
git clone https://github.com/jaideepj2004/Custom-Chat-bot.git
cd Custom-Chat-bot/rag_personal
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

### `requirements.txt` includes:

```
sentence-transformers
PyPDF2
nltk
scikit-learn
numpy
flask
```

---

## API Reference

### `GET /`
Returns the chat interface.

### `POST /upload`
Upload a PDF file (multipart/form-data, field `pdf`).

### `POST /ask`
Ask a question about the uploaded PDF.
```json
{ "question": "What is the main conclusion of the paper?" }
```
**Response:**
```json
{
  "relevant_context": ["Passage 1...", "Passage 2..."],
  "similarity_scores": [0.87, 0.72],
  "error": null
}
```

### `GET /stats`
Returns document statistics (sentence count, embedding dimensions).
