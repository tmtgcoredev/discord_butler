import discord
import os

from discord.client import Client

client = discord.Client()

@client.event
async def on_ready():
    print("THIS. IS. SPARTA!!!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith(">sparta"):
        await message.channel.send("ahoo ahoo ahoo!!!")

print(os.getenv('jobs'))
# client.run(piso)
