import disnake
from disnake.ext import commands


class Guildicon(commands.Cog):

   def __init__(self, bot):
      self.bot = bot

   
   @commands.slash_command(
      name="guildicon",
      description="displays guild icon",
   )
   async def guildicon(self, interaction: disnake.ApplicationCommandInteraction):
      await interaction.send(interaction.guild.icon_url)