# Imports
import disnake
from disnake import ApplicationCommandInteraction



from helpers.deleteinteraction import deleteinteraction


from typing import Optional



async def interactionsend(interaction: ApplicationCommandInteraction, message: Optional[str] = None, view: Optional[str] = None, ephemeral: bool = False, modal: Optional[str] = None):
   try:
      await interaction.response.send_modal(modal=modal)
   except: 
      pass
   try: 
      interaction.send(message, view=deleteinteraction(), ephemeral=ephemeral)
   except:
      interaction.send(message, view=view, ephemeral=ephemeral)