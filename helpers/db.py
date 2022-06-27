import mysql.connector



def queries(query: str = None):
  if query == "guild_name": 
    return 0
  elif query == "guild_id": 
    return 1   
  elif query == "guild_webhook":
    return 2 
  elif query == "guild_membercountvoicechannel":
    return 3 
  elif query == "guild_verificationchannel":
    return 4 
  elif query == "guild_muterole":
    return 5 
  elif query == "guild_verifyrole":
    return 6
  elif query == "all":
    return
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



def insert_guild(guild_name = None, guild_id = None, guild_webhook = None, guild_membercountvoicechannel = None, guild_verificationchannel = None, guild_muterole = None, guild_verifyrole = None):
  try:
    if guild_webhook == None:
      guild_webhook = "This isnt real information, just randomly generated when joining a guild" + guild_id * 2
      print(guild_webhook)
    if guild_membercountvoicechannel == None:
      guild_membercountvoicechannel = "This isnt real information, just randomly generated when joining a guild" + guild_id * 3
      print(guild_membercountvoicechannel)
    if guild_verificationchannel == None:
      guild_verificationchannel = "This isnt real information, just randomly generated when joining a guild" + guild_id * 4
      print(guild_verificationchannel)
    if guild_muterole == None:
      guild_muterole = "This isnt real information, just randomly generated when joining a guild" + guild_id * 5
      print(guild_muterole)
    if guild_verifyrole == None:
      guild_verifyrole = "This isnt real information, just randomly generated when joining a guild" + guild_id * 6
      print(guild_verifyrole)

    sql = "INSERT INTO astraldatabase (guild_name, guild_id, guild_webhook, guild_membercountvoicechannel, guild_verificationchannel, guild_muterole, guild_verifyrole) VALUES (%s, %s, %s, %s, %s, %s, %s)"  
    values = (guild_name, guild_id, guild_webhook, guild_membercountvoicechannel, guild_verificationchannel, guild_muterole, guild_verifyrole)
    cursor.execute(sql, values)
    db.commit()
  except Exception as e:
    import traceback
    traceback.print_exc()
    print("----")
    print(e)
    
    

def remove_guild(guild_id: int = None):
  sql = f"DELETE FROM astraldatabase WHERE guild_id = '{guild_id}'"
  cursor.execute(sql)
  db.commit()



def fetch_guild_information(query: str = None, guild_id: int = None):
  sql = f"SELECT * FROM astraldatabase WHERE guild_id Like '%{guild_id}%'"
  cursor.execute(sql)
  results = cursor.fetchall()
  try: 
    results = results[0]
  except Exception as e:
    pass
  querynum = queries(query)
  return results[querynum]



def fetch_all_guild_information(guild_id: int = None):
  sql = f"SELECT * FROM astraldatabase WHERE guild_id Like '%{guild_id}%'"
  cursor.execute(sql)
  results = cursor.fetchall()
  return results



def update_guild_information(variable, before, after):
  sql = f"UPDATE astraldatabase SET {variable} = '{after}' WHERE {variable} = '{before}'"
  cursor.execute(sql)
  db.commit()