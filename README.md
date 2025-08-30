# 📘 Smart FAQ System (with Reinforcement Learning Knowledge Base)

This project is a Smart FAQ Retrieval System powered by LangChain, FAISS, and HuggingFace embeddings.

It allows you to:
- Ask questions in natural language
- Retrieve relevant answers from a FAQ dataset (CSV)
- Supports FAQs on Reinforcement Learning (scraped from StackOverflow)
- Nicely formatted console output (with Markdown support)

---

## 🚀 Features

- ✅ Vector similarity search using FAISS 🔍
- ✅ HuggingFace all-mpnet-base-v2 embeddings for high-quality semantic matching 🤖
- ✅ Extendable to any custom FAQ dataset (just replace faq_data.csv) 📂
- ✅ Interactive CLI chatbot that responds until you type quit 💬
- ✅ Preserves Markdown/Code/Tables in answers for better readability 📑

---

## 📸 Demo Screenshots

### 🔹The Setup
![alt text](<Screenshot (545).png>)

### 🔹 Start Screen
![alt text](<Screenshot 2025-08-30 164951.png>)

### 🔹 Asking a Question
![alt text](<Screenshot 2025-08-30 165112.png>)

### 🔹 Answer Formatting
![alt text](<Screenshot 2025-08-30 165125.png>)

---

## 📁 Project Structure

```bash
smart-faq-system/
├── data/
│   └── faq_data.csv              # FAQ dataset (Reinforcement Learning or Business FAQs)
├── vectorstore/                  # Auto-generated FAISS index (created on first run)
├── screenshots/                  # Store your demo images here
├── embed_store.py                # Script to embed CSV and create vectorstore
├── retriever.py                  # Loads FAISS and retrieves relevant answers
├── nodes.py                      # LangGraph nodes (retrieval, answer, etc.)
├── state.py                      # Defines FAQState for LangGraph
├── langgraph_faq.py              # Graph creation and routing logic
├── main.py                       # CLI interface to interact with the system
└── requirements.txt              # Python dependencies
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

### 1️⃣ Clone the repo

```bash
git clone https://github.com/ceodaniyal/smart-faq-system.git
cd smart-faq-system
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Prepare Your Data

- Default file: data/faq_data.csv

- Format:
   question,answer
   What is Q-learning?,Q-learning is an off-policy RL algorithm...
   What is SARSA?,SARSA is an on-policy RL algorithm...

- You can replace this CSV with your own FAQs.

### 4️⃣ Build Vectorstore

### 4. Generate embeddings (run once)

```bash
python embed_store.py
```

### 5. Start the Smart FAQ System

```bash
python main.py
```

---

## 🎮 Example Usage

```csv
📘 Smart FAQ System (Type 'quit' to exit)

You: What is the difference between Q-learning and SARSA?

🤖 Answer:

**Q-learning vs SARSA**

|             | SARSA | Q-learning |
|-------------|-------|------------|
| Choosing A' |  π    |    π       |
| Updating Q  |  π    |    μ       |

- **Q-learning** → off-policy (evaluates μ while following π)  
- **SARSA** → on-policy (follows π consistently)  

...
--------------------------------------------------------------------------------
```

---

## 🔧 Tech Stack

* [LangGraph](https://www.langgraph.dev/)
* [LangChain](https://www.langchain.com/)
* [HuggingFace Embeddings](https://huggingface.co/sentence-transformers/all-mpnet-base-v2)
* [FAISS](https://github.com/facebookresearch/faiss)
* Python 3.9+

---

## 📌 Notes

- If you update your dataset, delete the vectorstore/ folder and re-run:

```bash
python embed_store.py
```

- For better formatting, answers are rendered with Markdown in the console.

## 🤝 Contributing

Pull requests are welcome! If you have more FAQ datasets (e.g., Machine Learning, NLP, Cybersecurity), feel free to add them.

## ✨ Future Improvements

* [ ] Switch to Chroma or MongoDB vector store with scoring
* [ ] Add Streamlit or Gradio UI
* [ ] Live feedback + learning loop
* [ ] Web API with FastAPI or Flask

---

## 📄 License

MIT License © 2025 Ayush Sahu(https://github.com/Ayush2649)
