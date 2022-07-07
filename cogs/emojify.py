import disnake
from disnake.ext import commands


from utils.message import send


class Emojify(commands.Cog):

   def __init__(self, bot):
      self.bot = bot


   
   @commands.slash_command(
      name="emojify",
      description="emojifies your text",
   )
   async def emojify(interaction: disnake.ApplicationCommandInteraction,
                     text: str = None,
                     ) -> None: 
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
      await send(interaction=interaction, msg=text, ephemeral=True)
