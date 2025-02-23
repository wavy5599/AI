import openai
import os
from dotenv import load_dotenv

# Load environment variables from.env file

load_dotenv()

# Add your code here to initialize your main function and GPT-4o chatbot

# Initialize OpenAI client with your API key
client = openai.Client(api_key=os.getenv('The_Claw'))

# Function to interact with GPT-4o
def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
        
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    print("Chat with GPT-4o! Type 'quit', 'exit', or 'bye' to stop.")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Goodbye!")
            break
        
        response = chat_with_gpt(user_input)
        print("\nAi: ", response)


        
    

