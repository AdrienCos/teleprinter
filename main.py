from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

tokenpath = "./token"
token = open(tokenpath, "r").read()
print(token)


def hello(bot, update):
    update.message.reply_text('Hello {}'.format(
        update.message.from_user.first_name))


def request_print(bot, update):
    file_id = update.message.document.file_id
    file_name = update.message.document.file_name
    file_link = bot.get_file(file_id)
    file_link.download(file_name)
    print("Downloaded file %s" % file_name)
    print("Printing file %s" % file_name)
    os.system("lpr ./%s" % file_name)


updater = Updater(token)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(MessageHandler(Filters.document, request_print))

updater.start_polling()
updater.idle()
