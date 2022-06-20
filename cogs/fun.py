# Imports
import disnake
from disnake.ext import tasks, commands
from disnake.ext.commands import Bot
from disnake.ext.commands import Context
from disnake.enums import ButtonStyle
from disnake import ApplicationCommandInteraction, Option, OptionType



import asyncio
import random



from helpers.deleteinteraction import deleteinteraction
from helpers.color import color
from helpers.message import interactionsend



# NerdButton View
class NerdButton(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    # Creates a row of buttons and when one of them is pressed, it will send a message with the number of the button.

    @disnake.ui.button(emoji="🤓", style=ButtonStyle.red, custom_id="nerd")
    async def first_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.send_message("nerd")
   
    @disnake.ui.button(label="Delete Interaction ❌", style=ButtonStyle.red, custom_id="deleteinter")
    async def first_button(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
       if not interaction.author:
          await interactionsend(interaction=interaction, msg="You Must Be The Author To Delete The Interaction", ephemeral=True)
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
      await interaction.response.send_message("balls")
      
   @disnake.ui.button(label="Delete Interaction ❌", style=ButtonStyle.red, custom_id="deleteinter")
   async def first_button(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
      if not interaction.author:
         await interactionsend(interaction=interaction, msg="You Must Be The Author To Delete The Interaction", ephemeral=True)
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
   ''', view=deleteinteraction())
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
      await interactionsend(interaction=interaction, msg=text, view=deleteinteraction())
      
      
      
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
         title=f"{slotmachineoutput}",
         description=description,
         timestamp=disnake.utils.utcnow(),
         color=color
      )
      embed.set_footer(
         text=f"Requested by {interaction.author}"
      )
      await interactionsend(interaction=interaction, embed=embed, view=deleteinteraction())
      
      
      
   @commands.slash_command(
      name="minesweeper",
      description="minesweeper in discord",
      options=[
         Option(
            name="columns",
            description="The number of columns",
            type=OptionType.integer,
            required=False,
         ),
         Option(
            name="rows",
            description="The number of rows",
            type=OptionType.integer,
            required=False,
         ),
         Option(
            name="bombs",
            description="The number of bombs",
            type=OptionType.integer,
            required=False,
         )
      ]
   )
   async def minesweeper(interaction, columns: int, rows: int, bombs: int) -> None:
      columns = None
      rows = None
      bombs = None
      if columns is not None or rows is not None or bombs is not None:
         pass
      else:
         columns = random.randint(4,13)
         rows = random.randint(4,13)
         bombs = columns * rows - 1
         bombs = bombs / 2.5
         bombs = round(random.randint(5, round(bombs)))
      try:
         columns = int(columns)
         rows = int(rows)
         bombs = int(bombs)
      except ValueError:
         await interactionsend(interaction=interaction, msg="Error Getting Values")
      if columns > 13 or rows > 13:
         await interactionsend(interaction=interaction, msg="The limit for the columns and rows are 13 due to discord limits.")
      if columns < 1 or rows < 1 or bombs < 1:
         await interactionsend(interaction=interaction, msg="The provided numbers cannot be zero or negative.")
      if bombs + 1 > columns * rows:
         await interactionsend(interaction=interaction, msg="You have more bombs than spaces on the grid or you attempted to make all of the spaces bombs!")

      grid = [[0 for num in range (columns)] for num in range(rows)]

      loop_count = 0
      while loop_count < bombs:
         x = random.randint(0, columns - 1)
         y = random.randint(0, rows - 1)
         if grid[y][x] == 0:
            grid[y][x] = 'B'
            loop_count = loop_count + 1
         if grid[y][x] == 'B':
            pass

      pos_x = 0
      pos_y = 0
      while pos_x * pos_y < columns * rows and pos_y < rows:
         adj_sum = 0
         for (adj_y, adj_x) in [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]:
            try:
                  if grid[adj_y + pos_y][adj_x + pos_x] == 'B' and adj_y + pos_y > -1 and adj_x + pos_x > -1:
                     adj_sum = adj_sum + 1
            except:
                  pass
         if grid[pos_y][pos_x] != 'B':
            grid[pos_y][pos_x] = adj_sum
         if pos_x == columns - 1:
            pos_x = 0
            pos_y = pos_y + 1
         else:
            pos_x = pos_x + 1

      string_builder = []
      for the_rows in grid:
         string_builder.append(''.join(map(str, the_rows)))
      string_builder = '\n'.join(string_builder)
      string_builder = string_builder.replace('0', '||:white_large_square:||')
      string_builder = string_builder.replace('1', '||:one:||')
      string_builder = string_builder.replace('2', '||:two:||')
      string_builder = string_builder.replace('3', '||:three:||')
      string_builder = string_builder.replace('4', '||:four:||')
      string_builder = string_builder.replace('5', '||:five:||')
      string_builder = string_builder.replace('6', '||:six:||')
      string_builder = string_builder.replace('7', '||:seven:||')
      string_builder = string_builder.replace('8', '||:eight:||')
      final = string_builder.replace('B', '||:bomb:||')

      percentage = columns * rows
      percentage = bombs / percentage
      percentage = 100 * percentage
      percentage = round(percentage, 2)

      embed = disnake.Embed(title='Minesweeper', description=f'\U0000FEFF{final}', timestamp=disnake.utils.utcnow(), color=color)
      embed.add_field(name='Columns:', value=columns, inline=True)
      embed.add_field(name='Rows:', value=rows, inline=True)
      embed.add_field(name='Total Spaces:', value=columns * rows, inline=True)
      embed.add_field(name='\U0001F4A3 Count:', value=bombs, inline=True)
      embed.add_field(name='\U0001F4A3 Percentage:', value=f'{percentage}%', inline=True)
      embed.set_footer(text=f"Requested by {interaction.author}")
      await interactionsend(interaction=interaction, embed=embed, view=deleteinteraction())