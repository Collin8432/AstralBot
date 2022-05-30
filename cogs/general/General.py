import datetime
import os
import platform
import random
from unicodedata import category

import disnake
from disnake import ApplicationCommandInteraction, Option, OptionType
from disnake.enums import ButtonStyle
from disnake.ext import commands
from disnake.ext.commands import Context
from helpers import checks
from helpers.ticketbutton import Ticketbutton
from helpers.webhook import webhooksend
from helpers.helpembeds import helpemb, funemb, modemb

class TicketReason(disnake.ui.Modal):
    def __init__(self) -> None:
        components = [
            disnake.ui.TextInput(
                label="What is the reason for this ticket?",
                placeholder="Ex. I need help",
                custom_id="Reason",
                style=disnake.TextInputStyle.paragraph,
                min_length=5,
                max_length=500
            )
        ]
        super().__init__(title="Ticket Reason", custom_id="TicketReason", components=components)
    async def callback(self, interaction: disnake.ModalInteraction) -> None:
        global Reason
        Reason = interaction.text_values["Reason"]
        await interaction.response.send_message("Ticket Submitted Successfully!", ephemeral=True)
        ticketchannel = await interaction.guild.create_text_channel(
        name=f"ticket-{interaction.author.name}",
        overwrites={ 
            interaction.author: disnake.PermissionOverwrite(view_channel=True, send_messages=True, read_messages=True),
            interaction.guild.default_role: disnake.PermissionOverwrite(view_channel=False, send_messages=False, read_messages=False),
            # interaction: disnake.PermissionOverwrite(view_channel=False, send_messages=False, read_messages=False)
            }   
        )
        channel = ticketchannel 
        embed = disnake.Embed(
            title="Ticket Created!",
            description=f"{interaction.author.mention} **Created This Ticket**\n**Reason: **\n{Reason}",
            color=0xDC143C,
            timestamp=disnake.utils.utcnow()
        )
        await channel.send(embed=embed)
        await channel.send(view=Ticketbutton())
        await webhooksend(f"Ticket Created", f"{interaction.author.mention} **Created A Ticket**\n**Reason:**\n{Reason}")


class Buttons(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @disnake.ui.button(emoji="✅", style=ButtonStyle.green, custom_id="shutdowncomfirm")
    async def first_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.send_message("Exiting...")
        os._exit(0)
    @disnake.ui.button(emoji="⛔", style=ButtonStyle.red, custom_id="shutdowncancel")
    async def second_button(
        self, button: disnake.ui.button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.send_message("Cancelled!")
        await interaction.message.delete()


class HelpButtons(disnake.ui.View):
    def __init__(self):
        super().__init__()
        self.value = 0
    @disnake.ui.button(label="General ⚙️", style=disnake.ButtonStyle.success, custom_id="genhelp")
    async def General(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.send_message(embed=helpemb, ephemeral=True)
        self.value += 1
        if self.value == 3:
            self.stop()

    @disnake.ui.button(label="Fun 🎉", style=disnake.ButtonStyle.success)
    async def Fun(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction, custom_id="funhelp"):
        await interaction.response.send_message(embed=funemb, ephemeral=True)
        self.value += 1
        if self.value == 3:
            self.stop()

    @disnake.ui.button(label="Moderation 🚩", style=disnake.ButtonStyle.success)
    async def Moderation(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction, custom_id="modhelp"):
        await interaction.response.send_message(embed=modemb, ephemeral=True)
        self.value += 1
        if self.value == 3:
            self.stop()
            




class General(commands.Cog, name="General Cmds"):
   def __init__(self, bot):
      self.bot = bot
   
   

   @commands.slash_command(
      name="help",
      description="Displays Help Command"
   )
   @checks.not_blacklisted()
   async def help(interaction: ApplicationCommandInteraction) -> None:
      embed = disnake.Embed(
         description="Astral Bot - Coded by <@935339228324311040>",
         color=0xDC143C,
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
        value=f"{disnake.__version__}",
        inline=False
      )
      embed.set_footer(
         text=f"Requested by {interaction.author}"
      )
      await interaction.send(embed=embed, view=HelpButtons())


   @commands.slash_command(
        name="shutdown",
        description="Shuts The Bot Down.",
   )
   @checks.is_owner()
   async def shutdown(interaction):
      await interaction.send("Are You Sure?", view=Buttons())


   @commands.slash_command(
        name="randomchoice",
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


   @commands.slash_command(
       name="ticket",
       description="Creates A Ticket",
   )
   @checks.not_blacklisted()
   async def ticket(interaction):
    await interaction.response.send_modal(modal=TicketReason())

    
   @commands.slash_command(
        name="ping",
        description="Pings Bot Latency",
   )
   async def ping(interaction):
    latency = interaction.bot.latency * 1000
    pong = round(latency, 2)
    embed = disnake.Embed(
        title="Pong!",
        description=f"**Bot Latency:\n{pong} ms**",
        color=0xDC143C,
        timestamp=disnake.utils.utcnow()
    )
    await interaction.send(embed=embed)
    
   @commands.slash_command()
   async def invite(interaction):
       pass
    
   @invite.sub_command(
        name="link",
        description="Gets Invite Link To Astral's Discord Server",
   )
   async def link(interaction):
    embed = disnake.Embed(
        title="Invite Link",
        description=f"https://discord.gg/NdwvUHCDcM",
        color=0xDC143C,
        timestamp=disnake.utils.utcnow()
    )
    await interaction.send(embed=embed)
   @invite.sub_command(
        name="bot",
        description="Gets Invite Link To Astral Bot",
   )
   async def bot(interaction):
    embed = disnake.Embed(
        title="Invite Link",
        description=f"https://discord.com/api/oauth2/authorize?client_id=938579223780655145&permissions=8&scope=bot",
        color=0xDC143C,
        timestamp=disnake.utils.utcnow()
    )
    await interaction.send(embed=embed)


def setup(bot):
    bot.add_cog(General(bot))

