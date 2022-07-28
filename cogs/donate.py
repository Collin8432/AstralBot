import disnake
from disnake.ext import commands

from utils.color import color
from utils.DeleteButton import DeleteButton

class Donate(commands.Cog):

   def __init__(self, bot):
      self.bot = bot

   
   @commands.slash_command(
      name="donate",
      description="donate to the bot owner"
   )
   async def donate(self, interaction):
      embed = disnake.Embed(
         title="Donate",
         description="If you like the bot, please consider donating to the bot owner\nBTC: bc1q6cztd7sxrdppnutevwk0jfts76t4vdsdeagx0h\nETH: 0xFf4Ef7f4b9806BA1d95b8223C494Bf7ABc7E537A\nLTC: LYuMZVsCp6Uijzmu1wKq832UtGfCztgH2B",
         color=color,
         timestamp=disnake.utils.utcnow()
      )
      await interaction.send(embed=embed, view=DeleteButton())