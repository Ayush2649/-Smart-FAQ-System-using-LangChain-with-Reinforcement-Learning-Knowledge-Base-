import textwrap
import re
from langgraph_faq import graph
from rich.console import Console
from rich.markdown import Markdown

console = Console()

def clean_answer(answer: str) -> str:
    # Remove excess newlines
    answer = re.sub(r"\n{3,}", "\n\n", answer.strip())

    # Convert HTML entities if needed
    answer = answer.replace("&gt;", ">").replace("&lt;", "<").replace("&amp;", "&")

    return answer

def main():
    console.print("[bold blue]📘 Smart FAQ System (Type 'quit' to exit)[/bold blue]\n")

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "quit":
            console.print("[bold red]👋 Goodbye![/bold red]")
            break

        initial_state = {"question": user_input}
        result = graph.invoke(initial_state)

        if "answer" in result:
            answer = clean_answer(result["answer"])
            console.print("\n🤖 [bold green]Answer:[/bold green]\n")
            console.print(Markdown(answer))   # renders markdown beautifully in terminal
            console.print("\n" + "-" * 80)

        elif "followup" in result:
            console.print("🤖 [yellow]Follow-up:[/yellow]", result["followup"])
        else:
            console.print("🤖 [red]Sorry, I couldn't understand your question.[/red]")

if __name__ == "__main__":
    main()
