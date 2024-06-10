from telegram import Update
from telegram.ext import ContextTypes,CallbackContext,ConversationHandler

GET_NAME,GET_CITY = range(2)

async def create_meeting_txt(update: Update, context: CallbackContext):
  await update.message.reply_text(
    "Hi! I will be helping you create a new meeting template.\n"
    "What is your name?"
  )
  return GET_NAME

async def get_name(update: Update, context: CallbackContext):
  context.user_data['name'] = update.message.text
  await update.message.reply_text(
    "Great! What is your city?"
  )
  return GET_CITY

async def get_city(update: Update, context: CallbackContext):
  context.user_data['city']= update.message.text
  name = context.user_data['name']
  city = context.user_data['city']

  text = f"Hello, your name is {name} and from {city}."
  await update.message.reply_text(text)

async def cancel(update: Update, context: CallbackContext):
  await update.message.reply_text(
    "Task Cancelled!"
  )
  return ConversationHandler.END