"""
Contains interaction send - used to send messages within an interaction

Copyright 2022-Present Astral 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

# Imports
import disnake
from disnake import ApplicationCommandInteraction


from .deleteinteraction import deleteinteraction


from typing import Optional


async def send(
   interaction: Optional[ApplicationCommandInteraction], 
   msg: Optional[str] = None, 
   view: Optional[str] = None, 
   ephemeral: bool = False, 
   modal: Optional[str] = None, 
   embed: Optional[str] = None,
   channel: Optional[disnake.TextChannel] = None,
   ) -> None:
   if embed is not None:
      if embed.footer.text is None:
      
         embed.set_footer(
            text="Requested by {}".format(interaction.author)
         )
      if embed.footer.icon_url is None:
         embed.set_footer(icon_url=interaction.author.display_avatar.url)
   if modal is not None:
      return await interaction.response.send_modal(modal=modal)
      
      
   elif ephemeral == True and view is None and embed is None and channel is None:
      return await interaction.send(msg, ephemeral=True)
      
      
   elif ephemeral == True and view is None and embed is not None and channel is None:
      return await interaction.send(msg, ephemeral=True, embed=embed)
      
      
   elif ephemeral == True and view is not None and embed is not None and channel is None:
      return await interaction.send(msg, view=view, embed=embed, ephemeral=True)
      
      
   elif ephemeral == False and view is None and embed is not None and channel is None:
      return await interaction.send(msg, view=deleteinteraction(), embed=embed)
      
      
   elif ephemeral == False and view is not None and embed is not None and channel is None:
      return await interaction.send(msg, view=view, embed=embed)
      
   elif ephemeral == False and view is None and embed is None and channel is None:
      return await interaction.send(msg, view=deleteinteraction()) 
   
   elif ephemeral == True and view is None and embed is None and channel is not None:
      return await channel.send(msg, ephemeral=True)
      
      
   elif ephemeral == True and view is None and embed is not None and channel is not None:
      return await channel.send(msg, ephemeral=True, embed=embed)
      
      
   elif ephemeral == True and view is not None and embed is not None and channel is not None:
      return await channel.send(msg, view=view, embed=embed, ephemeral=True)
      
      
   elif ephemeral == False and view is None and embed is not None and channel is not None:
      return await channel.send(msg, view=deleteinteraction(), embed=embed)
      
      
   elif ephemeral == False and view is not None and embed is not None and channel is not None:
      return await channel.send(msg, view=view, embed=embed)
      
   elif ephemeral == False and view is None and embed is None and channel is not None:
      return await channel.send(msg, view=deleteinteraction()) 
 
   else:
      return await interaction.send(msg, ephemeral=True, view=view)