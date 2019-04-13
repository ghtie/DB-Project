from __future__ import print_function
from mysql.connector import errorcode
import mysql.connector

#Define function to query database, returns result of query
def db_query(sql):
	cnx = mysql.connector.connect(user = 'team_17', password = '2004d2a4', port = '3306', host = 'eecslab-9.case.edu')
	cursor = cnx.cursor()
	
	cursor.execute(sql) #sql is the command, as a string literal
	result = cursor.fetchall() #returns all results of the query

	cursor.close()
	cnx.close()
	return result

#Define function to write to database
def db_write(sql):
	cnx = mysql.connector.connect(user = 'team_17', password = '2004d2a4', port = '3306', host = 'eecslab-9.case.edu')
	cursor = cnx.cursor()
	cursor.execute()
	cursor.commit()
	cursor.close()
	cnx.close()
