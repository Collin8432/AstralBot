"""
Contains Class deleteinteraction which contains a button view to delete a message

Copyright 2022-Present Astral 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


# Imports
import disnake
from disnake import ApplicationCommandInteraction
from disnake.enums import ButtonStyle


from typing import Optional


async def interactionsend(interaction: ApplicationCommandInteraction, msg: Optional[str] = None, view: Optional[str] = None, ephemeral: bool = False, modal: Optional[str] = None, embed: Optional[str] = None) -> None:
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
      
      
class deleteinteraction(disnake.ui.View):
   def __init__(self):
      super().__init__(timeout=None)
   
   
   
   @disnake.ui.button(label="Delete Message ❌", style=ButtonStyle.red, custom_id="deleteinter")
   async def first_button(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
      if not interaction.author:
         await interactionsend(interaction=interaction, msg="You must be the author to delete this message", ephemeral=True)
      else:
         await interaction.message.delete()