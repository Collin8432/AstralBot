import disnake
from disnake.ext import commands

from guibot import Window


class Testcmd(commands.Cog):

   def __init__(self, bot):
      self.bot = bot

   @commands.slash_command(name="g")
   async def yoxxx(self, ctx):
      await ctx.send("g")
      
   # @commands.slash_command(name="tesxt")
   # async def tesxt(self, ctx):
   #    Window.button1.hide()