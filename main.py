from flask import request
from flask import jsonify
from loader import *
from sqliteMode import *
from routes import *



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

try:
    con.commit()
    con.close()
except:
    pass
