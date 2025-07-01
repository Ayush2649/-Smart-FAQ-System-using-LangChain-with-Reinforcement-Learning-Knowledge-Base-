import csv
import sys
from langchain_core.documents import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

csv.field_size_limit(sys.maxsize)  # ✅ Fix the large field error

docs = []
with open("data/faq_data.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        question = row.get("question", "").strip()
        answer = row.get("answer", "").strip()
        if question and answer:
            content = f"Q: {question}\nA: {answer}"
            docs.append(Document(page_content=content, metadata={"source": row.get("source", "")}))


splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
vectorstore = FAISS.from_documents(chunks, embedding)
retriever = vectorstore.as_retriever(search_type="similarity", k=1)