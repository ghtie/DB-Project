# application to run program from terminal

import configparser
from flask import Flask, render_template, request
import mysql.connector

config = configparser.ConfigParse()
config.read('config.ini')

app = Flask(__name_)

if __name__ == '__main__':
    app.run()