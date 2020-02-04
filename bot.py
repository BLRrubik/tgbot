import config
import telebot
from telebot import apihelper
bot = telebot.TeleBot('1005124044:AAEJvfJHObTgm6b-JyWH3z2Czcdme94nqbE')
apihelper.proxy = {'https':'http://51.158.99.51:8811'}

@bot.message_handler(commands = ['start'])
def send_message(message):
    bot.send_message(message.chat.id,"hi")

#@bot.message_handler(content_types = ["text"])
#def repeat_message(message):
#	bot.send_message(message.chat.id, message.text)
@bot.message_handler(content_types = ['text'])
def send_message(message):
    if message.text.lower() == "саня пидр?":
        bot.send_message(message.chat.id, "yes")
    else:
        bot.send_message(message.chat.id, message.text)


bot.polling()

