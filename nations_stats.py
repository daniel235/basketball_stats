import sqlite3

#data is format of list [(of tuples)]
def get_all_data(sq_file):
	conn = sqlite3.connect(sq_file)
	cur = conn.cursor()
	cur.execute("SELECT * FROM stats")

	data = []
	for row in cur:
		data.append(row)

	cur.close()
	return data


#column is 30
def get_countries(data):
	pass


def create_box_plot():
	pass
	

def get_country_data(country):
	pass


def get_nation_stats(sq_file):
	#import data
	data = get_all_data(sq_file)
	#get different countries
	countries = get_countries(data)
	#for country in countries select data from database
	for country in countries:
		country_data = get_country_data(country)
		#add to box plot
		create_box_plot(country_data)





