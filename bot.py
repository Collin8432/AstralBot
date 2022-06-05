# Imports
import json
import os
import random
from re import X
import sys


import disnake
from disnake import ApplicationCommandInteraction, Option, OptionType
from disnake.ext import tasks, commands
from disnake.ext.commands import Bot



from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont



from helpers.webhook import webhooksend
from helpers.helpembeds import helpemb, funemb, modemb
from helpers.database import webhook_add, verification_add, memberchannel_add, muterole_add, serversearch, verification_search, verifyrole_add, verifyrole_search
from helpers import checks



# Setting Up Bot
if not os.path.isfile("./secret/config.json"):
    sys.exit("'config.json' not found! Please add it and try again.")
else:
    with open("./secret/config.json") as file:
        config = json.load(file)



intents = disnake.Intents.all()
bot = Bot(command_prefix=config["prefix"], intents=intents)
token = config.get("token")



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
    load_commands("listeners")
    global start_time
    start_time = disnake.utils.utcnow()



# Tasks and Special Events
@tasks.loop(minutes=1.0)
async def status_task() -> None:
    statuses = [f"Watching Over {len(bot.guilds)} Servers"]
    await bot.change_presence(activity=disnake.Game(random.choice(statuses)))
    # for guild in bot.guilds:
    #     channel1 = await memberchannel_search(f"{guild.id}")
    #     if channel1 is not None:    
    #         members = guild.member_count
    #         ch = bot.get_channel(channel1)
    #         try:
    #             await ch.edit(name=f"Members: {members}")
    #         except:
    #             pass



@bot.event
async def on_ready():
    await status_task.start()



@bot.event
async def on_button_click(interaction):
    custom_id=interaction.component.custom_id
    if custom_id == "pingstaff":
        pingrole = interaction.guild.get_member(935339228324311040)
        await interaction.send(pingrole.mention)
    elif disnake.errors.HTTPException:
        pass
    elif custom_id == "deletechannel":
        print("fde")
        await interaction.channel.delete()
    elif custom_id == "nerd":
        await interaction.send("nerd")
    elif custom_id == "balls":
        await interaction.send("balls")
    elif custom_id == "shutdownconfirm":
        await interaction.send("Exiting...")
        await os._exit(0)
    elif custom_id == "shutdowncancel":
        await interaction.send("Cancelled!")
        await interaction.message.delete()
    elif custom_id == "genhelp":
        await interaction.send(embed=helpemb, ephemeral=True)
    elif custom_id == "modhelp":
        await interaction.send(embed=modemb, ephemeral=True)
    elif custom_id == "funhelp":
        await interaction.send(embed=funemb, ephemeral=True)
    else:
        pass



