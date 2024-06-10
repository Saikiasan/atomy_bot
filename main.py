import logging 
from telegram.ext import CommandHandler, MessageHandler, filters, ConversationHandler
from bot import create_bot

from handlers.start import start
from handlers.create_meeting_temp import create_meeting_txt, get_name, get_city, cancel, GET_CITY, GET_NAME
from handlers.create_proceedings import *


def main() -> None:
  token = '7461461454:AAHjjmFgNhuXw43XEgGx8gEOxLF3zYM_pF4'

  app = create_bot(token)

  app.add_handler(CommandHandler('start', start))
  # app.add_handler(CommandHandler('help', help))
  # app.add_handler(MessageHandler(filters.TEXT, ))

  conversation_handler = ConversationHandler(
    entry_points=[CommandHandler('gen', create_meeting_txt)],
    states={
      GET_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
      GET_CITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_city)]
    },
    fallbacks=[CommandHandler('cancel', cancel)],
  )

  app.add_handler(conversation_handler)

  pro_con = ConversationHandler(
    entry_points=[CommandHandler('mg1', create_proceeding)],
    states={
      GET_PROCEEDINGS: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_proceeding)],
      GET_LINK: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_link)]
    },
    fallbacks=[CommandHandler('cancel', cancel)]
  )
  app.add_handler(pro_con)

  app.run_polling()

if __name__ == '__main__':
  main()