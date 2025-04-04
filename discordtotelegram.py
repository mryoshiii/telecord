import discord
from discord.ext import commands , tasks
import requests
import os

from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='%', intents=intents)

channelID = discordChatID
teleChatID = telegramChatID
teleToken = os.getenv('teleToken')
disToken = os.getenv('disToken')


@bot.event
async def on_message(message):
	if message.author != bot.user:
		if message.channel.id == channelID:
			userid = message.author.id
			user = bot.get_user(userid)
			requests.get(f"https://api.telegram.org/bot{teleToken}/sendMessage?chat_id={teleChatID}&text=[{user}] : {message.content}")

bot.run(disToken)

