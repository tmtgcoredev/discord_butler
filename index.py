import discord
from discord.ext import commands
import datetime

from urllib import parse, request
import re

bot = commands.Bot(command_prefix='>', description="This is a Helper Bot")

@bot.command()
async def ping(ret):
    await ret.send('pong')

@bot.command()
async def sum(ret, numOne: int, numTwo: int):
    await ret.send(numOne + numTwo)

@bot.command()
async def info(ret):
    embed = discord.Embed(title=f"{ret.guild.name}", description="Lorem Ipsum asdasd", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ret.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ret.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ret.guild.region}")
    embed.add_field(name="Server ID", value=f"{ret.guild.id}")
    embed.set_thumbnail(url=f"{ret.guild.icon}")

    await ret.send(embed=embed)

# Events
@bot.listen()
async def on_message(message):
    if "this_is_sparta" in message.content.lower():
        # in this case don't respond with the word "Tutorial" or you will call the on_message event recursively
        await message.channel.send('This is SPARTA https://coursebank.ph/sparta/')
        await bot.process_commands(message)

bot.run('token')