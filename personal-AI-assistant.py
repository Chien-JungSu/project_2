import os
import google.generativeai as genai

def setup_ai_brain():
    """
    Configures the Gemini API key from environment variables.
    Exits the program if the key is not found.
    """
    try:
        # Get the API key from the environment variable
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            print("❌ ERROR: GEMINI_API_KEY environment variable not found.")
            print("Please set the GEMINI_API_KEY environment variable.")
            exit()
        
        genai.configure(api_key=api_key)
        print("✅ AI Brain configured successfully.")
    except Exception as e:
        print(f"❌ An error occurred during configuration: {e}")
        exit()

def ask_ai(question):
    """
    Sends a question to the Gemini model and returns the response.
    """
    try:
        # Initialize the model
        model = genai.GenerativeModel('gemini-2.0-flash-lite')
        
        # Send the prompt and get the response
        response = model.generate_content(question)
        
        return response.text
    except Exception as e:
        return f"❌ An error occurred while communicating with the AI: {e}"

def main():
    """
    Main function to run the AI chat loop.
    """
    setup_ai_brain()
    print("\n--- AI Brain Initialized ---")
    print("Ask a question, or type 'exit' to quit.")
    
    while True:
        user_question = input("\nYour Question: ")
        
        if user_question.lower() == 'exit':
            print("👋 Goodbye!")
            break
            
        if not user_question:
            print("Please enter a question.")
            continue
            
        print("\n🧠 Thinking...")
        
        # Get the answer from the AI
        ai_response = ask_ai(user_question)
        
        print("\n🤖 AI Response:")
        print(ai_response)

if __name__ == "__main__":
    main()
