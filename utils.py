
MY_COMMANDS=["sub news","test command"]

def commands_checker(message):
    fg=0
    for commands_check in range(len(MY_COMMANDS)):
        if MY_COMMANDS[commands_check] in message.text:
            fg+=1
    return fg