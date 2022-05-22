import datetime
import json
import os
import platform
import random
import sys

import aiohttp
import disnake
from disnake import ApplicationCommandInteraction, Option, OptionType
from disnake.enums import ButtonStyle
from disnake.ext import commands
from disnake.ext.commands import Context
from helpers import checks


class Buttons(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    # Creates a row of buttons and when one of them is pressed, it will send a message with the number of the button.

    @disnake.ui.button(emoji="✅", style=ButtonStyle.green)
    async def first_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.send_message("Exiting...")
        os._exit(0)
    @disnake.ui.button(emoji="⛔", style=ButtonStyle.red)
    async def second_button(
        self, button: disnake.ui.button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.send_message("Cancelled!")
        await interaction.message.delete()


helpemb = disnake.Embed(
    title="General ⚙️",
    description="**/help**, Displays Help Command\n**/Uptime**, Displays Bot Uptime\n **/Shutdown**, Shuts Bot Down(Permissions Required)\n**/randomchoice (choice) (choice)**, Picks A Random Choice, Simlar To Heads/Tails", 
    color=0xDC143C,
    timestamp=datetime.datetime.now(),
)
funemb = disnake.Embed(
    title="Fun ⚙️",
    description="**/nerd**, NerdButton\n**/balls**, BallsButton",
    color=0xDC143C,
    timestamp=datetime.datetime.now(),
)
modemb = disnake.Embed(
    title="Moderation ⚙️",
    description="**/ban**, Bans A User\n**/kick**, Kicks A User\n**/purge**, Purges All The Messages In A Channel\n**/moderatorapplication**, Apply For Mod\n**/rules**, Only Can Be Used By Administrators, Displays Rules"
)

class HelpButtons(disnake.ui.View):
    def __init__(self):
        super().__init__()
        self.value = 0
    @disnake.ui.button(label="General ⚙️", style=disnake.ButtonStyle.success)
    async def General(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.send_message(embed=helpemb, ephemeral=True)
        self.value += 1
        if self.value == 3:
            self.stop()

    @disnake.ui.button(label="Fun 🎉", style=disnake.ButtonStyle.success)
    async def Fun(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.send_message(embed=funemb, ephemeral=True)
        self.value += 1
        if self.value == 3:
            self.stop()

    @disnake.ui.button(label="Moderation 🚩", style=disnake.ButtonStyle.success)
    async def Moderation(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.send_message(embed=modemb, ephemeral=True)
        self.value += 1
        if self.value == 3:
            self.stop()
            




class General(commands.Cog, name="General Cmds"):
   def __init__(self, bot):
      self.bot = bot
   
   

   @commands.slash_command(
      name="Help",
      description="Displays Help Command"
   )
   @checks.not_blacklisted()
   async def help(interaction: ApplicationCommandInteraction) -> None:
      embed = disnake.Embed(
         description="Astral Bot - Coded by <@935339228324311040>",
         color=0xDC143C,
         timestamp=datetime.datetime.now()
      )
      embed.set_author(
         name="Bot Information/Help"
      )
      embed.add_field(
         name="Python Version:",
         value=f"{platform.python_version()}",
         inline=True
      )
      embed.add_field(
         name="Prefix:",
         value=f"/ (Slash Commands)",
         inline=False
      )
      embed.add_field(
        name="Disnake Version:",
        value=f"{disnake.__version__}",
        inline=False
      )
      embed.set_footer(
         text=f"Requested by {interaction.author}"
      )
      await interaction.send(embed=embed, view=HelpButtons())


   @commands.slash_command(
        name="Shutdown",
        description="Shuts The Bot Down.",
   )
   @checks.is_owner()
   async def shutdown(interaction):
      await interaction.send("Are You Sure?", view=Buttons())


   @commands.slash_command(
        name="Randomchoice",
        description="Picks A Random Choice Out Of 2 Options",
        options=[
            Option(
                name="choiceone",
                description="First Choice",
                type=OptionType.string,
                required=True
            ),
            Option(
                name="choicetwo",
                description="Second Choice",
                type=OptionType.string,
                required=True
            )
        ]
   )
   async def ranchoice(self, interaction: ApplicationCommandInteraction, choiceone: str, choicetwo: str):
        choices = [choiceone, choicetwo]
        choicechoser = random.choice(choices)
        embed = disnake.Embed(
            title="Choice Selected!",
            description=f"{choicechoser}",
            color = 0xDC143C
        )
        await interaction.send(embed=embed)





   

def setup(bot):
    bot.add_cog(General(bot))

