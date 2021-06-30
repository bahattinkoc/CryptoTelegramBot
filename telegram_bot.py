import requests
import urllib.request

tg_token = '1775080944:AAHmCXc-Pnr5FfX4r7z6OgywvwdKisem5bQ'
chat_id = '-1001462355459'
# bot = telebot.TeleBot(tg_token)

# chat_id öğrenmek için siteye istek atılır. Dönen JSON parse edilip id çekilir. Böylece işlem otomatik hale gelir.

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        urllib.request.urlcleanup()
        return True
    except:
        return False


# def SendMessage(text):
#     if connect():
#         bot.send_message(chat_id, text, parse_mode='Markdown', disable_web_page_preview=True)
#     else:
#         print("İnternet bağlantısı yok!")
#

def SendMessage(text):
    if connect():
        send_text = 'https://api.telegram.org/bot' + tg_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&disable_web_page_preview=True&text=' + text
        requests.get(send_text)
    else:
        print("İnternet bağlantısı yok!")
