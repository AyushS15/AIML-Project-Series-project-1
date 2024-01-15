class SimpleChatbot:
    def __init__(self):
        self.context = {}

    def greet(self):
        return "Hello! I'm your friendly chatbot. How can I assist you today?"

    def respond_to_basic_questions(self, user_input):
        basic_questions = {
            "How are you?": "I'm doing well, thank you! How about you?",
            "What is your name?": "I'm just a chatbot, so I don't have a name.",
            "Who created you?": "I was created by a developer.",
            "What do you do?": "I'm here to chat and assist you with any questions.",
            "How can I help you?": "You can ask me anything, and I'll do my best to assist you!"
        }

        for question, response in basic_questions.items():
            if question.lower() in user_input.lower():
                return response

        return 'Can you please clarify your question again?'

    def farewell(self):
        return "Goodbye! If you have more questions, feel free to ask anytime."

    def ask_user_questions(self):
        questions = ["What is your favorite color?", "Tell me about your day.", "Do you have any hobbies?"]
        user_responses = []

        for question in questions:
            user_response = input(question + " ")
            user_responses.append(user_response)

        return user_responses

    def handle_user_input(self, user_input):
        response = self.respond_to_basic_questions(user_input)

        if response:
            return response

        if "ask" in user_input.lower():
            user_responses = self.ask_user_questions()
            self.context["user_responses"] = user_responses
            return "Thanks for sharing! How can I assist you further?"

        return "I'm sorry, I didn't understand that. Can you please rephrase or ask another question?"

# Main interaction loop
def chat():
    chatbot = SimpleChatbot()
    print(chatbot.greet())

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print(chatbot.farewell())
            break

        response = chatbot.handle_user_input(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat()
