# Imports
import disnake
from disnake import ApplicationCommandInteraction, Option, OptionType
from disnake.enums import ButtonStyle



class DeleteButton(disnake.ui.View):
   def __init__(self):
      self.value = 0
   
   @disnake.ui.button(
      emoji="❌",
      style=ButtonStyle.red,
      custom_id="deletechannel",
   )
   async def button(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
      if not interaction.author:
         await interaction.send("You Must Be The Author To Delete The Interaction", ephemeral=True)
      else:
         await interaction.delete()
         await interaction.message.delete()