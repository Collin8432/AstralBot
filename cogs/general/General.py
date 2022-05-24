import datetime
import os
import platform
import random

import disnake
from disnake import ApplicationCommandInteraction, Option, OptionType
from disnake.enums import ButtonStyle
from disnake.ext import commands
from disnake.ext.commands import Context
from helpers import checks
from helpers.ticketbutton import Ticketbutton
from helpers.webhook import webhooksend

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
            interaction.guild.get_role(972988909573242881): disnake.PermissionOverwrite(view_channel=False, send_messages=False, read_messages=False)
            }   
        )
        channel = ticketchannel 
        embed = disnake.Embed(
            title="Ticket Created!",
            description=f"{interaction.author.mention} **Created This Ticket**\n**Reason: **\n{Reason}",
            color=0xDC143C,
            timestamp=datetime.datetime.now()
        )
        await channel.send(embed=embed)
        await channel.send(view=Ticketbutton())
        await webhooksend(f"Ticket Created", f"{interaction.author.mention} **Created A Ticket**\n\n**Reason:**{Reason}")


class Buttons(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
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


   @commands.slash_command(
       name="ticket",
       description="Creates A Ticket",
   )
   @checks.not_blacklisted()
   async def ticket(interaction):
    await interaction.response.send_modal(modal=TicketReason())

    

   

def setup(bot):
    bot.add_cog(General(bot))

