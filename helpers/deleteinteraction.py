# Imports
import disnake
from disnake import ApplicationCommandInteraction
from disnake.enums import ButtonStyle



from typing import Optional



async def messagesend(interaction: ApplicationCommandInteraction, msg: Optional[str] = None, view: Optional[str] = None, ephemeral: bool = False, modal: Optional[str] = None):
   try:
      await interaction.response.send_modal(modal=modal)
   except: 
      pass
   try: 
      interaction.send(msg, view=deleteinteraction(), ephemeral=ephemeral)
   except:
      interaction.send(msg, view=view, ephemeral=ephemeral)



class deleteinteraction(disnake.ui.View):
   def __init__(self):
      super().__init__(timeout=None)
   
   @disnake.ui.button(label="Delete Message ❌", style=ButtonStyle.red, custom_id="deleteinter")
   async def first_button(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
      if not interaction.author:
         await messagesend(interaction=interaction, msg="You Must Be The Author To Delete The Interaction", ephemeral=True)
      else:
         await interaction.message.delete()
         