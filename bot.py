import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)


def hello(update, context):
    update.message.reply_text("Hello {}".format(update.message.from_user.first_name))


def echo(update, context):
    update.message.reply_text(update.message.text)


def start(update, context):
    update.message.reply_text("Hi!")


def run_bot(token):
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('hello', hello))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    logger.info("Bot started")
    updater.idle()
