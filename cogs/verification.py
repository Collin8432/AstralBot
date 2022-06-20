# Imports
import disnake
from disnake.ext import commands



from helpers.database import verification_search, verifyrole_search
from helpers.webhook import webhooksend
from helpers.deleteinteraction import deleteinteraction
from helpers.color import color
from helpers.message import interactionsend


 
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont



import random



# Checker 
async def Checker(self, filename):
   def check(message):
      return message.content == filename.upper() or message.content == filename.lower()
   await self.bot.wait_for("message", check=check)
   
   
   
# Class Verification
class Verification(commands.Cog, name="Verification"):
   def __init__(self, bot: commands.Bot):
      self.bot = bot

      

   @commands.slash_command(
      name="verify",
      description="Verify yourself to gain access to the server"
   )
   async def verify(interaction):
      verifych = await verification_search(f"{interaction.guild.id}")
      verifychannel = int(verifych)  
      if interaction.channel.id != verifychannel:
         await interactionsend(interaction=interaction, msg=f"You can only use this command in <#{verifychannel}>", view=deleteinteraction())
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
         await interactionsend(interaction=interaction, file=disnake.File(f"./img/astral{FileName}.png"), view=deleteinteraction())
         try:
               await Checker(f"{FileName}")
         except:
               pass
         verifyrole = await verifyrole_search(f"{interaction.guild.id}")
         await interaction.author.add_roles(disnake.Object(verifyrole))  
         await webhooksend("Member Verified", f"Verified <@{interaction.author.id}>", f"{interaction.guild.id}")        
         await interaction.channel.purge(limit=9999999)
         embed = disnake.Embed(
               title=f"How To Verify!",
               description=f"**To Verify Yourself, Please Enter /verify, Then Enter The Code, Case InSensitive**",
               color=color,
               timestamp=disnake.utils.utcnow()
         )
         embed.set_image(
               file=disnake.File(f"C:/Users/astro/Documents/GitHub/AstralBot/img/VerifyVideo.mp4")
         )
         embed.set_footer(
               text=f"Astral Verification"
            )
         await interactionsend(interaction=interaction, embed=embed)