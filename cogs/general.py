# Imports
import os
import platform
import random
from typing import List



import disnake
from disnake import ApplicationCommandInteraction, Option, OptionType
from disnake.enums import ButtonStyle
from disnake.ext import commands



from helpers import checks
from helpers.webhook import webhooksend
from helpers.helpembeds import helpemb, funemb, modemb, setupemb, nsfwemb
from helpers.color import color
from helpers.message import interactionsend



global starttime
starttime = disnake.utils.utcnow()



# Class Paginator
class Paginator(disnake.ui.View):
    
    
    
    def __init__(self, embeds: List[disnake.Embed]):
        super().__init__(timeout=None)
        self.embeds = embeds
        self.embed_count = 0

        self.first_page.disabled = True
        self.prev_page.disabled = True

        for i, embed in enumerate(self.embeds):
            embed.set_footer(text=f"Page {i + 1} of {len(self.embeds)}")
    
    
    
    @disnake.ui.button(emoji="⏪", style=disnake.ButtonStyle.blurple)
    async def first_page(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        self.embed_count = 0
        embed = self.embeds[self.embed_count]
        embed.set_footer(text=f"Page 1 of {len(self.embeds)}")

        self.first_page.disabled = True
        self.prev_page.disabled = True
        self.next_page.disabled = False
        self.last_page.disabled = False
        await interaction.response.edit_message(embed=embed, view=self)



    @disnake.ui.button(emoji="◀", style=disnake.ButtonStyle.secondary)
    async def prev_page(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        self.embed_count -= 1
        embed = self.embeds[self.embed_count]

        self.next_page.disabled = False
        self.last_page.disabled = False
        if self.embed_count == 0:
            self.first_page.disabled = True
            self.prev_page.disabled = True
        await interaction.response.edit_message(embed=embed, view=self)



    @disnake.ui.button(emoji="❌", style=disnake.ButtonStyle.red)
    async def remove(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        await interaction.response.edit_message(view=None)



    @disnake.ui.button(emoji="▶", style=disnake.ButtonStyle.secondary)
    async def next_page(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        self.embed_count += 1
        embed = self.embeds[self.embed_count]

        self.first_page.disabled = False
        self.prev_page.disabled = False
        if self.embed_count == len(self.embeds) - 1:
            self.next_page.disabled = True
            self.last_page.disabled = True
        await interaction.response.edit_message(embed=embed, view=self)



    @disnake.ui.button(emoji="⏩", style=disnake.ButtonStyle.blurple)
    async def last_page(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        self.embed_count = len(self.embeds) - 1
        print(self.embeds[self.embed_count])
        embed = self.embeds[self.embed_count]

        self.first_page.disabled = False
        self.prev_page.disabled = False
        self.next_page.disabled = True
        self.last_page.disabled = True
        await interaction.response.edit_message(embed=embed, view=self)      
        


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
        await interactionsend(interaction=interaction, msg="Ticket Submitted Successfully!", ephemeral=True)
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
            text="Requested by {}".format(interaction.author)
        )
        await channel.send(embed=embed)
        await webhooksend(f"Ticket Created", f"{interaction.author.mention} **Created A Ticket**\n**Reason:**\n{Reason}", f"{interaction.guild.id}")  



# Shutdown View 
class Shutdown(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        
        
        
    @disnake.ui.button(emoji="✅", style=ButtonStyle.green, custom_id="shutdowncomfirm")
    async def Confirm(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interactionsend(interaction=interaction, msg="exiting...")
        os._exit(0)
        
        
        
    @disnake.ui.button(emoji="⛔", style=ButtonStyle.red, custom_id="shutdowncancel")
    async def Deny(
        self, button: disnake.ui.button, interaction: disnake.MessageInteraction  
    ):
        await interactionsend(interaction=interaction, msg="Cancelled")
        await interaction.message.delete()
        
        
        
    @disnake.ui.button(label="Delete Interaction ❌", style=ButtonStyle.red, custom_id="deleteinter")
    async def first_button(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
      if not interaction.author:
         await interactionsend(interaction=interaction, msg="You Must Be The Author To Delete The Interaction", ephemeral=True)
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
            text="Requested by {}".format(interaction.author)
        )
        await interactionsend(interaction=interaction, embed=embed, ephemeral=True)



    @disnake.ui.button(label="Fun 🎉", style=disnake.ButtonStyle.success, custom_id="funhelp")
    async def Fun(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = funemb
        embed.set_footer(
            text="Requested by {}".format(interaction.author)
        )   
        await interactionsend(interaction=interaction, embed=embed, ephemeral=True)



    @disnake.ui.button(label="Moderation 🚩", style=disnake.ButtonStyle.success, custom_id="modhelp")
    async def Moderation(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = modemb
        embed.set_footer(
            text="Requested by {}".format(interaction.author)
        )
        await interactionsend(interaction=interaction, embed=embed, ephemeral=True)
        
        
        
    @disnake.ui.button(label="Setup ⚙️", style=disnake.ButtonStyle.success, custom_id="setuphelp")
    async def Setup(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = setupemb
        embed.set_footer(
            text="Requested by {}".format(interaction.author)
        )
        await interactionsend(interaction=interaction, embed=embed, ephemeral=True)
        
        
        
    @disnake.ui.button(label="NSFW 🔞", style=disnake.ButtonStyle.success, custom_id="nsfwhelp")
    async def nsfw(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        embed = nsfwemb  
        embed.set_footer(
            text="Requested by {}".format(interaction.author)
        )
        await interactionsend(interaction=interaction, embed=embed, ephemeral=True)
    
    
    
    @disnake.ui.button(label="Delete Interaction ❌", style=ButtonStyle.red, custom_id="deleteinter")
    async def first_button(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
      if not interaction.author:
         await interactionsend(interaction=interaction, msg="You must be the author to delete this message", ephemeral=True)
      else:
         await interaction.message.delete()

            

# General Cog
class General(commands.Cog, name="General Cmds"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot  
   
   
   
    # Commands
    @commands.slash_command(
        name="help",
        description="displays help command"
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
            value=disnake.__version__,
            inline=False
        )
        embed.set_footer(
            text="Requested by {}".format(interaction.author)
         )
        await interactionsend(interaction=interaction, embed=embed, view=HelpButtons())

 

    @commands.slash_command(
        name="shutdown",
        description="shuts the bot down",
    )
    @checks.is_owner()
    async def shutdown(interaction):
        await interactionsend(interaction=interaction, msg="Are You Sure?", view=Shutdown())



    @commands.slash_command(
        name="randomchoice",
        description="picks a random choice out of 2 options",
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
            description=choicechoser,
            color=color
        )
        embed.set_footer(
            text="Requested by {}".format(interaction.author)
        )
        await interactionsend(interaction=interaction, embed=embed)



    @commands.slash_command(
       name="ticket",
       description="creates a ticket",
    )
    @checks.not_blacklisted()
    async def ticket(interaction):
        await interactionsend(interaction=interaction, modal=TicketReason())  

    

    @commands.slash_command(
        name="ping",
        description="pings bot latency",
    )
    async def ping(interaction):
        latency = interaction.bot.latency * 1000  
        pong = round(latency, 2)
        embed = disnake.Embed(
            title="Pong!",
            description="**Bot Latency:\n{} ms**".format(pong),
            color=color,
            timestamp=disnake.utils.utcnow()
        )
        embed.set_footer(
            text="Requested by {}".format(interaction.author)
        )
        await interactionsend(interaction=interaction, embed=embed)  
    


    @commands.slash_command(
        name="astral",
        description="support, invite, uptime, credits"
    )
    async def astral(self, interaction):
        pass


    
    @astral.sub_command(
        name="support",
        description="gets invite link to astral's discord server",
    )
    async def link(self, interaction):
        embed = disnake.Embed(
            title="Invite Link",
            description="https://discord.gg/NdwvUHCDcM",
            color=color,
            timestamp=disnake.utils.utcnow()
        )
        embed.set_footer(
            text=f"Requested by {interaction.author}"
        )
        await interactionsend(interaction=interaction, embed=embed)



    @astral.sub_command(
        name="invite",
        description="gets invite link to astral discord bot",
    )
    async def bot(self, interaction):
        embed = disnake.Embed(
            title="Invite Link",
            description="https://discord.com/api/oauth2/authorize?client_id=938579223780655145&permissions=8&scope=bot%20applications.commands",
            color=color,
            timestamp=disnake.utils.utcnow()
        )
        embed.set_footer(
            text="Requested by {}".replace(interaction.author)
        )
        await interactionsend(interaction=interaction, embed=embed)
        
        
    
    @astral.sub_command(
        name="uptime",
        description="shows the uptime of the bot",
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
            description="**The Bot Has Been Online For: {}**".format(uptime_str),
            color=color,
            timestamp=disnake.utils.utcnow(),
        ) 
        embed.set_footer(
            text="Requested by {}".format(interaction.author)
        )
        await interactionsend(interaction=interaction, embed=embed)
        
        
    
    @astral.sub_command(
        name="credits",
        description="shows credits for the bot",
    )
    @checks.not_blacklisted()
    async def credits(self, interaction):
        embed = disnake.Embed(
            title="Credits",
            description=f"**Astral Bot**\n[**Disnake - Discord API Wrapper**](https://disnake.dev)\n[**Original Template - Credits To kkrypt0nn**](https://github.com/kkrypt0nn/Python-Discord-Bot-Template)\n**Coded By <@935339228324311040>**",
            color=color,
            timestamp=disnake.utils.utcnow()
        )
        embed.set_footer(
            text="Requested by {}".format(interaction.author)
        )
        await interactionsend(interaction=interaction, embed=embed)
        
        
        
    @commands.slash_command(
        name="allcmds",
        description="all commands"
    )
    async def allcmds(self,  interaction):
        embeds = [
             disnake.Embed(
                title="Commands Page 1",
                description="",
                color=color,
                timestamp=disnake.utils.utcnow(),
            ),
            disnake.Embed(
                title="Commands Page 2",
                description="",
                color=color,
                timestamp=disnake.utils.utcnow(),
            ),
            disnake.Embed(
                title="Commands Page 3",
                description="",
                color=color,
                timestamp=disnake.utils.utcnow()
            ),
        ]
        s = list(self.bot.slash_commands)
        for cmd in s[:12]:  
            embeds[0].add_field(name=f"{cmd.name}", value=f"{cmd.description}", inline=True)
        for cmd in s[13:25]:
            embeds[1].add_field(name=f"{cmd.name}", value=f"{cmd.description}", inline=True)
        for cmd in s[26:]:
            embeds[2].add_field(name=f"{cmd.name}", value=f"{cmd.description}", inline=True)
        await interactionsend(interaction=interaction, embed=embeds[0], view=Paginator(embeds))
