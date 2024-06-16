import discord
from discord.ext import commands, tasks
from discord.utils import get

import os
import asyncio


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

@bot.command()
async def hello(ctx):
    await ctx.send(f"hello there, {ctx.author.mention}!")

@bot.command()
async def Comp(ctx):
    member = ctx.message.author
    role = get(member.guild.roles, name="Competitor")
    await member.add_roles(role)
    await ctx.send("EAT SHIT FATTY!")


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


asyncio.run(main())
