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

from helpers import checks


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

        bot_choice = random.choice(list(choices.keys()))
        bot_choice_index = choices[bot_choice]

        result_embed = disnake.Embed(color=0xDC143C )
        result_embed.set_author(name=interaction.author.display_name, icon_url=interaction.author.avatar.url)

        if user_choice_index == 0:
            result_embed.description = f"**In Progress**"
            result_embed.colour = 0xDC143C
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
   async def help(interaction: ApplicationCommandInteraction) -> None:
      embed = disnake.Embed(
         description="Newlife Bot - Coded by Astro",
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

def setup(bot):
    bot.add_cog(General(bot))