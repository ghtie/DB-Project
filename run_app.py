# application to run program from terminal
from __future__ import print_function
from mysql.connector import errorcode
from decimal import Decimal

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

#Funtion that inserts into a table
def db_insert(sql, val):
	cnx = mysql.connector.connect(**config['mysql.connector'])
	cursor = cnx.cursor()
	cursor.execute(sql, val)
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
		return display_swipes_for_buyer(swipe_view_data, guest_id_counter=guest_id_counter)

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
			return display_swipes_for_buyer(buy_view_data, guest_id_counter=guest_id_counter)

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

def display_swipes_for_buyer(dictionary, guest_id_counter):
	dictionary = {}
	sql = "select id, quantity, price from swipes where status=0 order by price"
	swipes = db_query(sql)
	sql2 = "select (sum(price)/sum(quantity)), sum(quantity) from swipes where status=0"
	data = db_query(sql2)
	dataAvg = data[0][0]
	dataSum = data[0][1]
	dictionary['swipes'] = swipes
	print(swipes)
	return render_template('buyPage.html', template_data=dictionary, dataAvg=dataAvg, dataSum=dataSum, guest_id_counter=guest_id_counter)


@app.route('/goToSellPage', methods=['GET', 'POST'])
def go_to_sell_page():
	print(request.form)
	if "seeSellerView" in request.form:
		return render_template('sellerLogin.html'), 400
	else:
		return ''

@app.route('/createListing', methods=['GET', 'POST'])
def add_seller_info():
	if "sendSellerInfo" in request.form:
		name = str(request.form["name"])
		id = str(request.form["caseID"])
		sql = "insert into user (name, id) values (%s, %s)"
		val = (name, id)
		db_insert(sql, val)
		return render_template('sellerList.html'), 400

@app.route('/submitSwipes', methods=['GET', 'POST'])
def add_swipe_listing():
	if "sendListing" in request.form:
		id = str(request.form["caseID"])
		quantity = int(request.form["quantity"])
		price = Decimal(request.form["price"])
		sql = "insert into swipes (user_id, price, quantity) values (%s, %s, %s)"
		val = (id, price, quantity)
		db_insert(sql, val)
		return render_template('sellerLogin.html'), 400


if __name__ == '__main__':
    app.run()
    #app.run(**config['app']) will probably need this one rather than app.run()
