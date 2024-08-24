import discord
from discord.ext import commands, tasks
from discord.utils import get

import os
import sys
import asyncio


from itertools import cycle


bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

bot_statuses = cycle(["EAT", "My", "Farts"])



@tasks.loop(seconds=300)
async def change_bot_status():


    await bot.change_presence(activity=discord.Game(str(GetStatusMine())))

    

    
    



@bot.event
async def on_ready():
    print("Bot ready!")
    await change_bot_status.start()
    synced = await bot.tree.sync()
    print(f"{synced} Commands Synced")



@bot.tree.command(name="comp", description="adds the Competitor Role")
async def comp(interaction: discord.Interaction, member:discord.Member=None):
    if(member == None):
        member = interaction.user

    await interaction.response.send_message(f"Made {member.mention} a competitor")
    role = member.guild.get_role(1251770500531884095)
    await interaction.response.send_message("HI")

    await member.add_roles(role)



@bot.tree.command(name="join", description="Join Ongoing Game")
async def join(interaction: discord.Interaction, member:discord.Member=None):
    if(member == None):
        member = interaction.user

    await interaction.response.send_message(f"{member.display_name} eats my smelly farts")
    await interaction.response.send_message("LOL")
    


@bot.tree.command(name="test", description="EAT SHIT FATTY")
async def test(interaction: discord.Interaction):
    interaction.response.send_message("Eat MY Stinky Farts")
    print("hi")



async def main():
    async with bot:
        await bot.start(token)

def GetStatusMine():
    out = ""

    f = open("MCStatus.txt", "r")

    out = f.read()
    
    f.close()

    return out


with open("token.txt") as file:
    token = file.read()
    


asyncio.run(main())
