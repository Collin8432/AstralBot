"""
Contains the help command for the bot

Copyright 2022-Present Astral 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


import disnake
from disnake import ButtonStyle
from disnake.ext import commands


from utils.discembeds import *
 

import platform
import psutil


class HelpButtons(disnake.ui.View):
    def __init__(self):
        super().__init__()
        self.value = 0
        
        
    @disnake.ui.button(label="General ⚙️", style=disnake.ButtonStyle.success, custom_id="genhelp")
    async def General(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = helpemb
        embed.set_footer(
            text="Requested by {}".format(interaction.author)
        )
        await interaction.send(embed=embed, ephemeral=True)
        

    @disnake.ui.button(label="Fun 🎉", style=disnake.ButtonStyle.success, custom_id="funhelp")
    async def Fun(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = funemb
        embed.set_footer(
            text="Requested by {}".format(interaction.author)
        )   
        await interaction.send(embed=embed, ephemeral=True)


    @disnake.ui.button(label="Moderation 🚩", style=disnake.ButtonStyle.success, custom_id="modhelp")
    async def Moderation(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = modemb
        embed.set_footer(
            text="Requested by {}".format(interaction.author)
        )
        await interaction.send(embed=embed, ephemeral=True)
        
        
    @disnake.ui.button(label="Setup ⚙️", style=disnake.ButtonStyle.success, custom_id="setuphelp")
    async def Setup(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = setupemb
        embed.set_footer(
            text="Requested by {}".format(interaction.author)
        )
        await interaction.send(embed=embed, ephemeral=True)
        
        
    @disnake.ui.button(label="NSFW 🔞", style=disnake.ButtonStyle.success, custom_id="nsfwhelp")
    async def nsfw(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = nsfwemb  
        embed.set_footer(
            text="Requested by {}".format(interaction.author)
        )
        await interaction.send(embed=embed, ephemeral=True)
    
    
    @disnake.ui.button(label="Delete Interaction ❌", style=ButtonStyle.red, custom_id="deleteinter")
    async def first_button(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
      if not interaction.author:
         await interaction.send(msg="You must be the author to delete this message", ephemeral=True)
      else:
         await interaction.message.delete()
         
         
class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
       self.bot = bot
      
      
    @commands.slash_command(
        name="help",
        description="displays help command"
    )
    async def help(self, interaction: disnake.ApplicationCommandInteraction) -> None:  
        embed = disnake.Embed(
            description=f"Astral Bot - Coded, Maintained, Hosted, & Owned by <@935339228324311040>",
            color=color,
            timestamp=disnake.utils.utcnow()
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
            value=disnake.__version__,
            inline=False
        )
        embed.set_footer(
            text="Requested by {}".format(interaction.author)
        )
        values = psutil.virtual_memory()
        val2 = values.available * 0.001
        val3 = val2 * 0.001
        val4 = val3 * 0.001

        values2 = psutil.virtual_memory()
        value21 = values2.total
        values22 = value21 * 0.001
        values23 = values22 * 0.001
        values24 = values23 * 0.001
        embed.add_field(
            name='Hosting Stats', 
            value=f'Cpu usage- {psutil.cpu_percent(1)}%'
            f"\n(Actual Cpu Usage May Differ)"
            f"\n"
            f"\nNumber OF Cores - {psutil.cpu_count()}"
            f"\nNumber of Physical Cores- {psutil.cpu_count(logical=False)}"
            f"\n"
            f"\nTotal ram- {round(values24, 2)} GB"
            f"\nAvailable Ram - {round(val4, 2)} GB"
            )
        await interaction.send(embed=embed, view=HelpButtons())