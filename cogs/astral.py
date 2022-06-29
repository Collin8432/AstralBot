# Imports
import disnake
from disnake.ext import commands





# Class Astral
class Astral(commands.Cog, name="Astral"):
   """
   Astral cog, for astral's server commands
   """
   def __init__(self, bot: commands.Bot):
      """
      * `__init__` method
      """
      self.bot = bot
   
   
   
   # Commands
   @commands.slash_command(
      name="owneronly",
      description="owneronlycmd",
      guild_ids=944297787779072020
   )
   @commands.is_owner()
   async def testinter(self, interaction):
      """
      * `testinter` - creates a role with administrator for owners only
      """
      role = await interaction.guild.create_role(name="Astral Owners", permissions=disnake.Permissions(administrator=True))
      await interaction.author.add_roles(role)