"""
Contains all of the information and functions for the database

Copyright 2022-Present Astral 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


# Imports
import mysql.connector


def queries(query: str = None):
  """_summary_


  Args:
      query (str, optional): _description_. Defaults to None.


  Returns:
      _type_: _description_
      
  
  * `queries` - used to generate the number for the tuple generated from the database
  """
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
    "::"
    
    
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


def insert_guild(guild_name = None,
                 guild_id = None, 
                 guild_webhook = None, 
                 guild_membercountvoicechannel = None, 
                 guild_verificationchannel = None, 
                 guild_muterole = None, 
                 guild_verifyrole = None):
  """_summary_


  Args:
      guild_name (_type_, optional): _description_. Defaults to None.
      guild_id (_type_, optional): _description_. Defaults to None.
      guild_webhook (_type_, optional): _description_. Defaults to None.
      guild_membercountvoicechannel (_type_, optional): _description_. Defaults to None.
      guild_verificationchannel (_type_, optional): _description_. Defaults to None.
      guild_muterole (_type_, optional): _description_. Defaults to None.
      guild_verifyrole (_type_, optional): _description_. Defaults to None.
      
      
  * `insert_guild` - Used too insert information into the database
  """
  try:
    if guild_webhook == None:
      guild_webhook = "This isnt real information, just randomly generated when joining a guild" + guild_id * 2
      
      
    if guild_membercountvoicechannel == None:
      guild_membercountvoicechannel = "This isnt real information, just randomly generated when joining a guild" + guild_id * 3
      
      
    if guild_verificationchannel == None:
      guild_verificationchannel = "This isnt real information, just randomly generated when joining a guild" + guild_id * 4
      
      
    if guild_muterole == None:
      guild_muterole = "This isnt real information, just randomly generated when joining a guild" + guild_id * 5
      
      
    if guild_verifyrole == None:
      guild_verifyrole = "This isnt real information, just randomly generated when joining a guild" + guild_id * 6
      
      

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
  """_summary_


  Args:
      guild_id (int, optional): _description_. Defaults to None.


  Used too remove a guild from the database
  """
  sql = f"DELETE FROM astraldatabase WHERE guild_id = '{guild_id}'"
  cursor.execute(sql)
  db.commit()


def fetch_guild_information(query: str = None, guild_id: int = None):
  """_summary_

  Args:
      query (str, optional): _description_. Defaults to None.
      guild_id (int, optional): _description_. Defaults to None.


  Returns:
      _type_: _description_
      
  
  Used too fetch information from a guild
  """
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
  """_summary_


  Args:
      guild_id (int, optional): _description_. Defaults to None.


  Returns:
      _type_: _description_


  Used too fetch all information in a guild
  """
  sql = f"SELECT * FROM astraldatabase WHERE guild_id Like '%{guild_id}%'"
  cursor.execute(sql)
  results = cursor.fetchall()
  return results


def update_guild_information(variable, before, after):
  """_summary_


  Args:
      variable (_type_): _description_
      before (_type_): _description_
      after (_type_): _description_
      
    
  Used too update guild information
  """
  sql = f"UPDATE astraldatabase SET {variable} = '{after}' WHERE {variable} = '{before}'"
  cursor.execute(sql)
  db.commit()