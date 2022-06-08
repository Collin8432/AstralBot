# Imports
import json
import os
import random
import sys
import traceback


import disnake
from disnake.ext import tasks, commands
from disnake.ext.commands import Bot



from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont



from helpers.webhook import webhooksend
from helpers.helpembeds import helpemb, funemb, modemb, setupemb
from helpers.database import verification_search, verifyrole_search, memberchannel_search
from helpers import checks
from helpers.deleteinteraction import deleteinteraction



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
                print(f"Loaded ✅ {extension}.py")
            except Exception as e:
                traceback.print_exc()
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")



if __name__ == "__main__":
    load_commands("general")
    load_commands("moderation")
    load_commands("fun")
    load_commands("listeners")
    load_commands("setup")
    global start_time
    start_time = disnake.utils.utcnow()



# Tasks and Special Events
@tasks.loop(minutes=1.0)
async def status_task() -> None:
    statuses = [f"Watching Over {len(bot.guilds)} Servers"]
    await bot.change_presence(activity=disnake.Game(random.choice(statuses)))
    for guild in bot.guilds:
        members = len(guild.members)
        id = guild.id
        ch = await memberchannel_search(f"{id}")
        if ch is not None:
            gd = await bot.fetch_guild(id)
            try:
                channel = await bot.fetch_channel(ch)
            except disnake.NotFound:
                pass
            try:
                await channel.edit(name=f"Members: {members}")
            except Exception as e:
                print(e)
        else:
            list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
            s = random.choice(list)
            if s == "a":
                await webhooksend(f"Member Channel Updates!", "We Reccomend Adding A Memberchannel To Your Server!\nTo Do This, Type `/setmembervoicechannel` In Any Voice Channel In Your Server!", f"{id}")
            
   

@bot.event
async def on_ready():
    await status_task.start()



@bot.listen("on_button_click")
async def listener(interaction: disnake.MessageCommandInteraction):
    try:
        if (interaction.component.custom_id) == "deleteinter":
            if not interaction.author:
                await interaction.send("You Must Be The Author To Delete The Interaction", ephemeral=True)
            else:
                await interaction.message.delete()
        elif (interaction.component.custom_id) == "balls":
            await interaction.send("balls", view=deleteinteraction())
        elif (interaction.component.custom_id) == "nerd":
            await interaction.send("nerd", view=deleteinteraction())
        elif (interaction.component.custom_id) == "shutdowncomfirm":
            os._exit(0)
        elif (interaction.component.custom_id) == "shutdowncancel":
            await interaction.response.send_message("Cancelled!")
            await interaction.message.delete()
        elif (interaction.component.custom_id) == "genhelp":
            embed = helpemb
            embed.set_footer(
                text=f"Requested by {interaction.author}"
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
        elif (interaction.component.custom_id) == "funhelp":
            embed = funemb
            embed.set_footer(
                text=f"Requested by {interaction.author}"
            )   
            await interaction.response.send_message(embed=embed, ephemeral=True)
        elif (interaction.component.custom_id) == "modhelp":
            embed = modemb
            embed.set_footer(
                text=f"Requested by {interaction.author}"
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
        elif (interaction.component.custom_id) == "setuphelp":
            embed = setupemb
            embed.set_footer(
                text=f"Requested by {interaction.author}"
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            await interaction.response.send_message(f"Invalid Button! - {interaction.component.custom_id}")
    except:
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
    await interaction.send(embed=embed, view=deleteinteraction())



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
        await interaction.send(f"You can only use this command in <#{verifychannel}>", view=deleteinteraction())
    else:
        list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        FileName = ""
        for i in range(5, 15):
            FileName += (random.choice(list))
            continue
        img = Image.open('./img/Astral.png')

        image = ImageDraw.Draw(img)
        font = ImageFont.truetype("./font/MomB.ttf", 30)

        guildname = interaction.guild.name
        widthithink = 222
        width = widthithink - len(guildname) * 7.5
        
        image.text((width, 375), f"to {guildname}", fill=(43,22,197), font=font)
        image.text((160, 275), f"{FileName}", fill=(32,22,197), font=font)
        image.text((125, 300), f"Please enter the", fill=(43,22,197), font=font)
        image.text((125, 325), f"letters/numbers", fill=(43,22,197), font=font)
        image.text((85, 350), f"above to gain access", fill=(43,22,197), font=font)
        img.save(f"./img/astral{FileName}.png")
        await interaction.send(file=disnake.File(f"./img/astral{FileName}.png"), view=deleteinteraction())
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
        embed.set_image(
            file=disnake.File(f"C:/Users/astro/Documents/GitHub/AstralBot/img/VerifyVideo.mp4")
        )
        embed.set_footer(
            text=f"Astral Verification"
         )
        await interaction.send(embed=embed)
    


# Starting The Bot
bot.run(config["token"])