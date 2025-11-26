print("🤖 Chatbot: Hello! I am your simple chatbot. Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    # Exit condition
    if user_input in ["bye", "exit", "quit"]:
        print("🤖 Chatbot: Goodbye! Have a great day!")
        break

    # Responses using IF-ELSE
    if "hello" in user_input or "hi" in user_input:
        print("🤖 Chatbot: Hello! How can I help you today?")

    elif "how are you" in user_input:
        print("🤖 Chatbot: I'm doing great! Thanks for asking 😊")

    elif "name" in user_input:
        print("🤖 Chatbot: I am a simple rule-based chatbot created in Python!")

    elif "help" in user_input:
        print("🤖 Chatbot: Sure! Ask me anything about Python, projects, or general doubts.")

    elif "python" in user_input:
        print("🤖 Chatbot: Python is a powerful programming language used for AI, web, and more!")

    elif "what can you do" in user_input:
        print("🤖 Chatbot: I can answer simple questions using if-else rules!")

    else:
        print("🤖 Chatbot: Sorry, I didn’t understand that. Try asking something else!")