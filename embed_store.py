import csv, sys
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain.text_splitter import CharacterTextSplitter

csv.field_size_limit(sys.maxsize)

# File containing scraped data
INPUT_FILE = "stackoverflow_faq.csv"

docs = []
with open(INPUT_FILE, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        question = row.get("question", "").strip()
        answer = row.get("answer", "").strip()
        topic = row.get("topic", "").strip()   # keep track of which topic (RL, SL, etc.)
        if question and answer:
            content = f"Q: {question}\nA: {answer}"
            docs.append(
                Document(
                    page_content=content,
                    metadata={"question": question, "answer": answer, "topic": topic}
                )
            )

# Split into chunks
splitter = CharacterTextSplitter(chunk_size=4000, chunk_overlap=200)

# Create embeddings
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
vectorstore = FAISS.from_documents(chunks, embedding)

# Save index
vectorstore.save_local("vectorstore/faiss_index")

print(f"✅ Vectorstore created successfully with {len(chunks)} chunks from {INPUT_FILE}")