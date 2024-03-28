#!/usr/bin/env python
# encoding: utf-8

import json
import random
from pymongo import MongoClient

databaseAddress = "127.0.0.1"
databaseName = "topaz_bi"
databaseTable = "dut_running"
connection = MongoClient(databaseAddress, 27017)
db = connection[databaseName]
status_runtime = db[databaseTable]

def delete_test_data():
    for i in range(0,128):
        filter = {"_id": i}
        status_runtime.delete_one(filter)

if __name__ == "__main__":
    delete_test_data()

