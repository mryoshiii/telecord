import telebot
import requests
import os

from dotenv import load_dotenv
load_dotenv()
channelID = discordChatID
teleChatID = telegramChatID
# ЗДЕСЬ НУЖНО УКАЗАТЬ АЙДИ ВАШЕГО ЧАТА В ТГ И В ДИСКОРДЕ
# Чтобы их получить прочтите readme файл из репозитория
teleToken = os.getenv('teleToken')
disToken = os.getenv('disToken')


bot = telebot.TeleBot(teleToken)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.chat.id == teleChatID:
        bot_url = f"https://discord.com/api/v10/channels/{channelID}/messages"
        headers_data = {
            "Authorization": f"Bot {disToken}",
            "Content-Type": "application/json",
        }
        json_data = {
            'content': f'**[{message.from_user.username}]:** {message.text}',
        }
        requests.post(bot_url, headers=headers_data , json=json_data)
    else:
        print(f'oops {teleChatID} , {message.chat.id}')
bot.polling(none_stop=True, interval=0)