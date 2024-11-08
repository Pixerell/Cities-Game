import telebot
TOKEN = '7827971601:AAF9prZTfj609NI2PJUBOXtLgihUUK0w6AI'


bot=telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "GAME START!")


@bot.message_handler(commands=['stop'])
def stop(message):
    bot.send_message(message.chat.id, "GAME DEAD!")


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,
    "List of following commands:\n/start - start the game \n /stop - stop the game \n/help - list of commands (and help)")


bot.polling(none_stop=True, interval=0)

#test