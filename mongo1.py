from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['poop']
 
collection = db['lol'] 

import datetime

post = {"name": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
post_id
ObjectId('...')

db.collection_names(include_system_collections=False)
[u'posts']			
