"""
Contains all verification commands for the bot

Copyright 2022-Present Astral 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


# Imports
import disnake
from disnake.ext import commands


from utils.db import *
from utils.webhook import webhooksend
from utils.color import color
from utils.message import send

 
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


import random


async def Checker(self, filename):
   def check(message):
      return message.content == filename.upper() or message.content == filename.lower()
   await self.bot.wait_for("message", check=check)
   
   
class Verification(commands.Cog, name="Verification"):
   def __init__(self, bot: commands.Bot):
      self.bot = bot


   @commands.slash_command(
      name="verify",
      description="Verify yourself to gain access to the server"
   )
   async def verify(interaction):
      verifych = fetch_guild_information("guild_verificationchannel", f"{interaction.guild.id}")
      verifychannel = int(verifych)  
      if interaction.channel.id != verifychannel:
         await send(interaction=interaction, msg=f"You can only use this command in <#{verifychannel}>")
      else:
         list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
         FileName = ""
         for i in range(5, 15):
               FileName += (random.choice(list))
               continue
         img = Image.open('./img/Astral.png')

         image = ImageDraw.Draw(img)
         font = ImageFont.truetype("./font/MomB.ttf", 30)

         guildname = interaction.guild.name
         widthithink = 222
         width = widthithink - len(guildname) * 7.5
         
         image.text((width, 375), f"to {guildname}", fill=(43,22,197), font=font)
         image.text((160, 275), f"{FileName}", fill=(32,22,197), font=font)
         image.text((125, 300), f"Please enter the", fill=(43,22,197), font=font)
         image.text((125, 325), f"letters/numbers", fill=(43,22,197), font=font)
         image.text((85, 350), f"above to gain access", fill=(43,22,197), font=font)
         img.save(f"./img/astral{FileName}.png")
         await send(interaction=interaction, file=disnake.File(f"./img/astral{FileName}.png"))
         try:
               await Checker(f"{FileName}")
         except:
               pass
         verifyrole = fetch_guild_information("guild_verifyrole", f"{interaction.guild.id}")
         await interaction.author.add_roles(disnake.Object(verifyrole))  
         await webhooksend("Member Verified", f"Verified <@{interaction.author.id}>", f"{interaction.guild.id}")        
         await interaction.channel.purge(limit=9999999)
         embed = disnake.Embed(
               title=f"How To Verify!",
               description=f"**To Verify Yourself, Please Enter /verify, Then Enter The Code, Case InSensitive**",
               color=color,
               timestamp=disnake.utils.utcnow()
         )
         embed.set_footer(
               text=f"Astral Verification"
            )
         await send(interaction=interaction, embed=embed)