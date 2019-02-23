from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

tokenpath = "./token"
token = open(tokenpath, "r").read()

valid_types = [
    "application/pdf",
    "image/png",
    "image/jpg",
    "image/bmp",
    "text/plain"
]

def get_lp_command(args):
    # Double or single sided
    duplex = "-o sides=two-sided-long-edge"
    if "simple" in args or "single" in args:
            duplex = "-o sides=one-sided"
    # Number of copies
    copies = "-n 1"
    for arg in args:
        if arg.isdigit():
            copies = "-n %s" % arg
    # Generate the lp command
    command = "lp %s %s" % (copies, duplex)
    return command



def request_print(bot, update, args):
    # Get the message in which the file was sent
    file_msg = update.message.reply_to_message
    # Check if we can print the document
    file_type = file_msg.document.mime_type
    if file_type in valid_types:
        # Get the file id, name and link
        file_id = file_msg.document.file_id
        file_name = file_msg.document.file_name
        file_link = bot.get_file(file_id)
        # Download the file
        file_link.download("to_print")
        # Generate the printing command
        command = get_lp_command(args)
        # Print the user
        reply = "Printing file %s" % (file_name)
        update.message.reply_text(reply, quote=True)
        os.system("%s ./to_print" % command)

def recognize_file(bot, update):
    # Notify the user that we can print this file
    file_type = update.message.document.mime_type
    if file_type in valid_types:
        reply = "If you want me to print this file, reply to it with the /print command"
        update.message.reply_text(reply, quote=True)

# Start the bot
updater = Updater(token)

# Handler to notify the user we can print their document
updater.dispatcher.add_handler(MessageHandler(Filters.document, recognize_file))
# Handler to execute a print command
updater.dispatcher.add_handler(CommandHandler('print', request_print, pass_args=True))

updater.start_polling()
updater.idle()
