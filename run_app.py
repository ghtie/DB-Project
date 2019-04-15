# application to run program from terminal
from __future__ import print_function
from mysql.connector import errorcode

import configparser
from flask import Flask, render_template, Response, request, redirect, url_for
import mysql.connector


# read configuration from file
config = configparser.ConfigParser()
config.read('config.ini')

# set up application server
app = Flask(__name__)

#Define function to query database, returns result of query
def db_query(sql):
	cnx = mysql.connector.connect(user = 'team_17', password = 
'2004d2a4', port = '3306', host = 'eecslab-9.case.edu', database = 
'team_17')
	cursor = cnx.cursor()
	
	cursor.execute(sql) #sql is the command, as a string literal
	result = cursor.fetchall() #returns all results of the query

	cursor.close()
	cnx.close()
	return result

#Define function to write to database
def db_write(sql):
	cnx = mysql.connector.connect(user = 'team_17', password = 
'2004d2a4', port = '3306', host = 'eecslab-9.case.edu', database = 
'team_17')
	cursor = cnx.cursor()
	cursor.execute()
	cursor.commit()
	cursor.close()
	cnx.close()

# not sure if this is the best app.route function to use yet
@app.route('/')
def basic_response():
    return render_template('home.html')

# trying to get buttons to work but isnt
@app.route('/action1', methods=['POST'])
def button2_should_do_something():
	if "method1" in request.form:
		print ("You pressed this button.")
		return '', 400
	return ''

if __name__ == '__main__':
    app.run()
    #app.run(**config['app']) will probably need this one rather than app.run()
