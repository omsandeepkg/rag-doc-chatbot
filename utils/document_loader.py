from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import CharacterTextSplitter

def load_and_chunk(uploaded_file):
    loader = PyMuPDFLoader(uploaded_file)
    documents = loader.load()
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_documents(documents)
