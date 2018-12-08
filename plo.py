from flask import Flask
from flask import request
from flask_pymongo import PyMongo
from pymongo import MongoClient
import datetime


app = Flask(__name__)
if __name__ == '__main__':
    app.run(host='192.168.56.1', port=5000)


@app.route('/', methods = ['POST'])

def postJsonHandler():
    content = request.get_json()
    print (content)
    return 'JSON posted'
    
    
    
    
client = MongoClient('mongodb://localhost:27017')
db = client['db']
collection = db.test  
x = 5
posts = db.test
post_data = {
    'title': ,
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
    }
result = posts.insert_one(post_data)
print('One post: {0}'.format(result.inserted_id))
   



