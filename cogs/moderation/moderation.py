import json
import os
import random
import sys
import platform

import aiohttp
import datetime
import disnake
from disnake.ext import commands
from disnake.ext.commands import Context
from disnake import ApplicationCommandInteraction, Option, OptionType
from disnake.enums import ButtonStyle
from disnake.ext import commands
import disnake
from disnake import ApplicationCommandInteraction, Option, OptionType
from disnake.ext import commands

from helpers import checks
from helpers.webhook import webhooksend

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
                placeholder="Ex. Discord",
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
        await webhooksend("New Application", f"<@{interaction.author.id}> Submitted This Application \n**Appplying For:**\n{ApplyingFor}\n**Experience:**\n{Experience}\n**Why Are You Better Than Others For Your Role:**\n{BR}")
        await interaction.response.send_message("Application Submitted Successfully!", ephemeral=True)
    async def on_error(self, error: Exception, inter: disnake.ModalInteraction) -> None:
        await inter.response.send_message("Error In Modal Interaction, {error}", ephemeral=True)





class Moderation(commands.Cog, name="Mod Cmds"):
    def __init__(self, bot):
      self.bot = bot

    @commands.slash_command(
        name="kick",
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
                color=0xE02B2B,
                timestamp=disnake.utils.utcnow()
            )
            await interaction.send(embed=embed)
        else:
            try:
                embed = disnake.Embed(
                    title="Member Kicked",
                    description=f"<@{member.id}> Was Kicked By <@{interaction.author.id}>\n**Reason:**\n{reason}",
                    color=0xDC143C,
                    timestamp=disnake.utils.utcnow()
                )
                await interaction.send(embed=embed)
                try:
                    embed = disnake.Embed(
                    title="You Were Kicked!",
                    description=f"<@{member.id}> Was Kicked By <@{interaction.author.id}>\n**Reason:**\n{reason}",
                    color=0xDC143C,
                    timestamp=disnake.utils.utcnow()
                    )
                    await member.send(embed=embed)
                except disnake.Forbidden:
                    pass
                await member.kick(reason=reason)
            except:
                embed = disnake.Embed(
                    title="Error",
                    description="Error While Kicking Member, Make Sure Member Does Not Have Higher Roles Than Me",
                    color=0xDC143C,
                    timestamp=disnake.utils.utcnow()
                )
                await interaction.send(embed=embed)
    @commands.slash_command(
        name="ban",
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
                          color=0xDC143C,
                          timestamp=disnake.utils.utcnow()
                      )
                      await interaction.send(embed=embed)
                  else:
                      try:
                        embed = disnake.Embed(
                            title="Member Banned",
                            description=f"<@{member.id}> Was Banned By <@{interaction.author.id}>\n**Reason:**\n{reason}",
                            color=0xDC143C,
                            timestamp=disnake.utils.utcnow()
                        )
                        await interaction.send(embed=embed)
                        await member.ban(reason=reason)
                      except:
                          embed = disnake.Embed(
                              title="Error!",
                              description="Error While Banning Member, Make Sure Member Does Not Have Higher Roles Than Me",
                              color=0xDC143C,
                              timestamp=disnake.utils.utcnow()
                          )




    @commands.slash_command(
       name="moderatorapplication",
       description="Sends A Moderator Appliction"
    )
    async def Appliction(interaction: disnake.CommandInteraction):
      await interaction.response.send_modal(modal=ModApp())



    @commands.slash_command(
        name="purge",
        description="Purges All Messages In A Channel",
    )
    @commands.has_permissions(manage_messages=True)
    async def purge(interaction: disnake.CommandInteraction):
        embed = disnake.Embed(
            title="Messages Purged",
            description="Purged All Messages In This Channel",
            color=0xDC143C,
            timestamp=disnake.utils.utcnow()
        )
        await interaction.send(embed=embed, ephemeral=True)
        await interaction.channel.purge(limit=200)


    @commands.slash_command(
        name="rules",
        description="Sends The Rules",
    )
    @commands.has_permissions(administrator=True)
    async def rules(interaction):
        embed = disnake.Embed(
            title="Astral Rules",
            description="1. Dont Be Annoying\n2. Dont Ask For Free Shit/Mod\n3. Be Smart With What You Say And Do\n4. Please Be Kind And Follow Discord TOS",
            color=0xDC143C,
            timestamp=disnake.utils.utcnow()
        )
        await interaction.send(embed=embed)
def setup(bot):
    bot.add_cog(Moderation(bot))