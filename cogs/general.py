# Imports
import os
import platform
import random



import disnake
from disnake import ApplicationCommandInteraction, Option, OptionType
from disnake.enums import ButtonStyle
from disnake.ext import commands



from helpers import checks
from helpers.webhook import webhooksend
from helpers.helpembeds import helpemb, funemb, modemb, setupemb
from helpers.deleteinteraction import deleteinteraction
from helpers.color import color



global starttime
starttime = disnake.utils.utcnow()



# TicketReason Modal
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
            }   
        )
        channel = ticketchannel 
        embed = disnake.Embed(
            title="Ticket Created!",
            description=f"{interaction.author.mention} **Created This Ticket**\n**Reason: **\n{Reason}",
            color=color,
            timestamp=disnake.utils.utcnow()
        )
        embed.set_footer(
            text=f"Requested by {interaction.author}"
        )
        await channel.send(embed=embed)
        await webhooksend(f"Ticket Created", f"{interaction.author.mention} **Created A Ticket**\n**Reason:**\n{Reason}")  



# Shutdown View 
class Shutdown(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    @disnake.ui.button(emoji="✅", style=ButtonStyle.green, custom_id="shutdowncomfirm")
    async def Confirm(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.send_message("Exiting...")
        os._exit(0)
    @disnake.ui.button(emoji="⛔", style=ButtonStyle.red, custom_id="shutdowncancel")
    async def Deny(
        self, button: disnake.ui.button, interaction: disnake.MessageInteraction  
    ):
        await interaction.response.send_message("Cancelled!")
        await interaction.message.delete()
    @disnake.ui.button(label="Delete Interaction ❌", style=ButtonStyle.red, custom_id="deleteinter")
    async def first_button(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
      if not interaction.author:
         await interactionsend(interaction, "You Must Be The Author To Delete The Interaction", ephemeral=True)
      else:
         await interaction.message.delete()



# HelpButtons View
class HelpButtons(disnake.ui.View):
    def __init__(self):
        super().__init__()
        self.value = 0
    @disnake.ui.button(label="General ⚙️", style=disnake.ButtonStyle.success, custom_id="genhelp")
    async def General(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = helpemb
        embed.set_footer(
            text=f"Requested by {interaction.author}"
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)


    @disnake.ui.button(label="Fun 🎉", style=disnake.ButtonStyle.success, custom_id="funhelp")
    async def Fun(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = funemb
        embed.set_footer(
            text=f"Requested by {interaction.author}"
        )   
        await interaction.response.send_message(embed=embed, ephemeral=True)


    @disnake.ui.button(label="Moderation 🚩", style=disnake.ButtonStyle.success, custom_id="modhelp")
    async def Moderation(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = modemb
        embed.set_footer(
            text=f"Requested by {interaction.author}"
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)
        
    @disnake.ui.button(label="Setup ⚙️", style=disnake.ButtonStyle.success, custom_id="setuphelp")
    async def Setup(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = setupemb
        embed.set_footer(
            text=f"Requested by {interaction.author}"
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)
    
    @disnake.ui.button(label="Delete Interaction ❌", style=ButtonStyle.red, custom_id="deleteinter")
    async def first_button(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
      if not interaction.author:
         await interactionsend(interaction, "You Must Be The Author To Delete The Interaction", ephemeral=True)
      else:
         await interaction.message.delete()

            

# General Cog
class General(commands.Cog, name="General Cmds"):
    def __init__(self, bot):
        self.bot = bot  
   
   
    # Commands
    @commands.slash_command(
        name="help",
        description="Displays Help Command"
    )
    @checks.not_blacklisted()
    async def help(self, interaction: ApplicationCommandInteraction) -> None:  
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
            value=f"{disnake.__version__}",
            inline=False
        )
        embed.set_footer(
            text=f"Requested by {interaction.author}"
         )
        await interactionsend(interaction, embed=embed, view=HelpButtons())

 

    @commands.slash_command(
        name="shutdown",
        description="Shuts The Bot Down.",
    )
    @checks.is_owner()
    async def shutdown(interaction):
        await interactionsend(interaction, "Are You Sure?", view=Shutdown())



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
            color=color
        )
        embed.set_footer(
            text=f"Requested by {interaction.author}"
        )
        await interactionsend(interaction, embed=embed, view=deleteinteraction())



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
            color=color,
            timestamp=disnake.utils.utcnow()
        )
        embed.set_footer(
            text=f"Requested by {interaction.author}"
        )
        await interactionsend(interaction, embed=embed, view=deleteinteraction())  
    


    @commands.slash_command(
        name="astral",
        description="support, invite, uptime, credits"
    )
    async def astral(self, interaction):
        pass


    
    @astral.sub_command(
        name="support",
        description="Gets Invite Link To Astral's Discord Server",
    )
    async def link(self, interaction):
        embed = disnake.Embed(
            title="Invite Link",
            description=f"https://discord.gg/NdwvUHCDcM",
            color=color,
            timestamp=disnake.utils.utcnow()
        )
        embed.set_footer(
            text=f"Requested by {interaction.author}"
        )
        await interactionsend(interaction, embed=embed, view=deleteinteraction())



    @astral.sub_command(
        name="invite",
        description="Gets Invite Link To Astral Bot",
    )
    async def bot(self, interaction):
        embed = disnake.Embed(
            title="Invite Link",
            description=f"https://discord.com/api/oauth2/authorize?client_id=938579223780655145&permissions=8&scope=bot%20applications.commands",
            color=color,
            timestamp=disnake.utils.utcnow()
        )
        embed.set_footer(
            text=f"Requested by {interaction.author}"
        )
        await interactionsend(interaction, embed=embed, view=deleteinteraction())
        
        
    
    
    @astral.sub_command(
        name="uptime",
        description="Shows the uptime of the bot",
    )
    @checks.not_blacklisted()
    async def uptime(self, interaction):
        end_time = disnake.utils.utcnow()
        diff = end_time - starttime
        seconds = diff.seconds % 60
        minutes = (diff.seconds // 60) % 60
        hours = (diff.seconds // 3600) % 24
        days = diff.days
        uptime_str = f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
        embed = disnake.Embed(
            title="Uptime",
            description=f"**The Bot Has Been Online For: {uptime_str}**",
            color=color,
            timestamp=disnake.utils.utcnow(),
        ) 
        embed.set_footer(
            text=f"Requested by {interaction.author}"
        )
        await interactionsend(interaction, embed=embed, view=deleteinteraction())
        
        
    
    @astral.sub_command(
        name="credits",
        description="Shows Credits For The Bot",
    )
    @checks.not_blacklisted()
    async def credits(self, interaction):
        embed = disnake.Embed(
            title="Credits",
            description=f"**Astral Bot**\n[**Disnake - Discord API Wrapper**](https://disnake.dev)\n[**Original Template - Credits To kkrypt0nn**](https://github.com/kkrypt0nn/Python-Discord-Bot-Template)\n**Coded By <@935339228324311040>**",
        )
        embed.set_footer(
            text=f"Requested by {interaction.author}"
        )
        await interactionsend(interaction, embed=embed, view=deleteinteraction())
        
        
        
    @commands.slash_command(
        name="allcmds",
        description="all commands"
    )
    async def allcmds(self, interaction):
        embed = disnake.Embed(
            title="All Commands",
            color=color,
            timestamp=disnake.utils.utcnow(),
        )
        for cmd in self.bot.slash_commands:
            embed.add_field(
                name=f"/{cmd.name}",
                value=f"{cmd.description}",
                inline=False,
            )
        embed.set_footer(
            text=f"Total of {len(self.bot.slash_commands)} commands",
        )
        await interactionsend(interaction, embed=embed, view=deleteinteraction())
    
    
    
    # @commands.slash_command(
    #     name="serverinfo",
    #     description="displays server info",
    # )
    # async def info(self, interaction: ApplicationCommandInteraction):
    #     nitrotype = interaction.author.premium_type   
         
    


# Adding Cog To Bot 
def setup(bot):
    bot.add_cog(General(bot))

