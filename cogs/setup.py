# Imports
import traceback
import disnake
from disnake.ext import commands



from utils.db import *
from utils.webhook import webhooksend
from utils.color import color
from utils.message import interactionsend



# Setup Dropdown
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
      
      
   # Commands
   @commands.slash_command(
      name="database",
      description="searches for servers db settings",
   )
   @commands.has_permissions(administrator=True)
   async def serversearchs(interaction: disnake.ApplicationCommandInteraction) -> None:
      results = fetch_all_guild_information(f"{interaction.guild.id}")  
     
      embed = disnake.Embed(
         title=f"Server Database",
         description=f"🟥DO NOT SHARE THIS INFORMATION🟥\n{results}",  
         color=color,
         timestamp=disnake.utils.utcnow()
      )
      embed.set_footer(
         text=f"Requested by {interaction.author}"
      )
      await interactionsend(interaction=interaction, embed=embed, ephemeral=True) 

      
      
   @commands.slash_command(
      name="setup",
      description="displays the setup options, to be selected"
   )
   @commands.has_permissions(administrator=True)
   async def setup(self, interaction):
      await interactionsend(interaction=interaction, msg="Choose The Correct Option, As This Cannot Be Undone.", view=SetupSelectView(), ephemeral=True)
