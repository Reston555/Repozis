import telebot
from config import API_URL
bot= telebot.TeleBot(API_URL)
@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id,'555')
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,'Доступные команды:\n" "/start — запустить бота и приветствие\n" "/help — показать это сообщение\n" "/about — информация о боте')
@bot.message_handler(commands = ['about'])
def about(message):
    bot.send_message(message.chat.id,'Я простой телеграмм бот. Я ничего не умею. Но это пока что!')
bot.polling()