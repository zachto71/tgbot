import asyncio

from ai_talks import ai_response

from utils import *

from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot(BOT_TOKEN)


@bot.message_handler(commands=["help", "start"])
async def send_welcome(message):
    await bot.reply_to(message, get_welcome_text())


@bot.message_handler(func=lambda message: True and message.text.startswith("sub news"))    # FIXME: КОСТЫЛЬ ЕБУЧИЙ
async def ai_news_teller(message):
    await bot.reply_to(message, ai_response(message))


@bot.message_handler(func=lambda message: True)
async def remember_messages(message):
    await message_collector(message)

asyncio.run(bot.polling())
