from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import CharacterTextSplitter
import tempfile
import os

def load_and_chunk(uploaded_file):
     # Save the uploaded file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        tmp_file_path = tmp_file.name

     # Now pass the path to PyMuPDFLoader
    loader = PyMuPDFLoader(tmp_file_path)
    documents = loader.load()
    #loader = PyMuPDFLoader(uploaded_file)
    #documents = loader.load()
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_documents(documents)
