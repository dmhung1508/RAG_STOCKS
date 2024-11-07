from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from uuid import uuid4
from tqdm import tqdm
from langchain_core.documents import Document
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
import chromadb
from chromadb.config import DEFAULT_TENANT, DEFAULT_DATABASE, Settings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Khởi tạo embeddings
embeddings = HuggingFaceEmbeddings(
    model_name='hiieu/halong_embedding',
)

# Khởi tạo Chroma client sử dụng HttpClient
client = chromadb.HttpClient(
    host="0.0.0.0",
    port=8505,
    ssl=False,
    headers=None,
    settings=Settings(),
    tenant=DEFAULT_TENANT,
    database=DEFAULT_DATABASE,
)

# Kết nối tới server Chroma thông qua client
vector_store = Chroma(
    collection_name="stocks_news",
    embedding_function=embeddings,
    client=client
)
def add_text(doc,id,date, source, sourceLink,article_content, symbol, category):
    docs = []
    load_docs = Document(
        id=id,
        page_content= doc,
        metadata={
            "date": date,
            "source":source,
            "source_link" : sourceLink,
            "text": article_content,
            "symbol": symbol,
            "category": category
            },
        
    )
    docs.append(load_docs)
    uuids = [str(uuid4()) for _ in range(len(docs))]
    vector_store.add_documents(documents=docs, ids=uuids, show_progress=True)
def get_vector_store():
    return vector_store