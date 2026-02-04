import asyncio

import os

from dotenv import load_dotenv

load_dotenv()

from ai_talks import ai_response

from telebot.async_telebot import AsyncTeleBot

with open("all_messages.txt", "r") as sms:
    all_messages = sms.read()

bot = AsyncTeleBot(os.getenv("BOT_TOKEN"))

@bot.message_handler(commands=["help", "start"])
async def send_welcome(message):
    text = "Пока что я просто эхобот"
    await bot.reply_to(message, text)


@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    if message.text[:2]!="ai" and message.text[:4]!="news":
        with open("all_messages.txt","a") as sms:
            sms.writelines(str(message.text)+"\n")
    if message.text[:2]=="ai":
        await bot.reply_to(message, message.text[2:])
    if message.text[:4]=="news":
        await bot.reply_to(message,ai_response(all_messages))

asyncio.run(bot.polling())
