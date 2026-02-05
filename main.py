import asyncio

import os

from dotenv import load_dotenv

from ai_talks import ai_response

from utils import commands_checker

from telebot.async_telebot import AsyncTeleBot

load_dotenv()

bot = AsyncTeleBot(os.getenv("BOT_TOKEN"))


@bot.message_handler(commands=["help", "start"])
async def send_welcome(message):
    text = """Очень полезных новостей бот.
Для просмотра новостей используйте "sub news". """
    await bot.reply_to(message, text)


@bot.message_handler(func=lambda message: True and message.text.startswith("sub news"))    # FIXME: КОСТЫЛЬ ЕБУЧИЙ
async def ai_news_teller(message):
    with open("data/"+str(message.chat.id)+".txt", "r") as sms:
        all_messages = sms.read()
        await bot.reply_to(message, ai_response(all_messages))


@bot.message_handler(func=lambda message: True)
async def remember_messages(message):
    if commands_checker(message) == 0:
        if message.chat.type == 'group':
            with open("data/"+str(message.chat.id)+".txt", "a") as sms:
                sms.writelines(str(message.text)+" / "+"@"+message.from_user.username+"\n")


asyncio.run(bot.polling())
