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
	cnx = mysql.connector.connect(**config['mysql.connector'])
	cursor = cnx.cursor()
	
	cursor.execute(sql) #sql is the command, as a string literal
	result = cursor.fetchall() #returns all results of the query

	cursor.close()
	cnx.close()
	return result

#Define function to write to database
def db_write(sql):
	cnx = mysql.connector.connect(**config['mysql.connector'])
	cursor = cnx.cursor()
	cursor.execute(sql)
	cursor.commit()
	cursor.close()
	cnx.close()

@app.route('/')
def home():
	return render_template('home.html')


@app.route('/goToBuyPage', methods=['GET', 'POST'])
def go_to_buy_page():
	print(request.form)
	if "seeBuyerView" in request.form:
		template_data = {}
		sql = "select user_id, price from swipes2 order by price"
		swipes = db_query(sql)
		template_data['swipes'] = swipes
		print(swipes)
		return render_template('buyPage.html', template_data=template_data)
		#return ''

@app.route('/goToSellPage', methods=['GET', 'POST'])
def go_to_sell_page():
	print(request.form)
	if "seeSellerView" in request.form:
		return render_template('sellPage.html'), 400
	else:
		return ''

if __name__ == '__main__':
    app.run()
    #app.run(**config['app']) will probably need this one rather than app.run()