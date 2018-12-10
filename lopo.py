
from flask import Flask
from flask import request
from flask_pymongo import PyMongo
from pymongo import MongoClient
import datetime


app = Flask(__name__)


client = MongoClient('mongodb://localhost:27017')
db = client['db']
stuff = db.test   
  
  
  
  
@app.route('/', methods = ['POST'])

def postJsonHandler():
   
    print (request.is_json)
    content=request.get_json("content")
    pind = datetime.datetime.now()
    stuff.insert({ "ESP":content, "TIME":pind})
    print (content)
    return 'JSON RECEIVED'
      



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
