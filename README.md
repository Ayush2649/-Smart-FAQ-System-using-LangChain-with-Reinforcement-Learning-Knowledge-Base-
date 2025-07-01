# 🤖 Smart FAQ System using LangGraph

A context-aware, LLM-powered FAQ assistant built using [LangGraph](https://www.langgraph.dev/), LangChain, and sentence-transformer embeddings. The system retrieves answers from a knowledge base and dynamically routes user queries based on confidence scores.

---

## 🚀 Features

- ✅ Smart question answering over a CSV FAQ file
- ✅ Semantic search with HuggingFace embeddings
- ✅ LangGraph-powered flow control based on confidence
- ✅ Follow-up prompt if LLM is unsure
- ✅ REPL-style CLI for continuous Q&A
- ✅ Modular code: retrieval, graph, and state are cleanly separated

---

## 📁 Project Structure

```bash
smart-faq-system/
├── data/
│   └── faq_data.csv              # Your FAQ dataset
├── vectorstore/
│   └── faiss_index/              # Saved FAISS index (generated once)
├── embed_store.py               # One-time script to embed and store FAQ data
├── retriever.py                 # Loads vectorstore for runtime retrieval
├── nodes.py                     # LangGraph nodes: retrieval, logic, answer, etc.
├── state.py                     # FAQState definition for typed LangGraph state
├── langgraph_faq.py             # Graph creation and routing logic
├── main.py                      # CLI loop: ask questions until "quit"
└── requirements.txt             # Python dependencies
````

---

## 🧠 How It Works

1. **Vector Embedding**
   Run `embed_store.py` once to convert your FAQ CSV into embeddings and save the vector index using FAISS.

2. **Graph Routing with LangGraph**
   LangGraph routes the user query based on the confidence of the retrieved answer:

   * If the score is high, return the answer
   * If the score is low, ask a follow-up question

3. **REPL Loop**
   Run `main.py` and interact with the assistant in a loop.

---

## 📦 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/ceodaniyal/smart-faq-system.git
cd smart-faq-system
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your FAQ data

Place your `faq_data.csv` file in the `data/` directory. A sample is already included.

### 4. Generate embeddings (run once)

```bash
python embed_store.py
```

### 5. Start the Smart FAQ System

```bash
python main.py
```

---

## 📝 FAQ Data Format (`faq_data.csv`)

```csv
question,answer
What are your business hours?,Our business hours are 9 AM to 6 PM, Monday through Friday.
How can I reset my password?,Click "Forgot Password" on the login page and follow the instructions.
...
```

---

## 🔧 Tech Stack

* [LangGraph](https://www.langgraph.dev/)
* [LangChain](https://www.langchain.com/)
* [HuggingFace Embeddings](https://huggingface.co/sentence-transformers/all-mpnet-base-v2)
* [FAISS](https://github.com/facebookresearch/faiss)
* Python 3.9+

---

## ✨ Future Improvements

* [ ] Switch to Chroma or MongoDB vector store with scoring
* [ ] Add Streamlit or Gradio UI
* [ ] Live feedback + learning loop
* [ ] Web API with FastAPI or Flask

---

## 🧑‍💻 Author

Made with 💡 by [@ceodaniyal](https://github.com/ceodaniyal)

---

## 📄 License

MIT License
