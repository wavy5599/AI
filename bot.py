import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with your API key
client = openai.OpenAI(api_key=os.getenv('key'))  

# Function to interact with GPT-4o
def chat_with_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        if response.choices and len(response.choices) > 0:
            return response.choices[0].message.content.strip()
        else:
            return "Error: No response from GPT-4o."
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("Chat with GPT-4o! Type 'quit', 'exit', or 'bye' to stop.")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Goodbye!")
            break
        
        response = chat_with_gpt(user_input)
        print("\nGPT 4o: ", response)