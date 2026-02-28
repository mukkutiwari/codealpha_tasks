# Simple Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi there! 😊"
    
    elif user_input == "how are you":
        return "I'm doing great, thanks for asking! How about you?"
    
    elif user_input == "bye":
        return "Goodbye! Have a wonderful day! 👋"
    
    else:
        return "Hmm... I don't understand that yet. Try saying hello, how are you, or bye."


def run_chatbot():
    print("🤖 ChatBot: Hello! I'm your friendly chatbot.")
    print("Type 'bye' anytime to exit.\n")

    while True:
        user = input("You: ")
        response = chatbot_response(user)
        print("ChatBot:", response)

        if user.lower() == "bye":
            break


# Start the chatbot
run_chatbot()