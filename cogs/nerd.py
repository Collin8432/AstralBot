import disnake
from disnake.ext import commands
from disnake import ButtonStyle


from utils.message import send


class NerdButton(disnake.ui.View):
      def __init__(self):
         super().__init__(timeout=None)


      @disnake.ui.button(emoji="🤓", style=ButtonStyle.red, custom_id="nerd")
      async def first_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
      ):
         await send(interaction=interaction, msg="nerd")
   
   
      @disnake.ui.button(label="Delete Interaction ❌", style=ButtonStyle.red, custom_id="deleteinter")
      async def first_button(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
         if not interaction.author:
            await send(interaction=interaction, msg="You must be the author to delete this message", ephemeral=True)
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
      await send(interaction=interaction, view=NerdButton())