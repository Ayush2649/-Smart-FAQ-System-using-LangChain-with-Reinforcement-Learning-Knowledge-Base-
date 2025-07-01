from retriever import retriever

# Define your custom nodes
def retrieve_answer(state):
    query = state["question"]
    docs = retriever.get_relevant_documents(query)
    return {
        **state,
        "retrieved_docs": docs
    }

def is_confident_enough(state):
    # Assume the retriever gives score in metadata
    doc = state["retrieved_docs"][0]
    score = doc.metadata.get("score", 0.0)
    
    return {
        **state,
        "condition": "no" if score < 0 else "yes"
    }


def generate_answer(state):
    answer = state["retrieved_docs"][0].page_content
    return {
        **state,
        "answer": answer
    }


def ask_followup_question(state):
    return {
        **state,
        "followup": "Can you please clarify your question?"
    }
