# Simple Basic Chatbot
def chatbot_response(user_input):
    user_input = user_input.lower().strip() 
    if user_input in ["hello", "hi", "hey"]:
        return "Hi!"
    elif user_input in ["how are you", "how are you doing"]:
        return "I'm fine, thanks!"
    elif user_input in ["bye", "goodbye", "see you"]:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."
def run_chatbot():
    print("Welcome to the Simple Chatbot! (Type 'bye' to exit)\n")
    while True:
        user_message = input("You: ")
        reply = chatbot_response(user_message)
        print("Chatbot:", reply)
        if user_message.lower().strip() in ["bye", "goodbye", "see you"]:
            break

if __name__ == "__main__":
    run_chatbot()