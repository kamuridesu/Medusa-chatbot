from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from messages_processor import MessagePreProcessor


class Bot:
    def __init__(self):
        self.bot = ChatBot('Bot')
        self.trainer = ChatterBotCorpusTrainer(self.bot)
        self.trainer.train('chatterbot.corpus.portuguese')
    
    def train(self, messages: list):
        self.trainer = ListTrainer(self.bot)
        self.trainer.train(messages)
    
    def get_response(self, message: str) -> str:
        res = {}
        res['status'] = 'OK'
        res['response'] = str(self.bot.get_response(message))
        return res
    


# bot = Bot()
# bot.train(MessagePreProcessor("messages.log").pre_processed_messages)
# while True:
#     print("bot:", bot.get_response(input("Você: ")))