from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'




  

@app.route('/', methods=['POST'])
def posted_JSON():
    data = request.get_json()
    print(data)
    return 'JSON RECEIVED'
    
    
    
 myrecord = data 
    
record_id = mydb.mytable.insert(myrecord)    
    
if __name__ == '__main__':
    app.run(host='192.168.8.108', port=5000)
