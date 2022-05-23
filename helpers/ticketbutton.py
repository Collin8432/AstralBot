import disnake
from disnake.enums import ButtonStyle
from disnake.ext import commands


class Ticketbutton(disnake.ui.View):
   def __init__(self):
        super().__init__(timeout=None)
      
   @disnake.ui.button(label="Ping Staff ❗", style=disnake.ButtonStyle.success)
   async def pingstaff(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
      pingrole = interaction.guild.get_role(978080848706404413)
      await interaction.send(pingrole.mention)
   
   @disnake.ui.button(label="Delete Channel ❌", style=disnake.ButtonStyle.danger)
   @commands.has_permissions(administrator=True)
   async def deletechannel(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
      await interaction.channel.delete()

