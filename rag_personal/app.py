import streamlit as st
import tempfile
import os
from pathlib import Path

from personal_rag_system import PersonalRAGSystem

# Initialize session state
if 'rag_system' not in st.session_state:
    st.session_state.rag_system = None
if 'uploaded_file_path' not in st.session_state:
    st.session_state.uploaded_file_path = None

def main():
    st.title("Personal Information Q&A System")
    
    # File upload section
    st.sidebar.header("Upload Document")
    uploaded_file = st.sidebar.file_uploader("Choose your PDF file", type=['pdf'])

    if uploaded_file:
        # Save uploaded file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_path = tmp_file.name

        # Process new file
        if st.session_state.uploaded_file_path != tmp_path:
            with st.spinner('Processing document...'):
                rag_system = PersonalRAGSystem()
                success = rag_system.load_pdf(tmp_path)
                
                if success:
                    st.session_state.rag_system = rag_system
                    st.session_state.uploaded_file_path = tmp_path
                    st.sidebar.success("✅ Document loaded successfully!")
                    
                    # Show document stats
                    stats = rag_system.get_document_stats()
                    st.sidebar.write("📊 Document Statistics:")
                    st.sidebar.write(f"Total sentences: {stats['total_sentences']}")
                else:
                    st.error("Failed to process document")
                    return

        # Main Q&A interface
        st.write("💭 Ask a question about your document:")
        col1, col2 = st.columns([3, 1])
        
        with col1:
            question = st.text_input("", placeholder="Enter your question here...")
        
        with col2:
            search_button = st.button("🔍 Search", use_container_width=True)
        
        if search_button and question:
            if not question.strip():
                st.warning("Please enter a question")
                return
                
            with st.spinner('Searching for answer...'):
                result = st.session_state.rag_system.answer_question(question)
                
                # Check for errors
                if result.get('error'):
                    st.error(f"Error: {result['error']}")
                    return
                
                # Display results
                if result['relevant_context'] and len(result['relevant_context']) > 0:
                    st.subheader("📝 Answer")
                    for i, (text, score) in enumerate(zip(result['relevant_context'], 
                                                        result['similarity_scores']), 1):
                        # Create a colored box based on confidence score
                        color = "green" if score > 0.8 else "orange" if score > 0.6 else "red"
                        st.markdown(
                            f"""
                            <div style='padding: 10px; border-radius: 5px; 
                                      border-left: 5px solid {color}; 
                                      background-color: rgba(0,0,0,0.05); 
                                      margin: 10px 0;'>
                                <strong>Passage {i}</strong> (Relevance: {score:.2f})<br><br>
                                {text}
                            </div>
                            """, 
                            unsafe_allow_html=True
                        )
                else:
                    st.warning("No relevant information found for your question.")
    else:
        st.info("👆 Please upload a PDF document to begin")
    # Footer
    st.markdown("---")
    st.markdown("Made with ❤️ using Streamlit and RAG")
if __name__ == "__main__":
    main()