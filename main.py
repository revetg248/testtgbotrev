from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url
def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
def main():
    updater = Updater('518538771:AAGJoGfapbrr4VA4NIAUztl3ToWNk-H5dpQ')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()