import json
import os
import random
import sys
import platform

import asyncio
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

class Counter(disnake.ui.View):


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
                        f"You Were Kicked From Astral By <@{interaction.author.id}>\n**Reason:**\n{reason}"
                    )
                except disnake.Forbidden:
                    pass
                await member.kick(reason=reason)
                webhook = DiscordWebhook(url="https://discord.com/api/webhooks/969975055704522814/9KxNw2MNN_tpUWFreon7k5V00f9v4sPxIQ9MJCVVFMhWOXzZy3TWwyNuZkhaoPBIaROG")
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
                        webhook = DiscordWebhook(url="https://discord.com/api/webhooks/969975055704522814/9KxNw2MNN_tpUWFreon7k5V00f9v4sPxIQ9MJCVVFMhWOXzZy3TWwyNuZkhaoPBIaROG")
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



    @commands.slash_command(
       name="ModeratorApplication",
       description="Sends A Moderator Appliction"
    )
    async def Appliction(interaction: disnake.CommandInteraction):
      await interaction.response.send_modal(modal=ModApp())



    @commands.slash_command(
        name="purge",
        description="Purges All Messages In A Server",
    )
    @commands.has_permissions(manage_messages=True)
    async def purge(interaction: disnake.CommandInteraction):
        await interaction.channel.purge(limit=9999999999999999999999999)
        await interaction.send("""Purge Complete, May Say ```The application did not respond```But It Should've Worked""", ephemeral=True)



def setup(bot):
    bot.add_cog(Moderation(bot))