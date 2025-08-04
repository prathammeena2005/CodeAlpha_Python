def chatbot():
    responses = {"hello": "Hi!",
        "how are you": "I'm fine, thanks!",
        "bye": "Goodbye!",
        "what is your name": "I'm a simple chatbot."}

    print("Enter your response : ")
    while True:
        user = input("You: ").lower()
        if user == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot:", responses.get(user, "I didn't understand that."))

chatbot()
