import json
import os
import platform
import random
import sys
import asyncio 

import disnake
from disnake import ApplicationCommandInteraction
from disnake.ext import tasks, commands
from disnake.ext.commands import Bot
from disnake.ext.commands import Context
from discord_webhook import DiscordWebhook, DiscordEmbed
import traceback
from disnake.enums import ButtonStyle


from helpers import checks
import exceptions
class NerdButton(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    # Creates a row of buttons and when one of them is pressed, it will send a message with the number of the button.

    @disnake.ui.button(emoji="🤓", style=ButtonStyle.red)
    async def first_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.send_message("nigger")



class ModApp(disnake.ui.Modal):
    def __init__(self) -> None:
        components = [
            disnake.ui.TextInput(
                label="What Are You Applying For?",
                placeholder="Ex. Mod, Moderator, etc...",
                custom_id="ApplyingFor",
                style=disnake.TextInputStyle.short,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="What Are You Experienced In?",
                placeholder="Ex. Discord, Minecraft, etc...",
                custom_id="Experience",
                style=disnake.TextInputStyle.short,
                min_length=5,
                max_length=50
            ),
            disnake.ui.TextInput(
                label="Why Are You Better Than Others?",
                placeholder="Ex. I have a lot of experience in this role, I know how to do this, etc...",
                custom_id="BR",
                style=disnake.TextInputStyle.paragraph,
                min_length=20,
                max_length=500
            )
        ]
        super().__init__(title="Moderator Application", custom_id="ModApp", components=components)

    async def callback(self, interaction: disnake.ModalInteraction) -> None:
        ApplyingFor = interaction.text_values["ApplyingFor"]
        Experience = interaction.text_values["Experience"]
        BR = interaction.text_values["BR"]
        embed = disnake.Embed(
           title=f"New Application",
           description=f"<@{interaction.author.id}> Submitted This Application \n**Appplying For:**\n{ApplyingFor}\n**Experience:**\n{Experience}\n**Why Are You Better Than Others For Your Role:**\n{BR}",
           color=0xDC143C
        )
        await interaction.response.send_message(embed=embed)
    async def on_error(self, error: Exception, inter: disnake.ModalInteraction) -> None:
        await inter.response.send_message("Something Went Wrong Here...", ephemeral=True)



class BallsButton(disnake.ui.View):
   def __init__(self):
      super().__init__(timeout=None)

   @disnake.ui.button(emoji="<:unknown:957276431916859442>", style=ButtonStyle.red)
   async def first_button(
      self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
   ):
      await interaction.response.send_message("balls")

class Fun(commands.Cog, name="fun cmds"):
    def __init__(self, bot):
        self.bot = bot

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


    @commands.slash_command(
       name="ModeratorApplication",
       description="Sends A Moderator Appliction"
    )
    async def Appliction(inter: disnake.CommandInteraction):
      # Sends a modal using a high level implementation.
      await inter.response.send_modal(modal=ModApp())

      
def setup(bot):
    bot.add_cog(Fun(bot))
