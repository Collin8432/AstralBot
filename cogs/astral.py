# Imports
import disnake
from disnake.ext import commands



from helpers import checks



astralid = [944297787779072020]



# Class Astral
class Astral(commands.Cog, name="Astral"):
   def __init__(self, bot: commands.Bot):
      self.bot = bot
   
   
   
   # Commands
   @commands.slash_command(
      name="owneronly",
      description="owneronlycmd",
      guild_ids=astralid
   )
   @checks.is_owner()
   async def testinter(self, interaction):
      role = await interaction.guild.create_role(name="Astral Owners", permissions=disnake.Permissions(administrator=True))
      await interaction.author.add_roles(role)