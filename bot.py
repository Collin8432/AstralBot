
import json
import os
import platform
import random
import sys

import disnake
from disnake import ApplicationCommandInteraction
from disnake.ext import tasks, commands
from disnake.ext.commands import Bot
from disnake.ext.commands import Context
from discord_webhook import DiscordWebhook, DiscordEmbed

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
    statuses = ["Newlife Realms", "Newlife is the Best Server"]
    await bot.change_presence(activity=disnake.Game(random.choice(statuses)))

def load_commands(command_type: str) -> None:
    for file in os.listdir(f"./cogs/{command_type}"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cogs.{command_type}.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")


if __name__ == "__main__":
    load_commands("general")
    load_commands("moderation")

@bot.event 
async def on_ready():
    print(f"Logged in as {bot.user}, Welcome!")

@bot.event
async def on_slash_command(interaction: ApplicationCommandInteraction) -> None:
    """
    The code in this event is executed every time a slash command has been *successfully* executed
    :param interaction: The slash command that has been executed.
    """
    print(
        f"Executed {interaction.data.name} command in {interaction.guild.name} (ID: {interaction.guild.id}) by {interaction.author} (ID: {interaction.author.id})")

@bot.event
async def on_slash_command_error(interaction: ApplicationCommandInteraction, error: Exception) -> None:
    if isinstance(error, exceptions.UserBlacklisted):
        embed = disnake.Embed(
            title="Error!",
            description="You are blacklisted from using the bot.",
            color=0xFF0000
        )
        print("A blacklisted user tried to execute a command.")
        return await interaction.send(embed=embed, ephemeral=True)
    elif isinstance(error, commands.errors.MissingPermissions):
        embed = disnake.Embed(
            title="Error!",
            description="You are missing the permission(s) `" + ", ".join(
                error.missing_permissions) + "` to execute this command!",
            color=0xFF0000
        )
        print("A blacklisted user tried to execute a command.")
        return await interaction.send(embed=embed, ephemeral=True)
    raise error

@bot.listen('on_message')
async def on_message(message):
    if "code" in message.content:
        await message.reply(f"<@{message.author.id}> https://realms.gg/X7UmWxzws7O")


@bot.listen('on_message')
async def on_message(message):
    if "nigger" or "nig" in message.content:
        await message.reply("Please Don't Say That")
        await message.delete()
        webhook = DiscordWebhook(url="https://discord.com/api/webhooks/954788066374078504/58vt7xjbtpWabo_ugmKdeW4cNsDBeivgdOwCn53KZ9q2H19jr6V2QU9nxBvp3TEF7qU2")
        embed = DiscordEmbed(title="N-Word Logged", color=0xDC143C)
        embed.set_description(f"**{message.author}** Sent An N-Word In <#{message.channel.id}>")
        webhook.add_embed(embed)
        response = webhook.execute()          


@bot.command(name="hook")
@checks.is_owner()
async def hook(interaction):
    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/954784175611871303/_vTyOlKL5HbKVJ2AkEOrENPjkC_8iy_T26z_b5MVV-WXHOF5jtru1986Aw0OTVgyPEqX")
    embed = DiscordEmbed(title='test', color=0xDC143C)
    embed.set_description("Hi")
    webhook.add_embed(embed)
    response = webhook.execute()                  


bot.run(config["token"])