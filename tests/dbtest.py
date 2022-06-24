import sqlite3 as sqlite

connection = sqlite.connect("./secret/discord.db")
cursor = connection.cursor()


"""
string = text
int = integer
float = real  
binary = blob
"""

# cursor.execute("""
#                create table astral (guild_name text, guild_id integer, webhook text, memberchannel integer, verification integer, muterole integer, verifyrole integer)
#                """)

guildinfo = [
    ("astral", 243, "texttt", 123, 123, 123, 132)
]

cursor.executemany("insert into astral values (?, ?, ?, ?, ?, ?, ?)", guildinfo)

for row in cursor.execute("select guild_name from astral where guild_id=:self", {"self": 243}):
    row = str(row).replace("'", "").replace("(", "").replace(")", "").replace(",", "")
    print(row)

connection.close()

