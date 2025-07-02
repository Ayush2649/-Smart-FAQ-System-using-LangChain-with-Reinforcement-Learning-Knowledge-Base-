from retriever import retriever

# Define your custom nodes
def retrieve_answer(state):
    query = state["question"]
    docs_with_scores = retriever.similarity_search_with_score(query, k=1, fetch_k=3)

    docs = []
    for doc, score in docs_with_scores:
        doc.metadata["score"] = score
        docs.append(doc)

    return {**state, "retrieved_docs": docs}


def is_confident_enough(state):
    # Assume the retriever gives score in metadata
    docs = state["retrieved_docs"]
    print(f"Retrived docs:\n{docs}")
    doc = state["retrieved_docs"][0]
    score = doc.metadata.get("score", 100.0)
    
    return {**state,"condition": "yes" if score < 1 else "no"}  # lower = more similar


def generate_answer(state):
    answer = state["retrieved_docs"][0].page_content
    return {**state,"answer": answer}


def ask_followup_question(state):
    return {**state,"followup": "Can you please clarify your question?"}
