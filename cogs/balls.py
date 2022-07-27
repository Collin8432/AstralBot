"""
Contains all fun commands for the bot

Copyright 2022-Present Astral 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


# Imports
import disnake
from disnake.ext import commands
from disnake import ButtonStyle


 


class BallsButton(disnake.ui.View):
   def __init__(self):
      super().__init__(timeout=None)

 
   @disnake.ui.button(emoji="<:unknown:957276431916859442>", style=ButtonStyle.red, custom_id="balls")
   async def first_button(
      self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
   ):
      await interaction.send(msg="balls")
      
      
   @disnake.ui.button(label="Delete Interaction ❌", style=ButtonStyle.red, custom_id="deleteinter")
   async def first_button(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
      if not interaction.author:
         await interaction.send(msg="You must be the author to delete this message", ephemeral=True)
      else:
         await interaction.message.delete()


class Balls(commands.Cog, name="fun cmds"):
   def __init__(self, bot):
      self.bot = bot


   @commands.slash_command(
      name="balls", 
      description="balls"
   )
   async def balls(self, interaction):
      await interaction.send(view=BallsButton())