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

# global variable that increments every time someone enters the buying page from the landing page (keeps track of guest user ids)
guest_id_counter = -1
x = 1

# Define function to query database, returns result of query
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
	cnx.commit()
	cursor.close()
	cnx.close()

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/landingPage', methods=['GET', 'POST'])
def returnToLandingPage():
	print(request.form)
	if "goToLanding" in request.form:
		global x
		x = 1
		#print(hi)
		return render_template('home.html')

@app.route('/goToBuyPage', methods=['GET', 'POST'])
def go_to_buy_page():
	print(request.form)
	global guest_id_counter 
	sql = "select max(id) from guest_user"
	num = db_query(sql) # does not work if table null: will need to add if case for empty
	print(num[0][0])
	if num[0][0] is None:
		guest_id_counter = -1
	else:
		guest_id_counter = num[0][0]
	guest_id_counter = guest_id_counter + 1
	print(guest_id_counter)
	if "seeBuyerView" in request.form:
		swipe_view_data = {}
		return display_swipes_for_buyer(swipe_view_data)

@app.route('/viewSwipes', methods=['GET', 'POST'])
def buy_swipe():
		print(request.form)
		if "buy_swipe" in request.form:
			global guest_id_counter 
			swipe_id = int(request.form["buy_swipe"])
			sql = "update swipes set status=1 where id={swipe_id}".format(swipe_id=swipe_id)
			db_write(sql)
			global x
			if x == 1:
				sql2 = "insert into guest_user (id, name) values (%d, 'Bob')" % guest_id_counter
				db_write(sql2)
				x = 0
			sql3 = "update swipes set guest_user_id=%d where id=%s" % (guest_id_counter, swipe_id)
			db_write(sql3)
			buy_view_data = {}
			return display_swipes_for_buyer(buy_view_data)

# @app.route('/viewSwipes', methods=['GET', 'POST'])ß
# def buy_swipe():
# 		print(request.form)
# 		if "buy_swipe" in request.form:
# 			swipe_id = int(request.form["buy_swipe"])
# 			sql = "delete from swipes where id={swipe_id}".format(swipe_id=swipe_id)
# 			db_write(sql)
# 			# newsql = "select user_idß, price from swipes order by price"
# 			# swipes = db_query(newsql)
# 			# print(swipes)
# 			buy_view_data = {}
# 			return display_swipes(buy_view_data)

def display_swipes_for_buyer(dictionary):
	dictionary = {}
	sql = "select id, user_id, price from swipes where status=0 order by price"
	swipes = db_query(sql)
	dictionary['swipes'] = swipes
	print(swipes)
	return render_template('buyPage.html', template_data=dictionary)


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