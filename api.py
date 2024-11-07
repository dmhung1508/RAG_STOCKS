from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from fastapi.responses import JSONResponse
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
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

app = FastAPI(
    title="RAG Stock News API",
    description="API for retrieving stock news",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return {"message": "Hello World"}
class RetrievalRequest(BaseModel):
    query: str
    top_k: int
    filter: dict

@app.post("/retrieval")
async def retrieval(request: RetrievalRequest):
    """
    Lọc bài viết dựa trên metadata, có thể không cần đủ các trường. 
    Người dùng có thể chọn một hoặc nhiều trường dưới đây để lọc:

    - **date**: Ngày đăng bài viết (định dạng YYYY-MM-DD)
    - **source**: Tên nguồn cung cấp bài viết (ví dụ: tên báo)
    - **source_link**: Đường dẫn đến bài viết gốc
    - **text**: Nội dung bài viết hoặc từ khóa liên quan để tìm kiếm

    Nếu không cung cấp trường nào, kết quả sẽ trả về tất cả bài viết.

    Example:
    ```json
    {
        "query": "Tin tức về doanh nghiệp",
        "top_k": 5,
        "filter": {
            "date": "2024-10-29",
            "source": "stockbiz.vn",
            "source_link": "https://stockbiz.vn/tin-tuc/co-hoi-lon-cuoi-nam-2024-10-nam-co-1-tren-thi-truong-chung-khoan-viet-nam/28930437",
        }
    }
    ```
    """
    results = vector_store.similarity_search(
        request.query,
        k=request.top_k,
        filter=request.filter
    )
    response = [
        {"page_content": res.page_content, "metadata": res.metadata}
        for res in results
    ]
    return JSONResponse(content=response)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8504)