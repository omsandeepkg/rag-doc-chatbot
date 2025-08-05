from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

def get_answer(query, docs):
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)
    retriever = db.as_retriever()
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa.run(query)
