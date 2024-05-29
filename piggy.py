import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import random

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

bot = commands.Bot(command_prefix='$', intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$whos a little pig'):
        await message.channel.send('joey!')
    if message.content.startswith('$show me a piggy'):
        random_num = random.randint(1, 27)
        image_path = 'assets/' + str(random_num) + '.jpg'
        await message.channel.send(file=discord.File(image_path))

client.run(os.getenv('DISCORD_TOKEN'))

