import disnake
from disnake.ext import commands


class Testcmd(commands.Cog):

   def __init__(self, bot):
      self.bot = bot

   @commands.slash_command(name="yoxxx")
   async def yoxxx(self, ctx):
      await ctx.send("g")