from operator import indexOf
import mysql.connector



def queries(query: str = None):
  if query == "guild_name": 
    return 0
  elif query == "guild_id": 
    return 1   
  elif query == "guild_webhook":
    return 2 
  elif query == "guild_membervoicechannel":
    return 3 
  elif query == "guild_verificationchannel":
    return 4 
  elif query == "guild_muterole":
    return 5 
  elif query == "guild_verifyrole":
    return 6
  else:
    return "Error Processing Query, Check Spelling"



db = mysql.connector.connect(
  host="containers-us-west-72.railway.app",
  user="root",
  password="PbK9zroblhTWZ0NYQxAh",
  port="7359",
  database="railway"
)



cursor = db.cursor()



def insertguild(guild_name: str = None, guild_id: int = None, guild_webhook: str = None, guild_membercountvoicechannel: int = None, guild_verificationchannel: int = None, guild_muterole: int = None, guild_verifyrole: int = None):
  sql = "INSERT INTO astraldatabase (guild_name, guild_id, guild_webhook, guild_membercountvoicechannel, guild_verificationchannel, guild_muterole, guild_verifyrole) VALUES (%s, %s, %s, %s, %s, %s, %s)"  
  values = (guild_name, guild_id, guild_webhook, guild_membercountvoicechannel, guild_verificationchannel, guild_muterole, guild_verifyrole)
  cursor.execute(sql, values)
  db.commit()



def fetch_guild_information(query: str = None, guild_id: int = None):
  
  sql = f"SELECT * FROM astraldatabase WHERE guild_id Like '%{guild_id}%'"
  cursor.execute(sql)
  results = cursor.fetchall()
  for res in results:
    print(res[queries(query)])
  
  

def update_guild_information(variable, before, after):
  sql = f"UPDATE astraldatabase SET {variable} = %s WHERE {variable} = %s"
  val = (after, before)
  cursor.execute(sql, val)
  db.commit()  
  
  
  
def remove_guild(guild_id):
  sql = f"DELETE FROM astraldatabase WHERE guild_id = '{guild_id}'"
  cursor.execute(sql)  
  
cursor.execute("SHOW DATABASES")

for x in cursor:
  print(x)