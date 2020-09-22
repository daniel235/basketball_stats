import sqlite3
import pandas as pd
import os
import nations_stats as ns

dbname = "basketballStats"
conn = sqlite3.connect("data/" + dbname + '.sqlite')
cur = conn.cursor()

#check if database exists
if (dbname + '.sqlite') not in os.listdir("data"):
	df = pd.read_csv("data/players_stats_by_season_full_details.csv")
	df.to_sql(name="stats", con=conn)


cur.execute('SELECT * FROM stats WHERE TEAM == "HOU" AND birth_year > 1990')

for row in cur:
	print(row)

cur.close()






