
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
    statuses = ["With Astro", "With You", "/help", "With Humans"]
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
    status_task.start()

@bot.event
async def on_slash_command(interaction: ApplicationCommandInteraction) -> None:
    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/954798642043174982/R-YPK-tNPkfXKrMwamx1g1piJULf3Dq3tYfjwrHqrbni1DY1noBptL_Vu0gswktFAKAO")
    embed = DiscordEmbed(title="Command Executed", color=0xDC143C)
    embed.set_description(f"**<@{interaction.author.id}>** Executed **{interaction.data.name}** in <#{interaction.channel.id}>")
    webhook.add_embed(embed)
    response = webhook.execute()          

def fancy_traceback(exc: Exception) -> str:
    text = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))
    return f"```py\n{text[-4086:]}\n```"

@bot.event
async def on_command_error(self, ctx: commands.Context, error: commands.CommandError) -> None:
    embed = disnake.Embed(
        title=f"Command `{ctx.command}` failed due to `{error}`",
        description=fancy_traceback(error),
        color=disnake.Color.red(),
    )
    await ctx.send(embed=embed)

@bot.listen('on_message')
async def on_message(message):
    if "code" in message.content:
        await message.reply(f"<@{message.author.id}> https://realms.gg/X7UmWxzws7O")
    if "nigger" in message.content:
        await message.reply("Please Don't Say That")
        await message.delete()
        webhook = DiscordWebhook(url="https://discord.com/api/webhooks/954788066374078504/58vt7xjbtpWabo_ugmKdeW4cNsDBeivgdOwCn53KZ9q2H19jr6V2QU9nxBvp3TEF7qU2")
        embed = DiscordEmbed(title="N-Word Logged", color=0xDC143C)
        embed.set_description(f"<@{message.author.id}> Sent An N-Word In <#{message.channel.id}>\n **Content:** \n{message.content}")
        webhook.add_embed(embed)
        response = webhook.execute()      

@bot.event
async def on_message_delete(message):
    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/954802482104660008/oV8tTjVR7Ozt0sCI7rGMs1ArRtzouToY6VsACHsRKq91r446y-SL_YlVUhn82jSg-FOp")
    embed = DiscordEmbed(title="Message Deleted", color=0xDC143C)
    embed.set_description(f"<@{message.author.id}> Deleted A Chat In <#{message.channel.id}>\n **Content:** \n{message.content}")
    webhook.add_embed(embed)
    response = webhook.execute()      

         


bot.run(config["token"])