# application to run program from terminal

import configparser
from flask import Flask, render_template, request
import mysql.connector

# read configuration from file
config = configparser.ConfigParser()
config.read('config.ini')

# set up application server
app = Flask(__name__)

# create a function for fetching data from database
def sql_query(sql):
    db = mysql.connector.connect(**config['mysql.connector'])
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result

def sql_execute(sql):
    db = mysql.connector.connect(**config['mysql.connector'])
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

# not sure if this is the best app.route function to use yet
@app.route('/')
def basic_response():
    return "Eyyyy, the web app runs!"

if __name__ == '__main__':
    app.run()