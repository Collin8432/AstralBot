
import json
import os
import platform
import random
import sys
from time import time
import datetime
from tkinter import N

import disnake
from disnake import ApplicationCommandInteraction
from disnake.ext import tasks, commands
from disnake.ext.commands import Bot
from disnake.ext.commands import Context
from discord_webhook import DiscordWebhook, DiscordEmbed
import traceback


from helpers import checks
import exceptions

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)

intents = disnake.Intents.default()

bot = Bot(command_prefix=config["prefix"], intents=intents)
token = config.get("token")

@bot.event
async def on_ready() -> None:
    status_task.start()


@tasks.loop(minutes=1.0)
async def status_task() -> None:
    statuses = ["astralsb.ga", "astral on top", "with you"]
    await bot.change_presence(activity=disnake.Game(random.choice(statuses)))

def load_commands(command_type: str) -> None:
    for file in os.listdir(f"./cogs/{command_type}"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cogs.{command_type}.{extension}")
                print(f"Loaded Extention {extension}")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")


if __name__ == "__main__":
    load_commands("general")
    load_commands("moderation")
    load_commands("fun")

@bot.event 
async def on_ready():
    print(f"Logged in as {bot.user}, Welcome!")
    status_task.start()

@bot.event
async def on_slash_command(interaction: Context):
    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/969975055704522814/9KxNw2MNN_tpUWFreon7k5V00f9v4sPxIQ9MJCVVFMhWOXzZy3TWwyNuZkhaoPBIaROG")
    embed = DiscordEmbed(title="Command Executed", color=0xDC143C)
    embed.set_description(f"**<@{interaction.author.id}>** Executed /**{interaction.data.name}** in <#{interaction.channel.id}>")
    webhook.add_embed(embed)
    response = webhook.execute()          

@bot.event
async def on_slash_command_error(interaction: ApplicationCommandInteraction, error: Exception) -> None:
    embed = disnake.Embed(
        title="Error",
        description=f"Error With Command:\n```py\n{error}```",
        color=0xDC143C
    )
    await interaction.edit_original_message(embed=embed, ephemeral=True)


whitelist = [938579223780655145]
@bot.listen('on_message')
async def on_message(message):
    if "code" in message.content:
        await message.reply(f"<@{message.author.id}> https://realms.gg/X7UmWxzws7O")
    if "nigger" in message.content and message.guild.id == 935632847547555920 and message.author.id not in whitelist:
        await message.reply("Please Don't Say That")
        await message.delete()
        webhook = DiscordWebhook(url="https://discord.com/api/webhooks/969975055704522814/9KxNw2MNN_tpUWFreon7k5V00f9v4sPxIQ9MJCVVFMhWOXzZy3TWwyNuZkhaoPBIaROG")
        embed = DiscordEmbed(title="N-Word Logged", color=0xDC143C)
        embed.set_description(f"<@{message.author.id}> Sent An N-Word In <#{message.channel.id}>\n **Content:** \n{message.content}")
        webhook.add_embed(embed)
        response = webhook.execute()      
    if message.channel.id == 957322698269278229 and message.author.id not in whitelist:
        await message.delete()
    if message.channel.id == 943425671101812767 and message.author.id not in whitelist:
        await message.author.edit(nick=f"{message.content}")
        embed = disnake.Embed(
            title=f"Nickname Changed!", 
            description=f"<@{message.author.id}> Changed Nickname To: {message.content}",
            color=0xDC143C
        )
        embed.set_image(url=message.author.avatar.url)
        await message.reply(embed=embed)


@bot.event
async def on_message_delete(message):
    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/969975055704522814/9KxNw2MNN_tpUWFreon7k5V00f9v4sPxIQ9MJCVVFMhWOXzZy3TWwyNuZkhaoPBIaROG")
    embed = DiscordEmbed(title="Message Deleted", color=0xDC143C)
    embed.set_description(f"<@{message.author.id}> Deleted A Chat In <#{message.channel.id}>\n **Content:** \n{message.content}")
    webhook.add_embed(embed)
    response = webhook.execute()      


# @bot.slash_command(
#     name="testembed",
#     description="Test Embed",
# )
# async def embed(interaction):
#     embed = disnake.Embed(
#         title="Embedtitle",
#         description="Embeddescription",
#         color=0xDC143C,
#         timestamp=datetime.datetime.now(),
#     )
#     embed.set_author(
#         name="Embedauthor",
#         url="https://store-Astral.tebex.io",
#         icon_url="https://cdn.discordapp.com/attachments/937106701063192677/960305394566176808/Astral.gif",
#     )
#     embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/937106701063192677/960305394566176808/Astral.gif")
#     embed.set_image(url="https://cdn.discordapp.com/attachments/937106701063192677/960305394566176808/Astral.gif")

#     embed.add_field(name="Regular Title", value="Regular Value", inline=False)

#     embed.add_field(name="Inline Title", value="Inline Value", inline=True)
#     embed.add_field(name="Inline Title", value="Inline Value", inline=True)
#     embed.add_field(name="Inline Title", value="Inline Value", inline=True)

#     embed.set_footer(
#         text="Embed Footer",
#         icon_url="https://cdn.discordapp.com/attachments/937106701063192677/960305394566176808/Astral.gif",
#     )
#     await interaction.send(embed=embed)


bot.run(config["token"])