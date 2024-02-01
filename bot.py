import discord
import responses
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

async def send_message(message):
    try:
        response = await responses.handle_response(message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        print(f"{message.author} said:'{message.content}' ({message.channel})")

        if message.content[0] == '-':
            message.content = message.content[1:]
            await send_message(message)

    client.run(TOKEN)
