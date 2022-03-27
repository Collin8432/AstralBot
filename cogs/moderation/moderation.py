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
from discord_webhook import DiscordWebhook, DiscordEmbed
import disnake
from disnake import ApplicationCommandInteraction, Option, OptionType
from disnake.ext import commands

from helpers import checks

class Counter(disnake.ui.View):

    # Define the actual button
    # When pressed, this increments the number displayed until it hits 5.
    # When it hits 5, the counter button is disabled and it turns green.
    # note: The name of the function does not matter to the library
    @disnake.ui.button(label="0", style=disnake.ButtonStyle.red)
    async def count(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        number = int(button.label) if button.label else 0
        if number + 1 >= 5:
            button.style = disnake.ButtonStyle.green
            button.disabled = True
        button.label = str(number + 1)

        # Make sure to update the message with our updated selves
        await interaction.response.edit_message(view=self)





class Moderation(commands.Cog, name="Mod Cmds"):
    def __init__(self, bot):
      self.bot = bot

    @commands.slash_command(
        name="Kick",
        description="Kicks A Member From The Server",
        options=[
            Option(
                name="user",
                description="The Member You Want To Kick",
                type=OptionType.user,
                required=True
            ),
            Option(
                name="reason",
                description="Reason To Kick Member",
                type=OptionType.string,
                required=False
            )
        ]
    )
    @commands.has_permissions(kick_members=True)
    @checks.not_blacklisted()
    async def kick(self, interaction: ApplicationCommandInteraction, user: disnake.User,
                   reason: str = "Not specified") -> None:
        member = await interaction.guild.get_or_fetch_member(user.id)
        if member.guild_permissions.administrator:
            embed = disnake.Embed(
                title="Error!",
                description="User has Admin permissions.",
                color=0xE02B2B
            )
            await interaction.send(embed=embed)
        else:
            try:
                embed = disnake.Embed(
                    title="Member Kicked",
                    description=f"<@{member.id}> Was Kicked By <@{interaction.author.id}>\n**Reason:**\n{reason}",
                    color=0xDC143C
                )
                await interaction.send(embed=embed)
                try:
                    await member.send(
                        f"You Were Kicked From Newlife By <@{interaction.author.id}>\n**Reason:**\n{reason}"
                    )
                except disnake.Forbidden:
                    pass
                await member.kick(reason=reason)
                webhook = DiscordWebhook(url="https://discord.com/api/webhooks/955273637206843432/TjG_TW6lfl3rrenI9JK5KkFen9qtel4uP3aerV0YTWqkRzkQHMY86NEfSpptEQxai0Pz")
                embed = DiscordEmbed(title="Member Kicked!", color=0xDC143C)
                embed.set_description(f"**{member}** Was Kicked By <@{interaction.author.id}>\n**Reason:**\n{reason}")
                webhook.add_embed(embed)
                response = webhook.execute()     
            except:
                embed = disnake.Embed(
                    title="Error",
                    description="Error While Kicking Member, Make Sure Member Does Not Have Higher Roles Than Me",
                    color=0xDC143C
                )
                await interaction.send(embed=embed)
    @commands.slash_command(
        name="Ban",
        description="Bans A Member From The Server",
        options=[
            Option(
                name="user",
                description="The Member You Want To Ban",
                type=OptionType.user,
                required=True
            ),
            Option(
                name="reason",
                description="Reason To Ban Member",
                type=OptionType.string,
                required=False
            )
        ]
    )
    @commands.has_permissions(ban_members=True)
    @checks.not_blacklisted()
    async def ban(self, interaction: ApplicationCommandInteraction, user: disnake.User,
                  reason: str = "Not specified") -> None:
                  member = await interaction.guild.get_or_fetch_member(user.id)
                  if member.guild_permissions.administrator:
                      embed = disnake.Embed(
                          title="Error!",
                          description="User Has Administrator Permissions",
                          color=0xDC143C
                      )
                      await interaction.send(embed=embed)
                  else:
                      try:
                        embed = disnake.Embed(
                            title="Member Banned",
                            description=f"<@{member.id}> Was Banned By <@{interaction.author.id}>\n**Reason:**\n{reason}",
                            color=0xDC143C
                        )
                        await interaction.send(embed=embed)
                        try:
                            embed = disnake.Embed(
                            title="You Were Banned!",
                            description=f"<@{member.id}> Was Banned By <@{interaction.author.id}>\n**Reason:**\n{reason}",
                            color=0xDC143C
                            )
                            await member.send(embed=embed)
                        except disnake.Forbidden:
                            pass
                        await member.ban(reason=reason)
                        webhook = DiscordWebhook(url="https://discord.com/api/webhooks/954803072096436255/scSHea18bR_vByOrlJSTEy-8yi0paqITg34YGPLmm6O762cdFQx1xdiz9MYccquf7vgz")
                        embed = DiscordEmbed(title="Member Banned!", color=0xDC143C)
                        embed.set_description(f"**{member}** Was Banned By <@{interaction.author.id}>\n**Reason:**\n{reason}")
                        webhook.add_embed(embed)
                        response = webhook.execute()     
                      except:
                          embed = disnake.Embed(
                              title="Error!",
                              description="Error While Banning Member, Make Sure Member Does Not Have Higher Roles Than Me",
                              color=0xDC143C
                          )

    @commands.slash_command(
        name="testcommand",
        description="This is a testing command that does nothing.",
    )
    @checks.not_blacklisted()
    @checks.is_owner()
    async def testcommand(self, interaction: ApplicationCommandInteraction):
        await interaction.send("This is a testing command that does nothing.", view=Counter(), ephemeral=True)
def setup(bot):
    bot.add_cog(Moderation(bot))