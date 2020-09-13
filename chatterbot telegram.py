# -*- coding: utf-8 -*-
import telepot
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot("Python")
#bot.set_trainer(ListTrainer)

trainer = ListTrainer(bot)

f = open("treinamento.txt", "r").readlines()
trainer.train(f)

## API KEY ADD HERE
api = "API_KEY"

# Function to search the text received, the return message below
def receber(msg):
    texto = (msg['text'])
    _id = msg['from']['id']
    nome = msg['from']['first_name']
    if "Olá" in texto:
        tele.sendMessage(_id,"Olá, "+str(nome))
    elif "Oi" in texto:
        tele.sendMessage(_id,"Ooi, "+str(nome))
    elif "Eae" in texto:
        tele.sendMessage(_id,"Eaae, "+str(nome))
    elif "/start" in texto:
        tele.sendMessage(_id,"Seu novo Bot-Python esta a suas ordens senhor(a), "+str(nome))
    else:
        tele.sendMessage(_id,str(bot.get_response(texto)))


tele = telepot.Bot(api)
tele.message_loop(receber)

# Set the while to true so that the bot is not interrupted
while True:
    pass
