"""
Contains async def def webhooksend used too send messages to a discord webhook

Copyright 2022-Present Astral 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


# Imports
import disnake
from disnake import Webhook


import aiohttp


from utils.db import *
from utils.color import color


async def webhooksend(title: str, description: str, guild_id: str) -> None:
   """
   Used too send messages to a discord webhook
   
   
   Args:
       title (str): _description_
       description (str): _description_
       guild_id (str): _description_
   
   
   See Also:
         * :func:`utils.db.fetch_guild_information`
   """
   
   
   try:
      async with aiohttp.ClientSession() as session:
         hook = fetch_guild_information("guild_webhook", guild_id)
         webhook = Webhook.from_url(f"{hook}", session=session)
         description = str(description).replace("*", "")
         title = str(title).replace("!", "")
         embed = disnake.Embed(
            title=f"{title}!",
            description=f"**{description}**",
            color=color,
            timestamp=disnake.utils.utcnow()
         )
         embed.set_footer(
            text=f"Astral Discord Bot"
         )
         await webhook.send(embed=embed, username="Astral - Bot Logging")
   except: 
      pass




      
