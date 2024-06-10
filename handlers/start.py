from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  user_name = update.effective_user.first_name
  this_name = 'Atomy Generative Bot'
  msg_1 = f"Welcome to {this_name}, {user_name}!"
  msg_2 = f"Here you can get all kinds of template for creating the following:"
  opt_1 = "Meeting links"
  opt_2 = "Meeting Members List & much more..."

  await update.message.reply_text(msg_1)
  await update.message.reply_text(msg_2)
  await update.message.reply_text(opt_1)
  await update.message.reply_text(opt_2)