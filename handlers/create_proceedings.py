from telegram import Update
from telegram.ext import ContextTypes,CallbackContext,ConversationHandler
from datetime import date

GET_PROCEEDINGS, GET_LINK = range(2)

async def create_proceeding(update: Update, context: CallbackContext):
  await update.message.reply_text(
    "Hi! I will be helping you create the proceedings for today's meeting.\n"
    "Please provide the proceedings in a sequence from top to bottom as the below example shown."
  )
  await update.message.reply_text(
    "ID verify & settings\n"
    "Hosting\n"
    "Meeting Link Sharing\n"
    "Joining process\n"
    "..."
    )
  return GET_PROCEEDINGS

async def get_proceeding(update: Update, context: CallbackContext):
  context.user_data['proceeding'] = update.message.text
  await update.message.reply_text(
    "Great! \n Now provide the meeting link for today!"
  )
  return GET_LINK

async def get_link(update: Update, context: CallbackContext):
  context.user_data['link']= update.message.text
  p = context.user_data['proceeding']
  l = context.user_data['link']
  s=p.count('\n') +1
  d = date.today()

  text = f"""            ⭐🌍 * l LOVE ATOMY INDIA🌍⭐
  📝শিক্ষাৰ অবিহনে সফলতা অসম্ভৱ,গতিকে শিকো আহক✍✍✍🧭🧭🧭🧭🧭🧭🧭🧭
  🎯🎯🎯🎯🎯🎯🎯🎯🎯

  🙏🙏🙏নমস্কাৰ*মই শ্ৰীমতী কেচন দত্ত 
  শদিয়া*ৰ পৰা সকলোকে আজিৰ দিনৰ প্ৰশিক্ষণলৈ আদৰণি জনাইছো*🙏🙏🙏👏👏👏🌹🌹🌹

  সকলো সদস্য সদস্যাক  হাতত বহী  কলম লৈ
  অনলাইন প্ৰশিক্ষণত উপস্থিত*থাকিবলৈ বিনম্ৰতাৰে*অনুৰোধ জনালোঁ।🙏🙏🙏

  আজি প্ৰশিক্ষণত আলোচোনা *হবলগীয়া বিষয় সমূহ হল **👇👇👇👇👇
  {p}
  👇👇👇
  এই {s} টা কাৰ্য্যসূচী আগবঢ়াই নিব আমাৰ মাজৰ এজন গ্ৰেট এক্টিভ  লিডাৰ শ্ৰী দীপক টেৰণ ছাৰে (*ৱেষ্ট কাৰ্বি আংলং*ৰ পৰা )🗣🗣🗣🎤🎤🎤📣📣📣

  আপুনি এই {s} টা কাৰ্য্যসূচী শিকিব আৰু বুজিব পাৰিব বহি কলম হাতত লৈ বহিব
  🙏🧕👰👸🕵👮👷👳🧑‍🍳🧑‍🦳🧑‍🦰🧔🧑🤝👍

  👇👇👇👇👇👇👇👇

  {l}
 
  👆👆👆👆👆👆👆👆
  ওপৰৰ লিংকত ক্লিক কৰি মিটিংত প্ৰৱেশ কৰিব  পাৰিব

  সময় -দুপৰীয়া 12 বজাত
  তাৰিখ {d}
  ধন্যবাদ🙏🙏"""

  await update.message.reply_text(text)

async def cancel(update: Update, context: CallbackContext):
  await update.message.reply_text(
    "Task Cancelled!"
  )
  return ConversationHandler.END