# bot.py
import os
import responses
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return # ignore bot's own message

    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)

    print(f"{username} said: '{user_message}' [{channel}])")
    response = responses.handle_response(message)

#    await message.author.send(response) # reply in private
    await message.channel.send(response) # reply in server channel
    
client.run(TOKEN)
