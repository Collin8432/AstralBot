# Imports
import disnake
from disnake.ext import commands



class nsfw(commands.Cog, name="NSFW"):
   def __init__(self, bot: commands.Bot):
      self.bot = bot
   
   
   
   # Commands
   
   
   
   
def setup(bot):
   bot.add_cog(nsfw(bot))