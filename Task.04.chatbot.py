def chatbot():
    print("Chatbot: Hello! I am ready to assist you. (Type 'bye' to exit)")
    
    # Predefined rules
    responses = {
        "hello": "Hi there! How can I help you today?",
        "how are you": "I am fine, thanks for asking! How about you?",
        "bye": "Goodbye! Have a great day!"
    }
    
    while True:
        user_input = input("You: ").lower().strip()
        
        # Logic check
        if user_input in responses:
            print(f"Chatbot: {responses[user_input]}")
            if user_input == "bye":
                break
        else:
            print("Chatbot: Sorry, I am a simple bot and didn't understand that.")

if __name__ == "__main__":
    chatbot()
  
