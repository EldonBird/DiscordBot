import discord
from discord.ext import commands, tasks
from discord.utils import get


import os
import sys
import asyncio

#import openpyxl
#from openpyxl import load_workbook

import DBManager


from itertools import cycle


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

bot_statuses = cycle(["Status One", "Hello", "Eat My Farts", "Campain Happening"])

@tasks.loop(seconds=5)
async def change_bot_status():
    await bot.change_presence(activity=discord.Game(next(bot_statuses)))

@bot.event
async def on_ready():
    print("Bot ready!")
    change_bot_status.start()
    synced = await bot.tree.sync()
    print(f"{synced} Commands Synced")



@bot.tree.command(name="hello", description="Says Hi!")
async def heya(interaction: discord.Interaction):
    print("HI")
    await interaction.response.send_message(f"HI, {interaction.user.display_name}")
    #await interaction.reply(f"hello there, {interaction.author.mention}!")




@bot.tree.command(name="comp", description="adds the Competitor Role")
async def comp(interaction: discord.Interaction, member:discord.Member=None):
    if(member == None):
        member = interaction.user

    await interaction.response.send_message(f"Made {member.mention} a competitor")

    role = member.guild.get_role(1251770500531884095)


    await member.add_roles(role)



with open("token.txt") as file:
    token = file.read()


async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with bot:
        await load()
        await bot.start(token)


async def load_DB():





asyncio.run(main())
