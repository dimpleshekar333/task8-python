# Simple Rule-Based Chatbot (Python)

This project is a **simple rule-based chatbot** built using Python.\
It uses **if-elif-else conditions** to respond to basic user inputs.

------------------------------------------------------------------------

## 📌 Features

-   Greets the user\
-   Responds to common queries\
-   Talks about its name and Python\
-   Says goodbye when the user types **bye**, **exit**, or **quit**

------------------------------------------------------------------------

## 🧠 How It Works

The chatbot continuously asks for user input inside a `while True`
loop.\
Based on keywords inside the user's message, it chooses a response.

If the user types: - **hello / hi** → greeting\
- **how are you** → well-being message\
- **name** → chatbot introduces itself\
- **help** → offers assistance\
- **python** → gives info about Python\
- **what can you do** → describes its ability\
- Anything else → default fallback reply

------------------------------------------------------------------------

## ▶️ How to Run the Program

1.  Install Python (if not installed)

2.  Save the chatbot code in a file:

        chatbot.py

3.  Run it in terminal:

        python chatbot.py

------------------------------------------------------------------------

## 📝 Chatbot Code

    print("🤖 Chatbot: Hello! I am your simple chatbot. Type 'bye' to exit.
    ")

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

------------------------------------------------------------------------

## ✔️ Output Example

    🤖 Chatbot: Hello! I am your simple chatbot. Type 'bye' to exit.

    You: hi
    🤖 Chatbot: Hello! How can I help you today?

    You: what can you do
    🤖 Chatbot: I can answer simple questions using if-else rules!

    You: bye
    🤖 Chatbot: Goodbye! Have a great day!

------------------------------------------------------------------------

## 📂 File Information

-   **File Name:** README.md\
-   **Use Case:** Submission for lab/project report

------------------------------------------------------------------------

Made with ❤️ using Python.
