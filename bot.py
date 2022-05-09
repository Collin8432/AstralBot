
import json
import os
import random
import sys
from time import time
import datetime
from colorama import Fore
import random
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import disnake
from disnake import ApplicationCommandInteraction
from disnake.ext import tasks, commands
from disnake.ext.commands import Bot
from disnake.ext.commands import Context
from discord_webhook import DiscordWebhook, DiscordEmbed
import asyncio


from helpers import checks
import exceptions

if not os.path.isfile("config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("config.json") as file:
        config = json.load(file)

intents = disnake.Intents.default()
intents.members = True

bot = Bot(command_prefix=config["prefix"], intents=intents)
token = config.get("token")


    


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
                print(f"Loaded (/) {extension} Commands")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")


if __name__ == "__main__":
    load_commands("general")
    load_commands("moderation")
    load_commands("fun")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ")
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
        color=0xDC143C,
        timestamp=datetime.datetime.now()
    )
    try:
        await interaction.edit_original_message(embed=embed, ephemeral=True)
    except:
        print(f"\n\n{error}")

whitelist = [938579223780655145]
@bot.listen('on_message')
async def on_message(message):
    if "code" in message.content:
        await message.reply(f"<@{message.author.id}> https://realms.gg/X7UmWxzws7O")
    if "nigger" in message.content and message.guild.id == 944297787779072020 and message.author.id not in whitelist:
        await message.reply("Please Don't Say That")
        await message.delete()
        webhook = DiscordWebhook(url="https://discord.com/api/webhooks/969975055704522814/9KxNw2MNN_tpUWFreon7k5V00f9v4sPxIQ9MJCVVFMhWOXzZy3TWwyNuZkhaoPBIaROG")
        embed = DiscordEmbed(title="N-Word Logged", color=0xDC143C)
        embed.set_description(f"<@{message.author.id}> Sent An N-Word In <#{message.channel.id}>\n **Content:** \n{message.content}")
        webhook.add_embed(embed)
        response = webhook.execute()
    if message.channel.id == 970325969359503460 and message.author.id not in whitelist:
        await message.author.edit(nick=f"{message.content}")
        embed = disnake.Embed(
            title=f"Nickname Changed!",
            description=f"<@{message.author.id}> Changed Nickname To: {message.content}",
            color=0xDC143C,
            timestamp=datetime.datetime.now()
        )
        embed.set_image(url=message.author.display_avatar)
        await message.reply(embed=embed)

@bot.event
async def on_message_delete(message):
    webhook = DiscordWebhook(url="https://discord.com/api/webhooks/969975055704522814/9KxNw2MNN_tpUWFreon7k5V00f9v4sPxIQ9MJCVVFMhWOXzZy3TWwyNuZkhaoPBIaROG")
    embed = DiscordEmbed(title="Message Deleted", color=0xDC143C)
    embed.set_description(f"<@{message.author.id}> Deleted A Chat In <#{message.channel.id}>\n **Content:** \n{message.content}")
    webhook.add_embed(embed)
    response = webhook.execute()

@bot.event
async def on_user_update(before, after):
    if before.discriminator != after.discriminator:
        webhook = DiscordWebhook(url="https://discord.com/api/webhooks/969975055704522814/9KxNw2MNN_tpUWFreon7k5V00f9v4sPxIQ9MJCVVFMhWOXzZy3TWwyNuZkhaoPBIaROG")
        embed = DiscordEmbed(title="User Discriminator Changed", color=0xDC143C)
        embed.set_description(f"<@{after.id}> Changed Discriminator From {before.discriminator} To {after.discriminator}")
        webhook.add_embed(embed)
        response = webhook.execute()
    if before.username != after.username:
        webhook = DiscordWebhook(url="https://discord.com/api/webhooks/969975055704522814/9KxNw2MNN_tpUWFreon7k5V00f9v4sPxIQ9MJCVVFMhWOXzZy3TWwyNuZkhaoPBIaROG")
        embed = DiscordEmbed(title="User Nickname Changed", color=0xDC143C)
        embed.set_description(f"<@{after.id}> Changed Nickname From {before.username} To {after.username}")
        webhook.add_embed(embed)
        response = webhook.execute()
    if before.avatar != after.avatar:
        webhook = DiscordWebhook(url="https://discord.com/api/webhooks/969975055704522814/9KxNw2MNN_tpUWFreon7k5V00f9v4sPxIQ9MJCVVFMhWOXzZy3TWwyNuZkhaoPBIaROG")
        embed = DiscordEmbed(title="User Avatar Changed", color=0xDC143C)
        embed.set_description(f"<@{after.id}> Changed Avatar From {before.avatar} To {after.avatar}")
        webhook.add_embed(embed)
        response = webhook.execute()

@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        img = Image.open("astral.png")
        image = ImageDraw.Draw(img)
        font = ImageFont.truetype("MomB.ttf", 30)
        image.text((160, 275), f"Welcome,", font=font, fill=(43,22,197))
        image.text((160, 325), f"{member.name}", font=font, fill=(43,22,197))
        list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        randomnumber = ""
        for i in range(5, 15):
            randomnumber += (random.choice(list))
            continue
        img.save(f"astral{randomnumber}.png")
        imgfile = disnake.File(f"astral{randomnumber}.png") 
        # embed = disnake.Embed(
        #     title="Member Joined",
        #     color=0xDC143C,
        #     timestamp=datetime.datetime.now()
        # )
        # embed.set_image(imgfile)
        await guild.system_channel.send(file=imgfile)


async def checker(filename):
    def check(message):
        return message.content == filename.upper() or message.content == filename.lower()
    await bot.wait_for("message", check=check)
    
verifychannel = [972679418763935794]
@bot.slash_command(
    name="Verify",
    description="Verify yourself to gain access to the server"
)
async def verify(interaction):
    if interaction.channel.id not in verifychannel:
        await interaction.send("You can only use this command in <#972679418763935794>")
    else:
        list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        FFileName = ""
        for i in range(5, 15):
            FFileName += (random.choice(list))
            continue
        print(f"{FFileName}")
        img = Image.open('astral.png')

        I1 = ImageDraw.Draw(img)
        
        font = ImageFont.truetype("MomB.ttf", 30)
        I1.text((150, 275), f"{FFileName}", fill=(32,22,197), font=font)
        I1.text((125, 300), f"Please enter the", fill=(43,22,197), font=font)
        I1.text((125, 325), f"letters/numbers", fill=(43,22,197), font=font)
        I1.text((75, 350), f"above to gain access", fill=(43,22,197), font=font)
        I1.text((150, 375), f"to Astral", fill=(43,22,197), font=font)
        img.save(f"astral{FFileName}.png")
        await interaction.send(file=disnake.File(f"astral{FFileName}.png"))
        try:
            await checker(f"{FFileName}")
        except:
            print("fail")
        await interaction.author.add_roles(disnake.Object(972988909573242881))


bot.run(config["token"])