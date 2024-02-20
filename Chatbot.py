import openai

# Set up your OpenAI API key
openai.api_key = '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'

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  
        prompt=prompt,
        temperature=0.7,  
        max_tokens=150  
    )
    return response.choices[0].text.strip()

# Main loop for interacting with the chatbot
def main():
    print("Welcome to the ChatGPT bot! Type 'quit' to exit.")
    user_input = input("You: ")

    while user_input.lower() != 'quit':
        # Interact with GPT based on user input
        response = chat_with_gpt(user_input)
        print("ChatGPT:", response)

        # Get the next user input
        user_input = input("You: ")

    print("Goodbye!")

if __name__ == "__main__":
    main()
