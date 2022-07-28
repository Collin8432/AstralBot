"""
Contains all games for the bot

Copyright 2022-Present Astral 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""



# Imports
import disnake
from disnake.ext import commands


import random


from utils.color import color
from utils.DeleteButton import DeleteButton
 

class Slots(commands.Cog):

   def __init__(self, bot):
      self.bot = bot


   @commands.slash_command(
      name="slots",
      description="slots in discord"
   )
   async def slots(self, interaction):
      emojis = "🍕🍟🍔🍫🍬🥤🍒🍉"
      a = random.choice(emojis)
      b = random.choice(emojis)
      c = random.choice(emojis)
      slotmachineoutput = f"{a} {b} {c}"
      if (a == b == c):
         description = "Match!, You Win"
      elif (a == b) or (a == c) or (b == c):
         description = "Two Matches!, You Win"
      else:
         description = "No Matches, You Lose"
      embed = disnake.Embed(
         title="{}".format(slotmachineoutput),
         description=description,
         timestamp=disnake.utils.utcnow(),
         color=color
      )
      await interaction.send(embed=embed, view=DeleteButton())
      
   
   