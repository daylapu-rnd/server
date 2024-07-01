from flask import Flask
from flask import jsonify
from flask import request
import sqlite3 as sq
import os

from utils import *


# create flask object
app = Flask(__name__)

db_path = 'bd.db'

# Check if database exists, create if it doesn't
if not os.path.exists(db_path):
    with open(db_path, 'w') as f:
        pass

# Connecting to a database and creating a cursor
con = sq.connect(db_path, check_same_thread=False)
cur = con.cursor()
