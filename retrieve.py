import dotenv
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

PDF = "data/"
REVIEWS_CHROMA_PATH = "chroma_data"

dotenv.load_dotenv()


loader=DirectoryLoader(PDF,glob="**/*.pdf",show_progress=True,loader_cls=PyPDFLoader)
document = loader.load()

embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vector_db = Chroma.from_documents(
    documents=document,
    embedding=embedding_model,
    persist_directory=REVIEWS_CHROMA_PATH
)

vector_db.persist()