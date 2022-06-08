# Imports
import disnake
from disnake.ext import commands




from helpers import checks
from helpers.database import webhook_add, verification_add, memberchannel_add, muterole_add, serversearch, verification_search, verifyrole_add, verifyrole_search, memberchannel_search
from helpers.webhook import webhooksend



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
            label="Member Voice Channel Display Only",
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
         await interaction.send("Setup Started", ephemeral=True)
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
         membervoicechannel = await interaction.guild.create_voice_channel(name=f"Members: {interaction.guild.member_count}")
         voverwrites = {
            interaction.guild.default_role: disnake.PermissionOverwrite(view_channel=True, send_messages=True, read_messages=True),
            interaction.guild.get_role(verifyrole.id): disnake.PermissionOverwrite(view_channel=False, send_messages=False, read_messages=False),
         }
         
         verificationchannel = await interaction.guild.create_text_channel(name=f"Verify", overwrites=voverwrites)
         ch = interaction.guild.get_channel(verificationchannel.id)
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
         await ch.send(embed=embed)
         await verifyrole_add(f"{interaction.guild.id}", f"{verifyrole.id}")
         await muterole_add(f"{interaction.guild.id}", f"{muterole.id}")
         await webhook_add(f"{interaction.guild.id}", f"{webhook.url}")
         await memberchannel_add(f"{interaction.guild.id}", f"{membervoicechannel.id}")
         await verification_add(f"{interaction.guild.id}", f"{verificationchannel.id}")
         await webhooksend("Test Webhook Message", "If This Message Is Sent, The Webhook Is Working, Further Use Of The Bot Can Be Accessed With /help", f"{interaction.guild.id}")
         await interaction.send("Setup Complete!", ephemeral=True)
         
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
         embed.set_footer(
            text=f"Requested by {interaction.author}"
         )
         await interaction.send(embed=embed, ephemeral=True)
         
         
         
      elif self.values[0] == "Logging Only":
         await interaction.send("Setup Started", ephemeral=True)
         overwrites = {
            interaction.guild.default_role: disnake.PermissionOverwrite(view_channel=False, send_messages=False, read_messages=False),  
         }
         category = await interaction.guild.create_category(name="Astral", overwrites=overwrites)
         channel = await category.create_text_channel(name="Astral - Bot Logging")
         with open("./img/astral.png", "rb") as file:
            data = file.read()
         webhook = await channel.create_webhook(name="Astral - Bot Logging", avatar=data)         
         await webhook_add(f"{interaction.guild.id}", f"{webhook.url}")
         await webhooksend("Test Webhook Message", "If This Message Is Sent, The Webhook Is Working, Further Use Of The Bot Can Be Accessed With /help", f"{interaction.guild.id}")
         await interaction.send("Setup Complete!", ephemeral=True)
         
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
         embed.set_footer(
            text=f"Requested by {interaction.author}"
         )
         await interaction.send(embed=embed, ephemeral=True)
         
         
         
      elif self.values[0] == "Verification Only":
         await interaction.send("Setup Started", ephemeral=True)
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
            color=0xDC143C,
            timestamp=disnake.utils.utcnow()
         )
         embed.set_image(
            file=disnake.File(f"C:/Users/astro/Documents/GitHub/AstralBot/img/VerifyVideo.mp4")
         )
         embed.set_footer(
            text=f"Astral Verification"
         )
         await ch.send(embed=embed)
         await verifyrole_add(f"{interaction.guild.id}", f"{verifyrole.id}")
         await verification_add(f"{interaction.guild.id}", f"{verificationchannel.id}")
         await interaction.send("Setup Complete!", ephemeral=True)
         
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
         embed.set_footer(
            text=f"Requested by {interaction.author}"
         )
         await interaction.send(embed=embed, ephemeral=True)
         
         
      elif self.values[0] == "Member Voice Channel Display Only":
         await interaction.send("Setup Started", ephemeral=True)
         membervoicechannel = await interaction.guild.create_voice_channel(name=f"Members: {interaction.guild.member_count}")
         await memberchannel_add(f"{interaction.guild.id}", f"{membervoicechannel.id}")
         await interaction.send("Setup Complete!", ephemeral=True)
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
         embed.set_footer(
            text=f"Requested by {interaction.author}"
         )
         await interaction.send(embed=embed, ephemeral=True)
   
   
      elif self.values[0] == "Mute Only":
         await interaction.send("Setup Started", ephemeral=True)
         muterole = await interaction.guild.create_role(name="Mute Role", permissions=disnake.Permissions(speak=False))
         await muterole_add(f"{interaction.guild.id}", f"{muterole.id}")
         await interaction.send("Setup Complete!", ephemeral=True)
      
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
         embed.set_footer(
            text=f"Requested by {interaction.author}"
         )
         await interaction.send(embed=embed, ephemeral=True)
   async def on_error(self, error: Exception):
      print(error)
         
         
         
class SetupSelectView(disnake.ui.View):
    def __init__(self):
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(SetupSelect())


class setupcmds(commands.Cog, name="Setup cmd"):
   def __init__(self, bot):
      self.bot = bot
      
      
   # Commands
   
   
   
   @commands.slash_command(
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
      embed.set_footer(
         text=f"Requested by {interaction.author}"
      )
      await interaction.send(embed=embed, ephemeral=True) 

      
      
   @commands.slash_command(
      name="setup",
      description="Displays The Setup Options, To Be Selected"
   )
   @commands.has_permissions(administrator=True)
   async def test(self, interaction):
      await interaction.send("Choose The Correct Option, As This Cannot Be Undone.", view=SetupSelectView(), ephemeral=True)
      


def setup(bot):
   bot.add_cog(setupcmds(bot))