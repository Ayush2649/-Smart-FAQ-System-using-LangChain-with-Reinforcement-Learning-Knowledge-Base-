from langgraph_faq import graph

def main():
    print("Hello from smart-faq-langgraph!")
    initial_state = {"question": "How can I reset my password?"}
    result = graph.invoke(initial_state)

    if "answer" in result:
        print("Answer:", result["answer"])
    elif "followup" in result:
        print("Follow-up:", result["followup"])
    else:
        print("No valid response returned.")


if __name__ == "__main__":
    main()
