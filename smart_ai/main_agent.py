# main_agent.py
import vertexai
from vertexai.preview import reasoning_engines
from config import PROJECT_ID, LOCATION
import tools # Import our tools file

def main():
    """Initializes and runs the smart research bot."""
    # 1. Initialize Vertex AI
    vertexai.init(project=PROJECT_ID, location=LOCATION)

    # 2. Create the agent
    # The agent will automatically discover the tools in the 'tools' module.
    # The system instruction guides the agent on how to behave.
    agent = reasoning_engines.ReasoningEngine.create(
        reasoning_engines.LangchainAgent(
            model="gemini-2.0-flash-lite",
            tools=[tools.search_the_web], # Pass the function directly
            model_kwargs={"temperature": 0.0}
        ),
        requirements=[],
    )

    print("🚀 AI Web Explorer is ready. Ask me anything!")
    print("Type 'exit' to end the conversation.")

    # 3. Main interaction loop
    while True:
        user_question = input("\nYour question: ")
        if user_question.lower() == 'exit':
            print("Goodbye!")
            break

        # 4. Query the agent
        response = agent.query(input=user_question)

        # The final answer is in the 'output' key
        print(f"\n✅ AI Answer:\n{response['output']}")

if __name__ == "__main__":
    main()
