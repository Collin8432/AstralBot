# Imports
import disnake
from disnake.ext import tasks, commands
from disnake.ext.commands import Bot
from disnake.ext.commands import Context
from disnake.enums import ButtonStyle



from helpers import checks



import exceptions



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



# BallsButton View
class BallsButton(disnake.ui.View):
   def __init__(self):
      super().__init__(timeout=None)

   @disnake.ui.button(emoji="<:unknown:957276431916859442>", style=ButtonStyle.red, custom_id="balls")
   async def first_button(
      self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
   ):
      await interaction.response.send_message("balls")



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
      await interaction.send(view=NerdButton())
   


   @commands.slash_command(
      name="balls", 
      description="balls"
   )
   async def balls(self, interaction):
      await interaction.send(view=BallsButton())

      

# Adding Cog To Bot
def setup(bot):
    bot.add_cog(Fun(bot))
