import os

from dotenv import load_dotenv

load_dotenv()

MY_COMMANDS = ["sub news","test command"]

AI_TOKEN = os.getenv("AI_TOKEN")

AI_MODEL = os.getenv("AI_MODEL")

AI_PROMPT = os.getenv("AI_PROMPT")

BOT_TOKEN = os.getenv("BOT_TOKEN")

def commands_checker(message):
    fg=0
    for commands_check in range(len(MY_COMMANDS)):
        if MY_COMMANDS[commands_check] in message.text:
            fg+=1
    return fg


def get_welcome_text():    # похуй клиркод в мейне + заранее легче редактировать здесь чем там
    return """Очень полезных новостей бот.
Для просмотра новостей используйте "sub news". """


async def message_collector(message):    # граббер сообщений
    if commands_checker(message)==0:
        if message.chat.type == 'group':
            with open("data/"+str(message.chat.id)+".txt", "a") as sms:
                sms.writelines(str(message.text)+" / "+"@"+message.from_user.username+"\n")
