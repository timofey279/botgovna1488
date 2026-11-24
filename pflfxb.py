import telebot

token = "9084904992:AAHwYSFX_iAV1P40VcfZtJnLVAMPnk9on0w"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "З-з-здравтсвуйте, х-хозяин!!~~~")
    

@bot.message_handler(commands=["search"])
def send_welcome(message):
    bot.reply_to(message, "Введите номер команды:")


@bot.message_handler(func=lambda message:True)
def echo_call(message):
    match message.text.isdigit():
        case True:
            bot.reply_to(message, "*инфа про команду*")
        case False:
            bot.reply_to(message, "Ты еблан, это число должно быть")

if name == "main":
    bot.infinity_polling()