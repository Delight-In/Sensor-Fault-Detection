from pymongo.mongo_client import MongoClient
import pandas as pd
import json
from src.constant import *


#create a new client and connectt to server
client = MongoClient(MONGO_DB_URL)

#create database name and collection name
DATABASE_NAME="Sensor"
COLLECTION_NAME='waferfault'

df=pd.read_csv(r"G:\PROJECT2_SENSOR_FAULT_DETECTOR\dataset\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0",axis=1)

json_record=list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)