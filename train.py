from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

def train_bot():
    chatbot = ChatBot("CleverBot")
    trainer = ChatterBotCorpusTrainer(chatbot)
    
    # Training with built-in English corpus data
    trainer.train("chatterbot.corpus.english")

if __name__ == "__main__":
    train_bot()
