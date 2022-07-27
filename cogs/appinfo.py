"""
Contains appinfo command

Copyright 2022-Present Astral 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


import disnake
from disnake.ext import commands


from utils.color import color
from utils.DeleteButton import DeleteButton


appinfo = """
**App Name:** `{appname}`
**App Id:** `{appid}`
**Bot Name:** `{botname}`
**Bot Id:** `{botid}`
**Public Bot:** `{publicbot}`
**Requires Bot Code Grant:** `{codegrant}`
**Terms Of Service URL:** `{tosurl}`
**Privacy Policy URL:** `{ppurl}`
**Bot Invite URL: ** {inviteurl}

**App Flags:** \n`{appflags}`

**App Tags:** \n`{apptags}`
"""


class Appinfo(commands.Cog):
   def __init__(self, bot: commands.Bot):
      self.bot = bot
      
   
   @commands.slash_command(
      name="appinfo",
      description="shows info about the bot",
   )
   async def appinfo(self, interaction):
      app = await self.bot.application_info()
      appflags=f"""Gateway Presence: {app.flags.gateway_presence}
Gateway Presence Limited: {app.flags.gateway_presence_limited}
Gateway Guild Members: {app.flags.gateway_guild_members}
Verificaiton Pending Guild Limit: {app.flags.verification_pending_guild_limit}
Embedded: {app.flags.embedded}
Gateway Message Content: {app.flags.gateway_message_content}
Gateway Message Content Limited: {app.flags.gateway_message_content_limited}"""
      apptag=str(app.tags)
      apptags=apptag.replace("[", "").replace("]", "").replace("'", "")
      embed = disnake.Embed(
         title="Appinfo!",
         description=appinfo.format(
            appname=app.name,
            appid=app.id,
            botname=self.bot.user.name, 
            botid=self.bot.user.id,
            publicbot=app.bot_public,
            codegrant=app.bot_require_code_grant,
            tosurl=app.terms_of_service_url,
            ppurl=app.privacy_policy_url,
            inviteurl="[Invite](https://discord.com/api/oauth2/authorize?client_id=938579223780655145&permissions=8&scope=bot%20applications.commands)",
            appflags=appflags,
            apptags=apptags,
            ),
         color=color,
         timestamp=disnake.utils.utcnow(),
      )
      embed.set_footer(
         text="Requested by {}".format(interaction.author),
      )
      DeleteButton() = DeleteButton
      await interaction.send(embed=embed, DeleteButton()=DeleteButton())