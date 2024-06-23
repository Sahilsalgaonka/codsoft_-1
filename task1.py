def chatbot_response(user_input):
    
    if "hello" in user_input.lower():
        return "Hello! How can I help you today?"
    elif "how are you" in user_input.lower():
        return "I'm a chatbot, so I don't have feelings, but I'm here to help you!"
    elif "bye" in user_input.lower():
        return "Goodbye! Have a great day!"
    elif "name" in user_input.lower():
        return "I am a simple chatbot created to assist you."
    elif "help" in user_input.lower():
        return "Sure, I'm here to help! What do you need assistance with?"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"


def main():
    print("Chatbot: Hi there! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
