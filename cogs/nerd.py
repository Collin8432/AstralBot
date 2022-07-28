import disnake
from disnake.ext import commands
from disnake import ButtonStyle


 

class NerdButton(disnake.ui.View):
      def __init__(self):
         super().__init__(timeout=None)


      @disnake.ui.button(emoji="🤓", style=ButtonStyle.red, custom_id="nerd")
      async def first_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
      ):
         await interaction.send("nerd")
   
   
      @disnake.ui.button(custom_id="deleteinter", emoji="❌", style=ButtonStyle.red)
      async def delcallback(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
         if not interaction.author:
            await interaction.send("This button is not for you", ephemeral=True)
         else:
            await interaction.message.delete()


class Nerd(commands.Cog):

   def __init__(self, bot):
      self.bot = bot


   @commands.slash_command(
      name="nerd",
      description="nerd"
   )
   async def nerd(self, interaction):
      await interaction.send(view=NerdButton())