import disnake
from disnake.ext import commands
from disnake import ApplicationCommandInteraction
from helpers.webhook import webhooksend

class EventListeners(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
   
    @commands.Cog.listener()
    async def on_ready():
       print(f"Logged in as {.user.name}")
       status_task.start()
    @commands.Cog.listener()
    async def on_button_click(interaction):
       custom_id=interaction.component.custom_id
       if custom_id == "pingstaff":
          pingrole = interaction.guild.get_member(935339228324311040)
          await interaction.send(pingrole.mention)
       elif disnake.errors.HTTPException:
          pass
       elif custom_id == "deletechannel":
          await interaction.channel.delete()
       elif custom_id == "nerd":
          await interaction.send("nerd")
       elif custom_id == "balls":
          await interaction.send("balls")
       elif custom_id == "shutdownconfirm":
          commands.has_permissions(administrator=True)
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
 

    @commands.Cog.listener()
    async def on_slash_command(interaction):
       await webhooksend(f"Command Executed", f"**<@{interaction.author.id}>** Executed /**{interaction.data.name}** in <#{interaction.channel.id}>")

    @commands.Cog.listener()
    async def on_slash_command_error(interaction: ApplicationCommandInteraction, error: Exception) -> None:
       embed = disnake.Embed(
          title="Error",
          description=f"Error With Command:\n```py\n{error}```",
          color=0xDC143C,
          timestamp=disnake.utils.utcnow()
       )
       try:
          await interaction.response.defer()
          await interaction.edit_original_message(embed=embed, ephemeral=True)
       except:
          await interaction.send(embed=embed, ephemeral=True)

    @commands.Cog.listener('on_message')
    async def on_message(message):
       botids = [938579223780655145]
       if "nigger" in message.content and message.guild.id == 944297787779072020 and message.author.id not in botids:
          await message.reply("Please Don't Say That")
          await message.delete()
          await webhooksend("N-Word Logged", f"<@{message.author.id}> Sent An N-Word In <#{message.channel.id}>\n **Content:** \n{message.content}")
       if message.channel.id == 970325969359503460 and message.author.id not in botids:
          await message.author.edit(nick=f"{message.content}")
          embed = disnake.Embed(
                title=f"Nickname Changed!",
                description=f"<@{message.author.id}> Changed Nickname To: {message.content}",
                color=0xDC143C,
                timestamp=disnake.utils.utcnow()
          )
          embed.set_image(url=message.author.display_avatar)
          await message.reply(embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(message):
       await webhooksend("Message Deleted", f"Chat Deleted In <#{message.channel.id}>\n**Author:** \n<@{message.author.id}>\n**Content:** \n{message.content}")

    @commands.Cog.listener()
    async def on_member_ban(guild, user):
       await webhooksend("Member Banned", f"<@{user.id}> Was Banned From Astral")
       embed = disnake.Embed(
          title="You Were Banned From Astral",
          description=f"<@{user.id}> Was Banned From Astral",
          color=0xDC143C,
          timestamp=disnake.utils.utcnow()
       ) 
       await user.send(embed=embed)   

    @commands.Cog.listener()
    async def on_member_unban(guild, user):
       await webhooksend("Member Unbanned", f"<@{user.id}> Was Unbanned From Astral")
       embed = disnake.Embed(
          title="You Were Unbanned From Astral",
          description=f"<@{user.id}> Was Unbanned From Astral\nhttps://discord.gg/uNnJyjaG",
          color=0xDC143C,
          timestamp=disnake.utils.utcnow()
       )
       await user.send(embed=embed)

    @commands.Cog.listener()
    async def on_presence_update(before, after):
       if before.status != after.status and after.id != 935339228324311040:
          await webhooksend("Presence Changed", f"<@{after.id}> Changed Status \n**From:**\n{before.status}\n**To:**\n{after.status}")
       if before.activity != after.activity and after.id != 935339228324311040:
          await webhooksend("Activity Changed", f"<@{after.id}> Changed Activity \n**From:**\n{before.activity}\n**To:**\n{after.activity}")

    @commands.Cog.listener()
    async def on_member_update(before, after):
       if before.display_name != after.display_name:
          await webhooksend("Display Name Changed", f"<@{after.id}> **Changed Name**\n**From:**\n{before.display_name}\n**To:**\n{after.display_name}")
       if before.roles != after.roles:
          roles = [role.mention for role in before.roles]
          roles2 = [role.mention for role in after.roles]
          beforeroles = str(roles).replace("]", "").replace("[", "").replace("'", "")
          afterroles = str(roles2).replace("]", "").replace("[", "").replace("'", "")
          await webhooksend(f"Roles Changed", f"<@{after.id}> Roles Changed\n**Before:**\n{beforeroles}\n**After:**\n{afterroles}")
       if before.current_timeout != after.current_timeout:
          await webhooksend(f"Timeout!", f"<@{after.id}> Timeout Changed\n**Before:**\n{before.current_timeout}\n**After:**\n{after.current_timeout}")

   

    @commands.Cog.listener()
    async def on_user_update(before, after):
       if before.display_avatar != after.display_avatar:
          await webhooksend(f"Avatar Changed", f"<@{after.member.id}> Avatar Changed\n**Before:**\n{before.display_avatar}\n**After:**\n{after.display_avatar}")
       if before.discriminator != after.discriminator:
          await webhooksend(f"Discriminator Changed", f"<@{after.member.id}> Discriminator Changed\n**Before:**\n{before.discriminator}\n**After:**\n{after.discriminator}")

    @commands.Cog.listener()
    async def on_member_join(member):
      guild = member.guild
      if guild.system_channel is not None:
          img = Image.open("./img/astral.png")
          image = ImageDraw.Draw(img)
          font = ImageFont.truetype("./font/MomB.ttf", 30)
          image.text((160, 275), f"Welcome,", font=font, fill=(43,22,197))
          image.text((160, 325), f"{member.name}", font=font, fill=(43,22,197))
          list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
          randomnumber = ""
          for i in range(5, 15):
                randomnumber += (random.choice(list))
                continue
          img.save(f"./img/astral{randomnumber}.png")
          imgfile = disnake.File(f"./img/astral{randomnumber}.png") 
          await guild.system_channel.send(file=imgfile)
          await webhooksend("Member Joined", f"<@{member.id}> Joined Astral")

    @commands.Cog.listener()
    async def on_member_remove(member):
       await webhooksend("Member Left", f"<@{member.id}> Left Astral")
       embed = disnake.Embed(
          title=f"{member.name}, Sorry Too See You Go!",
          description=f"If you left on accident, please join back!\nhttps://discord.gg/uNnJyjaG",
          color=0xDC143C,
          timestamp=disnake.utils.utcnow()
       )
       try:
          await member.send(embed=embed)
       except disnake.Forebidden:
          pass



def setup(bot):
   bot.add_cog(EventListeners(bot))