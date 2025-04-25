Personal Information Q&A System

A simple Streamlit-based Q&A application that uses a Retrieval-Augmented Generation (RAG) approach to answer questions about the contents of a user-supplied PDF document.

Why RAG?

Retrieval-Augmented Generation (RAG) combines information retrieval with large-language-model generation to deliver accurate, context-rich answers:

Grounded Responses: By retrieving relevant passages directly from your document, the system ensures that answers are based on actual content, minimizing hallucinations.

Efficiency: Embeddings and nearest-neighbor search quickly identify the most pertinent context, reducing the input size for the generative model.

Scalability: RAG architectures can handle large documents by indexing and searching chunks, rather than processing everything at once.

Flexibility: The retrieved context can be fed into any downstream LLM, enabling further refinement or summarization of the answer. The system extracts sentences from the PDF, embeds them using a pre-trained SentenceTransformer model, and retrieves the most relevant passages in response to a user query.

Features

PDF Upload: Upload any PDF document via the Streamlit sidebar.

Sentence Extraction: Automatically split PDF text into sentences using NLTK.

Embeddings: Encode sentences with the SentenceTransformer (all-MiniLM-L6-v2) model.

Similarity Search: Compute cosine similarity between user queries and document sentences.

Interactive UI: Highlight relevant passages with confidence-based color coding.

Table of Contents

Prerequisites

Installation

File Structure

Usage

Configuration

Troubleshooting

License

Acknowledgments

Prerequisites

Python 3.7 or later

pip (Python package manager)

Installation

Clone the repository

git clone https://github.com/yourusername/personal-info-qa
cd personal-info-qa

Create and activate a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate     # On macOS/Linux
venv\Scripts\activate      # On Windows

Install dependencies

pip install -r requirements.txt

Note: If you don't have a requirements.txt, install packages manually:

pip install streamlit nltk sentence-transformers numpy scikit-learn PyPDF2

Download NLTK data

The application downloads the required NLTK punkt tokenizer on first run. If you prefer manual download:

import nltk
nltk.download('punkt')

File Structure

personal-info-qa/
├── app.py                     # Streamlit application
├── personal_rag_system.py     # RAG system implementation
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Ignore Python artifacts

Usage

Run the Streamlit app

streamlit run app.py

Upload a PDF

Click on the sidebar upload widget and select a PDF file.

Wait for processing (sentence extraction and embedding).

Ask Questions

Enter a question in the text input field and click Search.

Relevant passages will appear, color-coded by relevance (green/orange/red).

Architecture

Embedding Model: The system uses the pre-trained all-MiniLM-L6-v2 model from the SentenceTransformers library to generate dense semantic embeddings for each sentence.

Text Tokenization: Sentence splitting is handled by NLTK’s punkt tokenizer (downloaded at runtime if necessary).

PDF Parsing: Text extraction from uploaded PDFs is performed with PyPDF2.

Similarity Computation: Cosine similarity between query and sentence embeddings is computed using scikit-learn’s cosine_similarity.

Data Structures: Embeddings and similarity scores are managed using NumPy arrays.

Web Interface: The frontend is built with Streamlit, providing file upload, question input, and result display.

Configuration

Model Selection: By default, the system uses all-MiniLM-L6-v2. To change, modify the SentenceTransformer instantiation in personal_rag_system.py.

Top-K Results: Adjust the top_k parameter in answer_question() if you want more or fewer passages.

Troubleshooting

Blank Output or Errors: Ensure the PDF contains extractable text. Scanned or image-based PDFs may not yield any text.

Slow Performance: Embedding large documents can be time-consuming. Consider splitting PDFs or using a smaller model.

Missing NLTK Data: If you encounter LookupError: punkt not found, download the tokenizer manually (see Installation).

License

This project is released under the MIT License. See LICENSE for details.

Acknowledgments

Streamlit for the interactive UI.

SentenceTransformers for easy access to pre-trained embedding models.

NLTK for text processing utilities.

Made with ❤️ by Jaideep Jaiswal

