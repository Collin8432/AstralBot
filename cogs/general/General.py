import json
import os
import random
import sys
import platform

import aiohttp
import disnake
from disnake.ext import commands
from disnake.ext.commands import Context
from disnake import ApplicationCommandInteraction, Option, OptionType
from disnake.enums import ButtonStyle
from disnake.ext import commands

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

class Help(disnake.ui.Select):
    def __init__(self):

        options = [
            disnake.SelectOption(
                label="General", description="Displays General Commands, For The Bot", emoji="⚙️"
            ),
            disnake.SelectOption(
                label="Fun", description="Displays Fun Commands", emoji="⚙️"
            ),
        ]

        super().__init__(
            placeholder="Choose...",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: disnake.MessageInteraction):
        choices = {
            "general": 0,
            "fun": 1,
        }
        user_choice = self.values[0].lower()
        user_choice_index = choices[user_choice]

        result_embed = disnake.Embed(color=0xDC143C )
        result_embed.set_author(name=interaction.author.display_name, icon_url=interaction.author.avatar.url)

        if user_choice_index == 0:
            result_embed.description = f"**General Help**"
            result_embed.colour = 0xDC143C
            result_embed.add_field(
                name="Help", 
                value=f"```Displays Help Command```",
                inline=True
            )
            result_embed.add_field(
                name="Test", 
                value=f"```Not A Real Command```",
                inline=True
            )
            result_embed.add_field(
                name="Test", 
                value=f"```Not A Real Command```",
                inline=True
            )
            result_embed.add_field(
                name="Test", 
                value=f"```Not A Real Command```",
                inline=True
            )
            result_embed.add_field(
                name="Test", 
                value=f"```Not A Real Command```",
                inline=True
            )
            result_embed.add_field(
                name="Test", 
                value=f"```Not A Real Command```",
                inline=True
            )
        elif user_choice_index == 1:
            result_embed.description = f"**In Progress**"
            result_embed.colour= 0xDC143C
        else:
            result_embed.description = f"**Error!**"
            result_embed.colour= 0xDC143C
            
        await interaction.response.defer()
        await interaction.edit_original_message(embed=result_embed, content=None, view=None)


class HelpView(disnake.ui.View):
    def __init__(self):
        super().__init__()

        self.add_item(Help())


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
         description="Newlife Bot - Coded by <@935339228324311040>",
         color=0xDC143C
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
      embed.set_footer(
         text=f"Requested by {interaction.author}"
      )
      await interaction.send(embed=embed, view=HelpView())


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

