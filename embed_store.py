import csv, sys
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain.text_splitter import CharacterTextSplitter

csv.field_size_limit(sys.maxsize)

docs = []
with open("data/faq_data.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        question = row.get("question", "").strip()
        answer = row.get("answer", "").strip()
        if question and answer:
            content = f"Q: {question}\nA: {answer}"
            docs.append(Document(page_content=content, metadata={"question": question, "answer": answer}))

# Split and embed
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_documents(docs)

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
vectorstore = FAISS.from_documents(chunks, embedding)

# Save to disk
vectorstore.save_local("vectorstore/faiss_index")
