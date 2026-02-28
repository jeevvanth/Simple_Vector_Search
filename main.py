import dotenv

# from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma
# from langchain.schema.runnable import RunnablePassthrough
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel


CHROMA_PATH = "chroma_data/"

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vector_db = Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=embedding_model
)

retriever=vector_db.as_retriever(k=10)

while True:
    query=input("Enter your query: ")
    results=retriever.invoke(query)
    print(results)