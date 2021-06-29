import telebot

tg_token = '1775080944:AAHmCXc-Pnr5FfX4r7z6OgywvwdKisem5bQ'
bot = telebot.TeleBot(tg_token)

def SendMessage(text):
    bot.send_message(-1001462355459, text, parse_mode='Markdown', disable_web_page_preview=True)
