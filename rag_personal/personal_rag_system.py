import nltk
from nltk.tokenize import sent_tokenize
from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2
import logging

# Download required NLTK data
nltk.download('punkt')

class PersonalRAGSystem:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.documents = []
        self.embeddings = None
        
    def load_pdf(self, pdf_path):
        """Load and process PDF document"""
        try:
            text = ""
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    text += page.extract_text()
            
            # Split text into sentences
            self.documents = sent_tokenize(text)
            print(f"Processed {len(self.documents)} sentences from PDF")
            
            # Create embeddings for all sentences
            if len(self.documents) > 0:
                self.embeddings = self.model.encode(self.documents)
                return True
            return False
            
        except Exception as e:
            print(f"Error loading PDF: {str(e)}")
            return False
        
    def answer_question(self, question, top_k=3):
        """Find relevant context and answer the question"""
        try:
            # Check if we have documents and embeddings
            if len(self.documents) == 0 or self.embeddings is None:
                return {
                    'relevant_context': [],
                    'similarity_scores': [],
                    'error': 'No document loaded'
                }
            
            # Encode the question
            question_embedding = self.model.encode([question])[0]
            
            # Calculate similarity scores
            similarities = cosine_similarity([question_embedding], self.embeddings)[0]
            
            # Get top k most relevant sentences
            top_k = min(top_k, len(similarities))  # Make sure we don't exceed array length
            top_indices = np.argsort(similarities)[-top_k:][::-1]
            
            # Get relevant contexts and scores
            relevant_context = [self.documents[i] for i in top_indices]
            similarity_scores = similarities[top_indices]
            
            print(f"Found {len(relevant_context)} relevant passages")
            print(f"Top similarity score: {np.max(similarities)}")
            
            return {
                'relevant_context': relevant_context,
                'similarity_scores': similarity_scores.tolist(),
                'error': None
            }
            
        except Exception as e:
            print(f"Error answering question: {str(e)}")
            return {
                'relevant_context': [],
                'similarity_scores': [],
                'error': str(e)
            }

    def get_document_stats(self):
        """Return basic statistics about the loaded document"""
        return {
            'total_sentences': len(self.documents),
            'has_embeddings': self.embeddings is not None,
            'embedding_shape': self.embeddings.shape if self.embeddings is not None else None
        }