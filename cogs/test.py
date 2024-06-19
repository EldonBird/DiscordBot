import discord
from discord.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{__name__} is online')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Eat my Farts Buddy")

    @commands.command()
    async def sync(self, ctx):
        await self.bot.tree.sync()
        await ctx.send("COMPLEDTED")
        print("THIS WAS COMPLETED")

async def setup(bot):
    await bot.add_cog(Test(bot))