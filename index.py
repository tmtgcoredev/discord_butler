import discord
import os

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

client.run(os.getenv('TOKEN'))