#bot by rizicks all purpose bot

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix="!") 

@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name = '!help | != prefix'))
    print("Bot is ONLINE.")


#cool thing
@bot.command(pass_context = True)
async def rally(ctx):
    await bot.say("Legion Transmissions presents to you: https://www.roblox.com/games/2504180464/Veil-RALLY ")

@bot.command(pass_context = True)    
async def holo(ctx):
    await bot.say(" Legion Transmissions presents to you: https://www.roblox.com/games/2505487043/Sentience-I-TRAIN#!/about ")

@bot.command(pass_context = True)
async def ping(ctx):
    await bot.say("PONG :ping_pong: ")    



bot.run("NTA0MzY2NTg5ODY1MzYxNDE5.DrEALA.gEWoWMU7qgiFmYW_uywOjJuVe80")



