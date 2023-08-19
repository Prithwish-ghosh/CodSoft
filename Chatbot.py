def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        response = "Hello! How can I help you?"
    elif "how are you" in user_input:
        response = "I'm just a chatbot, but I'm here to assist you!"
    elif "weather" in user_input:
        response = "I'm sorry, I am not connected to real-time data. You can check a weather website for accurate information."
    elif "bye" in user_input or "goodbye" in user_input:
        response = "Goodbye! Feel free to come back anytime."
    else:
        response = "I'm not sure how to respond to that."

    return response

print("Chatbot: Hi there! How can I assist you today?")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
