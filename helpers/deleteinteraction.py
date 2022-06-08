# Imports
import disnake
from disnake import ApplicationCommandInteraction, Option, OptionType
from disnake.enums import ButtonStyle



class deleteinteraction(disnake.ui.View):
   def __init__(self):
      super().__init__(timeout=None)
   
   @disnake.ui.button(label="Delete Interaction ❌", style=ButtonStyle.red, custom_id="deleteinter")
   async def first_button(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
      if not interaction.author:
         await interaction.send("You Must Be The Author To Delete The Interaction", ephemeral=True)
      else:
         await interaction.message.delete()
