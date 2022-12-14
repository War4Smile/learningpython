import logging
import settings
# Подгружаем из репозитория ФУНКЦИИ (точка - разделитель папок, ипортируются используемые в проекте функции)
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
					level=logging.INFO,
					filename='bot.log'
					)

# Определяем команды для старта
def start_bot(update:Updater, context: CallbackContext):
#	print(update)
	logging.info(update)
	mytext = """Hello {}

	I have only /start comand: ;)""".format(update.message.chat.first_name)
	logging.info('User {} press /start'.format(update.message.chat.username))
	update.message.reply_text(mytext)

def chat(update:Updater, context: CallbackContext):
	text = update.message.text
	logging.info(text)

	update.message.reply_text(text)

def main():
	updtr = Updater (settings.TOKEN_TELEGRAM)

	updtr.dispatcher.add_handler(CommandHandler("start", start_bot))
	updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat))

	updtr.start_polling()
	updtr.idle()

if __name__ == "__main__":
	logging.info('Bot started!')
	main()