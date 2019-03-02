#!/usr/bin/env python3
import psycopg2
import datetime

query1 = """select title, seen from vw_article 
			inner join articles on vw_article.path = slug 
			order by seen desc limit 3;"""
def top_articles(query):
	db = psycopg2.connect(database = "news")
	cur = db.cursor()
	cur.execute(query)
	output = cur.fetchall()
	for i, item in enumerate(output):
		print (str(output[i][0]) + " - "+ str(output[i][1]) + " views")

print("\n")	
print ("-----Top 3 Articles-----")
print("\n")
top_articles(query1)
print("\n")


query2 = """select authors.name, count(*) from vw_top_authors 
			inner join authors on vw_top_authors.author = authors.id 
			group by authors.name order by count(*) desc;"""
def top_authors(query):
	db = psycopg2.connect(database = "news")
	cur = db.cursor()
	cur.execute(query)
	output = cur.fetchall()
	for i,item in enumerate(output):
		print(str(output[i][0]) + " - " +str(output[i][1]) + " views")
	
print ("-----Popular Authors-----")
print("\n")
top_authors(query2)	
print("\n")


query3 = 'select date, percent from vw_percent where percent > 1;'
def error_percent(query):
	db = psycopg2.connect(database = "news")
	cur = db.cursor()
	cur.execute(query)
	output = cur.fetchall()
	
	for i,item in enumerate(output):
		date = ''.join(str(output[i][0]))
		date = date.split("-")
		year = int(date[0])
		month = int(date[1])
		day = int(date[2])
		ndate = datetime.datetime(year, month, day)
		print(ndate.strftime("%B") +" "+ ndate.strftime("%d") +"," + ndate.strftime("%Y") +" - "+ str(output[i][1]) +"%")
	
print("-----More than 1% Error in a Day-----")
print("\n")
error_percent(query3)	
print("\n")		
		

	
	
