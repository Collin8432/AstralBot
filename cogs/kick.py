"""
Contains kick command

Copyright 2022-Present Astral 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


# Imports
import disnake
from disnake.ext import commands
from disnake import ApplicationCommandInteraction


from utils.color import color
from utils.DeleteButton import DeleteButton
 

class Kick(commands.Cog, name="Mod Cmds"):
    def __init__(self, bot):
      self.bot = bot


    @commands.slash_command(
        name="kick",
        description="kicks a member from the server",
    )
    @commands.has_permissions(kick_members=True)
    async def kick(self, interaction: ApplicationCommandInteraction,
                   user: disnake.User,
                   reason: str = "Not specified") -> None:
        member = await interaction.guild.get_or_fetch_member(user.id)  
        if member.guild_permissions.administrator:  
            embed = disnake.Embed(
                title="Error!",
                description="**User has Admin permissions**",
                color=0xE02B2B,
                timestamp=disnake.utils.utcnow()
            )
            embed.set_footer(
                text="Requested by {}".format(interaction.author)
            )
            await interaction.send(embed=embed, view=DeleteButton())
        else:
            try:
                embed = disnake.Embed(
                    title="Member Kicked!",
                    description=f"**<@{member.id}> Was Kicked By <@{interaction.author.id}>\n**Reason:**\n{reason}**",  
                    color=color,
                    timestamp=disnake.utils.utcnow()
                )
                embed.set_footer(
                    text="Requested by {}".format(interaction.author)
                )
                await interaction.send(embed=embed, view=DeleteButton())
                try:
                    embed = disnake.Embed(
                        title="You Were Kicked!",
                        description=f"**You were Kicked by <@{interaction.author.id}>\n**Reason:**\n{reason}**",  
                        color=color,
                        timestamp=disnake.utils.utcnow()
                    )
                    embed.set_footer(
                        text="Requested by {}".format(interaction.author)
                    )
                    await member.send(embed=embed)  
                except disnake.Forbidden:
                    pass
                await member.kick(reason=reason)  
            except:
                embed = disnake.Embed(
                    title="Error!",
                    description="**Error While Kicking Member, Make Sure Member Does Not Have Higher Roles Than Me**",
                    color=color,
                    timestamp=disnake.utils.utcnow()
                )
                embed.set_footer(
                    text="Requested by {}".format(interaction.author)
                )
                await interaction.send(embed=embed, view=DeleteButton())