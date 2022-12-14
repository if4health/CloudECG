import json
import numpy as np
from biosppy.signals import ecg
import os

import sys

# from pymongo import MongoClient
from bson.objectid import ObjectId

# from dotenv import load_dotenv, find_dotenv
# import certifi

# load_dotenv(find_dotenv())

# Get the database using the method we defined in pymongo_test_insert file 
from db_connect import get_database
dbname = get_database()

# Create a new collection
collection_name = dbname['qual_collection']


if(len(sys.argv) == 1):
    raise Exception("cade o id seu bobao?")

query = {"_id": ObjectId(sys.argv[1])}

# dbClient = MongoClient(os.environ.get("MONGO_DB_URL"), tlsCAFile=certifi.where()).get_default_database()


bolo = dbname.exams.find_one(query)



out = ecg.ecg(signal=bolo["data"], sampling_rate=bolo["sampling_rate"], show=False)


class NDArrayEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


json_str = json.dumps({"filtered" : out['filtered'], 'rpeaks': out["rpeaks"],'bpm' :out["heart_rate"], "rate": bolo["sampling_rate"]}, cls=NDArrayEncoder)

print(json_str)

# f = 1/T
