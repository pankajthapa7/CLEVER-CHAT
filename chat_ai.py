from chatterbot import ChatBot

# Initialize the chatbot
chatbot = ChatBot("CleverBot")

def get_response(user_input):
    response = chatbot.get_response(user_input)
    return response
