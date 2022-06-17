# Imports
from tinydb import TinyDB, Query



# Setting DB Up
db = TinyDB("database.json")
Query = Query()


async def add_guild(guild_id):
   db.update({"guild_id": guild_id}, Query.guild_id == guild_id)
   

async def add_guild_message(guild_id, message_id):
   db.update({"db_guild_message": message_id}, Query.guild_id == guild_id)"})
   
   
async def idsearch(guild_id):
   results = db.search(Query.guild_id == guild_id)
   for result in results:
      return result["guild_id"]