"""
Contains all setup commands for the bot

Copyright 2022-Present Astral 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


# Imports
import disnake
from disnake.ext import commands


from utils.db import *
from utils.webhook import webhooksend
from utils.color import color
from utils.message import interactionsend


class SetupSelect(disnake.ui.Select):
   def __init__(self):
      options = [
         disnake.SelectOption(
            label="Complete Setup - Reccomended",
            description="Creates All The Options, Can Be Seen Below",
            emoji="⚙️"
         ),
         disnake.SelectOption(
            label="Logging Only",
            description="Creates A Logging Channel With Webhook ONLY",
            emoji="⚙️"
         ),
         disnake.SelectOption(
            label="Verification Only",
            description="Creates A Verification Role, A Verification Channel ONLY",
            emoji="⚙️"
         ),
         disnake.SelectOption(
            label="Member Count Voice Channel Display Only",
            description="Creates A Voice Channel That Periodcally Displays The Member Count ONLY",
            emoji="⚙️"
         ),
         disnake.SelectOption(
            label="Mute Only",
            description="Creates A Mute Role ONLY",
            emoji="⚙️"
         )
      ]
      super().__init__(
         placeholder="Select An Option",
         min_values=1, 
         max_values=1,
         options=options
      )
      
      
   async def callback(self, interaction: disnake.MessageInteraction):
      if self.values[0] == "Complete Setup - Reccomended":
         await interactionsend(interaction=interaction, msg="Setup Started", ephemeral=True)
         overwrites = {
            interaction.guild.default_role: disnake.PermissionOverwrite(view_channel=False, send_messages=False, read_messages=False),  
         }
         category = await interaction.guild.create_category(name="Astral", overwrites=overwrites)
         channel = await category.create_text_channel(name="Astral - Bot Logging")
         with open("./img/astral.png", "rb") as file:
            data = file.read()
         webhook = await channel.create_webhook(name="Astral - Bot Logging", avatar=data)
         muterole = await interaction.guild.create_role(name="Mute Role", permissions=disnake.Permissions(speak=False))
         verifyrole = await interaction.guild.create_role(name="Verified", permissions=disnake.Permissions(view_channel=True))
         membercountvoicechannel = await interaction.guild.create_voice_channel(name=f"Members: {interaction.guild.member_count}")
         voverwrites = {
            interaction.guild.default_role: disnake.PermissionOverwrite(view_channel=True, send_messages=True, read_messages=True),
            interaction.guild.get_role(verifyrole.id): disnake.PermissionOverwrite(view_channel=False, send_messages=False, read_messages=False),
         }
         
         verificationchannel = await interaction.guild.create_text_channel(name=f"Verify", overwrites=voverwrites)
         ch = interaction.guild.get_channel(verificationchannel.id)
         embed = disnake.Embed(
            title=f"How To Verify!",
            description=f"**To Verify Yourself, Please Enter /verify, Then Enter The Code, Case InSensitive**",
            color=color,
            timestamp=disnake.utils.utcnow()
         )
         embed.set_image(
            file=disnake.File(f"C:/Users/astro/Documents/GitHub/AstralBot/img/VerifyVideo.mp4")
         )
         embed.set_footer(
            text=f"Astral Verification"
         )
         await ch.send(embed=embed)
         
         _verifyrole = fetch_guild_information("guild_verifyrole", f"{interaction.guild.id}")
         update_guild_information("guild_verifyrole", f"{_verifyrole}", f"{verifyrole.id}")
         
         _muterole = fetch_guild_information("guild_muterole", f"{interaction.guild.id}")
         update_guild_information("guild_muterole", f"{_muterole}", f"{muterole.id}")
         
         _webhook = fetch_guild_information("guild_webhook", f"{interaction.guild.id}")
         update_guild_information("guild_webhook", f"{_webhook}", f"{webhook.url}")
         
         _membervoicechannel = fetch_guild_information("guild_membercountvoicechannel", f"{interaction.guild.id}")
         update_guild_information(f"guild_membercountvoicechannel", f"{_membervoicechannel}", f"{membercountvoicechannel.id}")
         
         _verificationchannel = fetch_guild_information("guild_verificationchannel", f"{interaction.guild.id}")
         update_guild_information(f"guild_verificationchannel", f"{_verificationchannel}", f"{verificationchannel.id}")
         
         await webhooksend("Test Webhook Message", "If This Message Is Sent, The Webhook Is Working, Further Use Of The Bot Can Be Accessed With /help", f"{interaction.guild.id}")
         await interactionsend(interaction=interaction, msg="Setup Complete!", ephemeral=True)
         
      elif self.values[0] == "Logging Only":
         await interactionsend(interaction=interaction, msg="Setup Started", ephemeral=True)
         overwrites = {
            interaction.guild.default_role: disnake.PermissionOverwrite(view_channel=False, send_messages=False, read_messages=False),  
         }
         category = await interaction.guild.create_category(name="Astral", overwrites=overwrites)
         channel = await category.create_text_channel(name="Astral - Bot Logging")
         with open("./img/astral.png", "rb") as file:
            data = file.read()
         webhook = await channel.create_webhook(name="Astral - Bot Logging", avatar=data) 
         
         _webhook = fetch_guild_information("guild_webhook", f"{interaction.guild.id}")        
         update_guild_information(f"guild_webhook", f"{_webhook}", f"{webhook.url}")
         
         await webhooksend("Test Webhook Message", "If This Message Is Sent, The Webhook Is Working, Further Use Of The Bot Can Be Accessed With /help", f"{interaction.guild.id}")
         await interactionsend(interaction=interaction, msg="Setup Complete!", ephemeral=True)

      elif self.values[0] == "Verification Only":
         await interactionsend(interaction=interaction, msg="Setup Started", ephemeral=True)
         verifyrole = await interaction.guild.create_role(name="Verified", permissions=disnake.Permissions(view_channel=True))
         voverwrites = {
            interaction.guild.default_role: disnake.PermissionOverwrite(view_channel=True, send_messages=True, read_messages=True),
            interaction.guild.get_role(verifyrole.id): disnake.PermissionOverwrite(view_channel=False, send_messages=False, read_messages=False),
         }
         
         verificationchannel = await interaction.guild.create_text_channel(name=f"Verify", overwrites=voverwrites)
         ch = await interaction.guild.get_channel(verificationchannel.id)
         embed = disnake.Embed(
            title=f"How To Verify!",
            description=f"**To Verify Yourself, Please Enter /verify, Then Enter The Code, Case InSensitive**",
            color=color,
            timestamp=disnake.utils.utcnow()
         )
         embed.set_image(
            file=disnake.File(f"C:/Users/astro/Documents/GitHub/AstralBot/img/VerifyVideo.mp4")
         )
         embed.set_footer(
            text=f"Astral Verification"
         )
         await ch.send(embed=embed)
         
         _verifyrole = fetch_guild_information("guild_verifyrole", f"{interaction.guild.id}")
         update_guild_information("guild_verifyrole", f"{_verifyrole}", f"{verifyrole.id}")
         
         _verificationchannel = fetch_guild_information("guild_verificationchannel", f"{interaction.guild.id}")
         update_guild_information(f"{interaction.guild.id}", f"{_verificationchannel}" f"{verificationchannel.id}")
         
         await interactionsend(interaction=interaction, msg="Setup Complete!", ephemeral=True)
         
      elif self.values[0] == "Member Count Voice Channel Display Only":
         await interactionsend(interaction=interaction, msg="Setup Started", ephemeral=True)
         membervoicechannel = await interaction.guild.create_voice_channel(name=f"Members: {interaction.guild.member_count}")
         
         _membervoicechannel = fetch_guild_information("guild_membercountvoicechannel", f"{interaction.guild.id}")
         update_guild_information(f"guild_membercountvoicechannel", f"{_membervoicechannel}", f"{membervoicechannel.id}")
         
         await interactionsend(interaction=interaction, msg="Setup Complete!", ephemeral=True)
   
      elif self.values[0] == "Mute Only":
         await interactionsend(interaction=interaction, msg="Setup Started", ephemeral=True)
         muterole = await interaction.guild.create_role(name="Mute Role", permissions=disnake.Permissions(speak=False))
         
         _muterole = fetch_guild_information("guild_muterole", f"{interaction.guild.id}")
         update_guild_information("guild_muterole", f"{_muterole}" f"{muterole.id}")
         
         await interactionsend(interaction=interaction, msg="Setup Complete!", ephemeral=True)
         
   async def on_error(self, error: Exception):
      print(error)
         
         
class SetupSelectView(disnake.ui.View):
    def __init__(self):
        super().__init__()

        self.add_item(SetupSelect())


class setupcmds(commands.Cog, name="Setup cmd"):
   def __init__(self, bot):
      self.bot = bot
      
      
   @commands.slash_command(
    name="fetchdatabase",
    description="fetches the guilds db"
   )
   @commands.has_permissions(administrator=True)
   async def fetchdatabase(self, interaction):
      res = fetch_all_guild_information(f"{interaction.guild.id}")
      
      try:
         res = res[0]
         guild_name = res[0]
         guild_id = res[1]
         guild_webhook = res[2]
         guild_membercountvoicechannel = res[3]
         guild_verificationchannel = res[4]
         guild_muterole = res[5]    
         guild_verifyrole = res[6]     
         embed = disnake.Embed(
            title="Fetched Results!", 
            description=f"**Guild Name:\n{guild_name}\nGuild ID:\n{guild_id}\nGuild Webhook:\n{guild_webhook}\nGuild Member Count Voice Channel:\n{guild_membercountvoicechannel}\nGuild Verification Channel:\n{guild_verificationchannel}\nGuild Muterole:\n{guild_muterole}\nGuild Verification Role:\n{guild_verifyrole}**",
            color=color,
            timestamp=disnake.utils.utcnow()
         )
      except:
         embed = disnake.Embed(
            title="Error Fetching Results!", 
            color=color,
            timestamp=disnake.utils.utcnow()
         )
      await interactionsend(interaction=interaction, embed=embed)
      
      
   @commands.slash_command(
      name="setup",
      description="displays the setup options, to be selected"
   )
   @commands.has_permissions(administrator=True)
   async def setup(self, interaction):
      await interactionsend(interaction=interaction, msg="Choose The Correct Option, As This Cannot Be Undone", view=SetupSelectView(), ephemeral=True)
