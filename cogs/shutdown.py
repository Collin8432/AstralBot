"""
Contains Shutdown View and command

Copyright 2022-Present Astral 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


import disnake
from disnake import ButtonStyle
from disnake.ext import commands


 

import os


class ShutdownView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        
        
    @disnake.ui.button(emoji="✅", style=ButtonStyle.green, custom_id="shutdowncomfirm")
    async def Confirm(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.send(msg="exiting...")
        os._exit(0)
        
        
    @disnake.ui.button(emoji="⛔", style=ButtonStyle.red, custom_id="shutdowncancel")
    async def Deny(
        self, button: disnake.ui.button, interaction: disnake.MessageInteraction  
    ):
        await interaction.send(msg="Cancelled")
        await interaction.message.delete()
        
        
    @disnake.ui.button(label="Delete Interaction ❌", style=ButtonStyle.red, custom_id="deleteinter")
    async def first_button(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
      if not interaction.author:
         await interaction.send(msg="You Must Be The Author To Delete The Interaction", ephemeral=True)
      else:
         await interaction.message.delete()
         

class Shutdown(commands.Cog):
   def __init__(self, bot: commands.Bot):
      self.bot = bot
      
      
   @commands.slash_command(
      name="shutdown",
      description="shuts the bot down",
   ) 
   @commands.is_owner()
   async def shutdown(interaction):
      await interaction.send(msg="Are You Sure?", view=ShutdownView())