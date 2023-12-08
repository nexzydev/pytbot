# Exemplo

from src.init import Bot

bot = Bot('TOKEN AQUI')

while True:
    command_info = bot.command('/start') 
    if command_info:
        chat_id = command_info['chat_id']
        bot.send_text(chat_id, "Hello")  

    
