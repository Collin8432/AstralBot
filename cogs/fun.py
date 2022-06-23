# Imports
import disnake
from disnake.ext import commands
from disnake.enums import ButtonStyle
from disnake import ApplicationCommandInteraction, Option, OptionType



import asyncio
import random



from helpers.color import color
from helpers.message import interactionsend



# NerdButton View
class NerdButton(disnake.ui.View):
      def __init__(self):
         super().__init__(timeout=None)



      @disnake.ui.button(emoji="🤓", style=ButtonStyle.red, custom_id="nerd")
      async def first_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
      ):
         await interactionsend(interaction=interaction, msg="nerd")
   
   
   
      @disnake.ui.button(label="Delete Interaction ❌", style=ButtonStyle.red, custom_id="deleteinter")
      async def first_button(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
         if not interaction.author:
            await interactionsend(interaction=interaction, msg="You must be the author to delete this message", ephemeral=True)
         else:
            await interaction.message.delete()



# BallsButton View
class BallsButton(disnake.ui.View):
   def __init__(self):
      super().__init__(timeout=None)

 
   @disnake.ui.button(emoji="<:unknown:957276431916859442>", style=ButtonStyle.red, custom_id="balls")
   async def first_button(
      self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
   ):
      await interactionsend(interaction=interaction, msg="balls")
      
      
      
   @disnake.ui.button(label="Delete Interaction ❌", style=ButtonStyle.red, custom_id="deleteinter")
   async def first_button(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
      if not interaction.author:
         await interactionsend(interaction=interaction, msg="You must be the author to delete this message", ephemeral=True)
      else:
         await interaction.message.delete()



# Fun Cog
class Fun(commands.Cog, name="fun cmds"):
   def __init__(self, bot):
      self.bot = bot



   # Commands
   @commands.slash_command(
      name="nerd",
      description="nerd"
   )
   async def nerd(self, interaction):
      await interactionsend(interaction=interaction, view=NerdButton())
   


   @commands.slash_command(
      name="balls", 
      description="balls"
   )
   async def balls(self, interaction):
      await interactionsend(interaction=interaction, view=BallsButton())



   @commands.slash_command(
      name="9-11",
      description="9-11 in discord"
      )
   async def nine_eleven(interaction):
      message = await interactionsend(interaction=interaction,   
         msg=f'''``` #
                        ,-------------------. 
                     ,'                    ;
                  ,'                    .'|
                  ,'                    .'# |
               ,'                    .'# # |
               :-------------------.'# # # |
               | # # # # # # # # # | # # # |
               | # # # # # # # # # | # # # |
               | # # # # # # # # # | # # # |
               | # # # # # # # # # | # # # |
               | # # # # # # # # # | # # # |
               | # # # # # # # # # | # # # |
               | #,-'. # # # # # # | # # # |
               |_/'  / # # # # # # | # # # |
         _.--""     /_ # # # # # # | # # #
         '__.--,       `-.# # # # # | # #
            /  /''`--.__; # # # # | #
         _,| ,'  # # # # # # # # #|
         `--|._`.```
   ''')
      await asyncio.sleep(.5)
      await interaction.edit_original_message(  
         content=f'''```
                     ,-------------------.
                     ,'                    ;  '::
                  ,'                    .'|'::::
            ::.: ,'                    .'# |::::':
      ':':.: ,'                    .'# # |::':::'
         :'. : :-------------------.'# # # |':::'::
         :::.:| # # # # # # # # # | # # # |:::::'
         ::.:..| # # # # # # # # # | # # # |::'
      `:;.::'| # # # # # # # # # | # # # |
      '::..:'| #.:::.. # # # # # | # # # |
         :::::|.,:.:::::::..::# # | # # # |
         `:::::::::::.::..:#::::.# | # # # |
         `:':::`::'.::::. :: # # | # # # |
         ,`::::::::::'::'::' # # | # # # |
      `:;.::'| # # # # # # # # # | # # # |
               | # # # # # # # # # | # # # |
               | # # # # # # # # # | # # #
               | # # # # # # # # # | # #
               | # # # # # # # # # | #
               | # # # # # # # # # |```
   ''')



   @commands.slash_command(
      name="emojify",
      description="emojifies your text",
      options=[
         Option(
               name="text",
               description="The text to emojify",
               type=OptionType.string,
               required=True            
         )
      ]
   )
   async def emojify(interaction: ApplicationCommandInteraction, text: str) -> None: 
      if text != None:
         out = text.lower()
         text = out.replace(' ', '   ')\
                  .replace('!', '❗')\
                  .replace('?', '❓')\
                  .replace('a', '\u200B🇦')\
                  .replace('b', '\u200B🇧')\
                  .replace('c', '\u200B🇨')\
                  .replace('d', '\u200B🇩')\
                  .replace('e', '\u200B🇪')\
                  .replace('f', '\u200B🇫')\
                  .replace('g', '\u200B🇬')\
                  .replace('h', '\u200B🇭')\
                  .replace('i', '\u200B🇮')\
                  .replace('j', '\u200B🇯')\
                  .replace('k', '\u200B🇰')\
                  .replace('l', '\u200B🇱')\
                  .replace('m', '\u200B🇲')\
                  .replace('n', '\u200B🇳')\
                  .replace('ñ', '\u200B🇳')\
                  .replace('o', '\u200B🇴')\
                  .replace('p', '\u200B🇵')\
                  .replace('q', '\u200B🇶')\
                  .replace('r', '\u200B🇷')\
                  .replace('s', '\u200B🇸')\
                  .replace('t', '\u200B🇹')\
                  .replace('u', '\u200B🇺')\
                  .replace('v', '\u200B🇻')\
                  .replace('w', '\u200B🇼')\
                  .replace('x', '\u200B🇽')\
                  .replace('y', '\u200B🇾')\
                  .replace('z', '\u200B🇿')
      await interactionsend(interaction=interaction, msg=text)
      
      
      
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
      await interactionsend(interaction=interaction, embed=embed)