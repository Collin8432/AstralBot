# Imports
import disnake
from disnake import Webhook



import aiohttp



from helpers.database import webhook_search



# Function
async def webhooksend(title: str, description: str, guild_id: str) -> None:
   try:
      async with aiohttp.ClientSession() as session:
         hook = await webhook_search(guild_id)
         webhook = Webhook.from_url(f"{hook}", session=session)
         embed = disnake.Embed(
            title=f"{title}",
            description=f"{description}",
            color=0xDC143C,
            timestamp=disnake.utils.utcnow()
         )
         await webhook.send(embed=embed, username="Astral - Bot Logging")
   except:
      pass