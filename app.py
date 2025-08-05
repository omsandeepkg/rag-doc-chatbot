import streamlit as st
from utils.document_loader import load_and_chunk
from utils.qa_chain import get_answer

st.title("📄 Chat with Your Document")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
query = st.text_input("Ask a question about your document:")

if uploaded_file and query:
    docs = load_and_chunk(uploaded_file)
    answer = get_answer(query, docs)
    st.write("🤖", answer)
