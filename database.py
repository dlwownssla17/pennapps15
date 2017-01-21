from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

HOST = "localhost"
PORT = 27017

client = MongoClient(HOST, PORT)
db_songs = client["db_songs"]["songs"]

# cursor = db_songs.find()
# for document in cursor:
#     print(document['filename'])

# inserts a song into database and returns the inserted id
def insert(song):
    document = {"filename":     song.get_filename(),
                "name":         song.get_name(),
                "bpm":          song.get_bpm(),
                "artist":       song.get_artist(),
                "description":  song.get_description(),
                "date":         datetime.datetime.now()}
    return db_songs.insert_one(document).inserted_id

# returns a song instance matching the query id
def get(q_id):
    return db_songs.find_one({"_id": ObjectId(q_id)})

# returns multiple song instances matching the query ids
def get_many(q_ids):
    return db_songs.find({"$or": [{"_id": ObjectId(q_id)} for q_id in q_ids]})

# removes a song by query id and returns the raw result document from the db server
def remove(q_id):
    return db_songs.delete_one({"_id": ObjectId(q_id)}).raw_result

# updates a song by query id on its key and value and returns the raw result document from the server
def update(q_id, k, v):
    return db_songs.update_one({"_id": ObjectId(q_id)}, {"$set": {k: v}}, upsert=False).raw_result
