# Imports
from tinydb import TinyDB, Query



# Setting DB Up
db = TinyDB("./secret/database.json")
guild = Query()



# DB Functions
async def on_join_insert(guild_name, guild_id):
   db.insert({"guild_name": f"{guild_name}", "guild_id": f"{guild_id}", "webhook": "", "verification": "", "memberchannel": "", "muterole": "", "verifyrole": ""})



async def webhook_add(guild_id, webhook):
   db.update({"webhook": webhook}, guild.guild_id == guild_id)



async def verification_add(guild_id, channelid):
   db.update({"verification": channelid}, guild.guild_id == guild_id)



async def memberchannel_add(guild_id, channelid):
   db.update({"memberchannel": channelid}, guild.guild_id == guild_id)



async def memberchannel_search(guild_id):
   results = db.search(guild.guild_id == guild_id)
   for result in results:
      return result["memberchannel"]



async def webhook_search(guild_id):
   results = db.search(guild.guild_id == guild_id)
   for result in results:
      return result["webhook"]



async def on_leave_remove(guild_id):
   db.remove(guild.guild_id == guild_id)



async def muterole_add(guild_id, roleid):
   db.update({"muterole": roleid}, guild.guild_id == guild_id)



async def muterole_search(guild_id):
   results = db.search(guild.guild_id == guild_id)
   for result in results:
      return int(result["muterole"])



async def serversearch(guild_id):
   results = db.search(guild.guild_id == guild_id)
   return results



async def verification_search(guild_id):
   results = db.search(guild.guild_id == guild_id)
   for result in results:
      return result["verification"]
      


async def verifyrole_add(guild_id, roleid):
   db.update({"verifyrole": roleid}, guild.guild_id == guild_id)



async def verifyrole_search(guild_id):
   results = db.search(guild.guild_id == guild_id)
   for result in results:
      return result["verifyrole"]