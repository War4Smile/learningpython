from telegram.ext import Updater, CommandHandler

def start_bot(bot, Updater):
	print("Hello")

def main():
	updtr = Updater ("296557628:AAEE_tE9q2xCh5kWhc8unKBEwkA6JEj_9K8")

	updtr.dispatcher.add_handler(CommandHandler("start", start_bot))

	updtr.start_polling()
	updtr.idle()

if __name__ == "__main__":
	main()