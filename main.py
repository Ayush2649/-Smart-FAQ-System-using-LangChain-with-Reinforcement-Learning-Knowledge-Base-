from langgraph_faq import graph

def main():
    print("📘 Smart FAQ System (Type 'quit' to exit)\n")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "quit":
            print("👋 Goodbye!")
            break

        initial_state = {"question": user_input}
        result = graph.invoke(initial_state)

        if "answer" in result:
            print("🤖 Answer:", result["answer"])
        elif "followup" in result:
            print("🤖 Follow-up:", result["followup"])
        else:
            print("🤖 Sorry, I couldn't understand your question.")

if __name__ == "__main__":
    main()
