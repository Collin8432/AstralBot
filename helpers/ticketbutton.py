# Imports 
import disnake
from disnake.enums import ButtonStyle
from disnake.ext import commands



# Class TicketButton
class Ticketbutton(disnake.ui.View):
   def __init__(self):
        super().__init__(timeout=None)
      
   @disnake.ui.button(label="Ping Staff ❗", style=disnake.ButtonStyle.success, custom_id="pingstaff")
   async def pingstaff(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
      pingrole = interaction.guild.get_member(935339228324311040) # type: ignore
      await interaction.send(pingrole.mention) # type: ignore
   
   @disnake.ui.button(label="Delete Channel ❌", style=disnake.ButtonStyle.danger, custom_id="deletechannel")
   @commands.has_permissions(administrator=True)
   async def deletechannel(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
      await interaction.channel.delete()

