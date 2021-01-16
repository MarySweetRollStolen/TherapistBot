import telebot
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

bot = telebot.TeleBot(config["bot"]["token"])

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет, " + message.from_user.first_name)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
