# Imports
import disnake
from disnake import ApplicationCommandInteraction
from disnake import embeds



from .deleteinteraction import deleteinteraction



from typing import Optional



async def interactionsend(interaction: ApplicationCommandInteraction, msg: Optional[str] = None, view: Optional[str] = None, ephemeral: bool = False, modal: Optional[str] = None, embed: Optional[str] = None) -> None:
   if embed is not None:
      if embed.footer.text is None:
      
         embed.set_footer(
            text="Requested by {}".format(interaction.author)
         )
   if modal is not None:
      await interaction.response.send_modal(modal=modal)
   elif ephemeral == True and view is None:
      await interaction.send(msg, ephemeral=True, embed=embed)
   elif ephemeral == True and view is not None:
      await interaction.send(msg, view=view, embed=embed, ephemeral=True)
   elif ephemeral == False and view is None:
      await interaction.send(msg, view=deleteinteraction(), embed=embed)
   elif ephemeral == False and view is not None:
      await interaction.send(msg, view=view, embed=embed)
   