# Slash commands
@bot.slash_command(
    name="uptime",
    description="Shows the uptime of the bot",
)
@checks.not_blacklisted()
async def uptime(interaction):
    end_time = disnake.utils.utcnow()
    diff = end_time - start_time
    seconds = diff.seconds % 60
    minutes = (diff.seconds // 60) % 60
    hours = (diff.seconds // 3600) % 24
    days = diff.days
    uptime_str = f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
    embed = disnake.Embed(
        title="Uptime",
        description=f"**The Bot Has Been Online For: {uptime_str}**",
        color=0xDC143C,
        timestamp=disnake.utils.utcnow(),
    ) 
    await interaction.send(embed=embed)



@bot.slash_command(
    name="setverification",
    description="Sets the verification channel",
)
@commands.has_permissions(administrator=True)
@checks.not_blacklisted()
async def setverification(interaction):
    await verification_add(f"{interaction.guild.id}", f"{interaction.channel.id}")
    await interaction.send("Verification Channel Set!", ephemeral=True)



@bot.slash_command(
    name="setmembervoicechannel",
    description="Sets the member voice channel",
)
@commands.has_permissions(administrator=True)
@checks.not_blacklisted()
async def setmembervoicechannel(interaction):
    await memberchannel_add(f"{interaction.guild.id}", f"{interaction.channel.id}")
    await interaction.send("Member Voice Channel Set!", ephemeral=True)



@bot.slash_command(
    name="database",
    description="Searches for servers db settings",
)
@commands.has_permissions(administrator=True)
@checks.not_blacklisted()
async def serversearchs(interaction: disnake.ApplicationCommandInteraction) -> None:
    results = await serversearch(f"{interaction.guild.id}")  
    for result in results:
        name: str = result["guild_name"]
        guildid: int = result["guild_id"]
        webhook: str = result["webhook"]
        memberchannel: int = result["memberchannel"]
        verificationchannel: int = result["verification"]
        muterole: int = result["muterole"]
        verifyrole: int = result["verifyrole"]
    embed = disnake.Embed(
        title=f"Server Database",
        description=f"🟥DO NOT SHARE THIS INFORMATION🟥\n**Guild Name:**\n{name}\n**Guild ID:**\n{guildid}\n**Webhook:**\n{webhook}\n**Member Channel:**\n{memberchannel}\n**Verification Channel:**\n{verificationchannel}\n**Mute Role:**\n{muterole}\n**Verify Role:**\n{verifyrole}",  
        color=0xDC143C,
        timestamp=disnake.utils.utcnow()
    )
    await interaction.send(embed=embed, ephemeral=True)



async def Checker(filename):
    def check(message):
        return message.content == filename.upper() or message.content == filename.lower()
    await bot.wait_for("message", check=check)

    

@bot.slash_command(
    name="verify",
    description="Verify yourself to gain access to the server"
)
async def verify(interaction):
    verifych = await verification_search(f"{interaction.guild.id}")
    verifychannel = int(verifych)  
    if interaction.channel.id != verifychannel:
        await interaction.send(f"You can only use this command in <#{verifychannel}>")
    else:
        list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        FileName = ""
        for i in range(5, 15):
            FileName += (random.choice(list))
            continue
        img = Image.open('./img/astral.png')

        image = ImageDraw.Draw(img)
        font = ImageFont.truetype("./font/MomB.ttf", 30)

        guildname= interaction.guild.name
        widthithink = 222
        width = widthithink - len(guildname) * 7.5
        
        image.text((width, 375), f"to {guildname}", fill=(43,22,197), font=font)
        image.text((160, 275), f"{FileName}", fill=(32,22,197), font=font)
        image.text((125, 300), f"Please enter the", fill=(43,22,197), font=font)
        image.text((125, 325), f"letters/numbers", fill=(43,22,197), font=font)
        image.text((85, 350), f"above to gain access", fill=(43,22,197), font=font)
        img.save(f"./img/astral{FileName}.png")
        await interaction.send(file=disnake.File(f"./img/astral{FileName}.png"))
        try:
            await Checker(f"{FileName}")
        except:
            pass
        verifyrole = await verifyrole_search(f"{interaction.guild.id}")
        await interaction.author.add_roles(disnake.Object(verifyrole))  
        await webhooksend("Member Verified", f"Verified <@{interaction.author.id}>", f"{interaction.guild.id}")        
        await interaction.channel.purge(limit=9999999)
        embed = disnake.Embed(
            title=f"How To Verify!",
            description=f"**To Verify Yourself, Please Enter /verify, Then Enter The Code, Case InSensitive**",
            color=0xDC143C,
            timestamp=disnake.utils.utcnow()
        )
        await interaction.send(embed=embed)



@bot.slash_command(
    name="setup",
    description="Sets Up The Bot",
)
@checks.not_blacklisted()
@commands.has_permissions(manage_guild=True)
async def setup(interaction):
    await interaction.send("Setup Started", ephemeral=True)
    category = await interaction.guild.create_category(name="Astral")
    channel = await category.create_text_channel(name="Astral - Bot Logging")
    with open("./img/astral.png", "rb") as file:
        data = file.read()
    webhook = await channel.create_webhook(name="Astral - Bot Logging", avatar=data)
    muterole = await interaction.create_role(name="Mute Role", permissions=disnake.Permissions(speak=False))
    verifyrole = await interaction.create_role(name="Verify Role", permissions=disnake.Permissions(view_channels=True))
    await verifyrole_add(f"{interaction.guild.id}", f"{verifyrole.id}")
    await muterole_add(interaction.guild.id, muterole.id)
    await webhook_add(f"{interaction.guild.id}", f"{webhook.url}")
    await interaction.send("Setup Complete!", ephemeral=True)



@bot.slash_command(
    name="testhooksend",
    description="Sends a test message to the webhook",
)
@checks.not_blacklisted()
@commands.has_permissions(administrator=True)
async def testhooksend(interaction):
    await webhooksend("Test Message", "Test Message", f"{interaction.guild.id}")
    await interaction.send("Message Sent")



@bot.slash_command(
    name="emojify",
    description="emojifies your text",
    options=[
        Option(
            name="text",
            description="The text to emojify",
            type=OptionType.string,
            required=True            
        )
    ]
)
async def emojify(interaction: ApplicationCommandInteraction, text: str) -> None: 
    if text != None:
        out = text.lower()
        text = out.replace(' ', '   ')\
                .replace('!', '❗')\
                .replace('?', '❓')\
                .replace('a', '\u200B🇦')\
                .replace('b', '\u200B🇧')\
                .replace('c', '\u200B🇨')\
                .replace('d', '\u200B🇩')\
                .replace('e', '\u200B🇪')\
                .replace('f', '\u200B🇫')\
                .replace('g', '\u200B🇬')\
                .replace('h', '\u200B🇭')\
                .replace('i', '\u200B🇮')\
                .replace('j', '\u200B🇯')\
                .replace('k', '\u200B🇰')\
                .replace('l', '\u200B🇱')\
                .replace('m', '\u200B🇲')\
                .replace('n', '\u200B🇳')\
                .replace('ñ', '\u200B🇳')\
                .replace('o', '\u200B🇴')\
                .replace('p', '\u200B🇵')\
                .replace('q', '\u200B🇶')\
                .replace('r', '\u200B🇷')\
                .replace('s', '\u200B🇸')\
                .replace('t', '\u200B🇹')\
                .replace('u', '\u200B🇺')\
                .replace('v', '\u200B🇻')\
                .replace('w', '\u200B🇼')\
                .replace('x', '\u200B🇽')\
                .replace('y', '\u200B🇾')\
                .replace('z', '\u200B🇿')
    await interaction.send(text)

# Starting The Bot
bot.run(config["token"])