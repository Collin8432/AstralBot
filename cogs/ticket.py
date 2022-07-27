"""
Contains the ticket command for the bot

Copyright 2022-Present Astral 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


import disnake
from disnake.ext import commands


from utils.color import color
 from utils.webhook import webhooksend



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
        await interaction.send(msg="Ticket Submitted Successfully!", ephemeral=True)
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
        await webhooksend(f"Ticket Created!", f"{interaction.author.mention} **Created A Ticket**\n**Reason:**\n{Reason}", f"{interaction.guild.id}")  


class Tickets(commands.Cog):
   def __init__(self, bot: commands.Bot):
      self.bot = bot
      
   
   @commands.slash_command(
      name="ticket",
      description="creates a ticket",
   )
   async def ticket(interaction):
        await interaction.send(modal=TicketReason())  
   