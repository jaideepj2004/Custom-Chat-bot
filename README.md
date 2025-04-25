🌟 Overview

The Personal Information Q&A System is a web application built with Streamlit that allows you to upload any PDF document and ask questions about its content. It uses a Retrieval-Augmented Generation (RAG) approach to retrieve the most relevant passages and deliver grounded, context-rich answers. Instead of pressing Enter, simply click 🔍 Search to apply your query.

✨ Features

Feature

Description

📄 PDF Upload

Upload and process any PDF document via the sidebar.

📜 Sentence Split

NLTK’s punkt tokenizer splits text into clean sentences.

🤖 Embeddings

all-MiniLM-L6-v2 converts text to semantic vectors.

🔍 Similarity

Cosine similarity finds the most relevant passages.

🎨 Interactive UI

Color-coded relevance with a smooth Streamlit interface.

🛠️ Table of Contents

Prerequisites

Installation

Quick Start

Usage

Architecture

Configuration

Troubleshooting

License

Acknowledgments

📋 Prerequisites

Python 3.7 or later

pip (Python package manager)

🔧 Installation

git clone https://github.com/yourusername/personal-info-qa.git
cd personal-info-qa

# (Optional) Create & activate a virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

Note: If you don’t have requirements.txt, install manually:

pip install streamlit nltk sentence-transformers numpy scikit-learn PyPDF2

🚀 Quick Start

streamlit run app.py

Open your browser at http://localhost:8501

Upload your PDF.

Ask your question and click 🔍 Search to apply.

🤔 Usage

Select and upload your PDF document via the sidebar.

Type your question in the input box.

Click 🔍 Search (don’t press Enter) to retrieve answers.

🤖 Architecture

Model: all-MiniLM-L6-v2 via SentenceTransformers

Tokenizer: NLTK punkt for sentence splitting

Parser: PyPDF2 for PDF text extraction

Similarity: scikit-learn’s cosine_similarity over NumPy arrays

UI: Streamlit for interactive frontend

⚙️ Configuration

Model Selection: Change in personal_rag_system.py:

self.model = SentenceTransformer('your-model-name')

Top-K Results: Adjust top_k in answer_question().

🛠️ Troubleshooting

Empty Output: Ensure PDF is text-based, not scanned.

Slow Embedding: Use smaller docs or lighter models.

NLTK Errors: Download tokenizer manually:

import nltk
nltk.download('punkt')

📄 License

Distributed under the MIT License. See LICENSE for details.

🙏 Acknowledgments

Streamlit

SentenceTransformers

NLTK

© 2025 Jaideep Jaiswal. Made with ❤️
