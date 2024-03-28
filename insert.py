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
data_pattern = {
    "_id" : 54,
    "STATUS" : 1,
    "PWRCYCS" : 6,
    "PCA" : "00000000",
    "PCBVER" : "000Rev02",
    "CYCLES7" : [ 
        {
            "READINESS" : 12,
            "RESERVED" : 30,
            "TEMP" : 31,
            "PGEMSTAT" : 1,
            "VIN" : 113,
            "VCAP" : 38,
            "VC1" : 37,
            "VC2" : 32,
            "VC3" : 31,
            "VC4" : 30,
            "VC5" : 31,
            "VC6" : 30,
            "TIME" : 0.07694506645202637
        }, 
        {
            "READINESS" : 12,
            "RESERVED" : 33,
            "TEMP" : 31,
            "TIME" : 3.164654016494751,
            "VIN" : 113,
            "VC2" : 35,
            "VC1" : 40,
            "VCAP" : 42,
            "VC3" : 34,
            "VC4" : 33,
            "VC5" : 34,
            "VC6" : 33,
            "PGEMSTAT" : 1
        }, 
        {
            "READINESS" : 12,
            "RESERVED" : 36,
            "TEMP" : 26,
            "PGEMSTAT" : 1,
            "VIN" : 113,
            "VCAP" : 45,
            "VC1" : 42,
            "VC2" : 38,
            "VC3" : 37,
            "VC4" : 36,
            "VC5" : 36,
            "VC6" : 36,
            "TIME" : 6.253992080688477
        }, 
        {
            "READINESS" : 12,
            "RESERVED" : 39,
            "TEMP" : 26,
            "TIME" : 9.340019941329956,
            "VIN" : 113,
            "VC2" : 42,
            "VC1" : 45,
            "VCAP" : 48,
            "VC3" : 39,
            "VC4" : 39,
            "VC5" : 39,
            "VC6" : 39,
            "PGEMSTAT" : 1
        }, 
        {
            "READINESS" : 12,
            "RESERVED" : 41,
            "TEMP" : 26,
            "PGEMSTAT" : 1,
            "VIN" : 113,
            "VCAP" : 51,
            "VC1" : 47,
            "VC2" : 43,
            "VC3" : 42,
            "VC4" : 41,
            "VC5" : 42,
            "VC6" : 41,
            "TIME" : 12.43994307518005
        }, 
        {
            "READINESS" : 12,
            "RESERVED" : 44,
            "TEMP" : 26,
            "TIME" : 15.53192901611328,
            "VIN" : 113,
            "VC2" : 46,
            "VC1" : 49,
            "VCAP" : 55,
            "VC3" : 45,
            "VC4" : 44,
            "VC5" : 45,
            "VC6" : 44,
            "PGEMSTAT" : 1
        }, 
        {
            "READINESS" : 12,
            "RESERVED" : 47,
            "TEMP" : 27,
            "PGEMSTAT" : 1,
            "VIN" : 113,
            "VCAP" : 58,
            "VC1" : 52,
            "VC2" : 48,
            "VC3" : 48,
            "VC4" : 47,
            "VC5" : 47,
            "VC6" : 47,
            "TIME" : 18.62094902992249
        }, 
        {
            "READINESS" : 12,
            "RESERVED" : 49,
            "TEMP" : 27,
            "TIME" : 21.7098400592804,
            "VIN" : 113,
            "VC2" : 51,
            "VC1" : 54,
            "VCAP" : 61,
            "VC3" : 50,
            "VC4" : 49,
            "VC5" : 50,
            "VC6" : 49,
            "PGEMSTAT" : 1
        }, 
        {
            "READINESS" : 12,
            "RESERVED" : 52,
            "TEMP" : 27,
            "PGEMSTAT" : 1,
            "VIN" : 113,
            "VCAP" : 64,
            "VC1" : 56,
            "VC2" : 53,
            "VC3" : 53,
            "VC4" : 52,
            "VC5" : 52,
            "VC6" : 52,
            "TIME" : 24.80233502388
        }, 
        {
            "READINESS" : 12,
            "RESERVED" : 55,
            "TEMP" : 27,
            "TIME" : 27.89362215995789,
            "VIN" : 113,
            "VC2" : 56,
            "VC1" : 58,
            "VCAP" : 67,
            "VC3" : 56,
            "VC4" : 54,
            "VC5" : 55,
            "VC6" : 55,
            "PGEMSTAT" : 1
        }, 
        {
            "READINESS" : 12,
            "RESERVED" : 57,
            "TEMP" : 27,
            "PGEMSTAT" : 1,
            "VIN" : 113,
            "VCAP" : 70,
            "VC1" : 60,
            "VC2" : 58,
            "VC3" : 58,
            "VC4" : 57,
            "VC5" : 58,
            "VC6" : 57,
            "TIME" : 30.97643709182739
        }, 
        {
            "READINESS" : 12,
            "RESERVED" : 60,
            "TEMP" : 28,
            "TIME" : 34.06638693809509,
            "VIN" : 113,
            "VC2" : 61,
            "VC1" : 63,
            "VCAP" : 73,
            "VC3" : 61,
            "VC4" : 60,
            "VC5" : 60,
            "VC6" : 60,
            "PGEMSTAT" : 1
        }, 
        {
            "READINESS" : 12,
            "RESERVED" : 62,
            "TEMP" : 28,
            "PGEMSTAT" : 1,
            "VIN" : 113,
            "VCAP" : 76,
            "VC1" : 65,
            "VC2" : 63,
            "VC3" : 63,
            "VC4" : 62,
            "VC5" : 63,
            "VC6" : 62,
            "TIME" : 37.15418100357056
        }, 
        {
            "READINESS" : 12,
            "RESERVED" : 64,
            "TEMP" : 28,
            "TIME" : 40.23964715003967,
            "VIN" : 113,
            "VC2" : 66,
            "VC1" : 67,
            "VCAP" : 78,
            "VC3" : 66,
            "VC4" : 65,
            "VC5" : 65,
            "VC6" : 64,
            "PGEMSTAT" : 1
        }, 
        {
            "READINESS" : 12,
            "RESERVED" : 67,
            "TEMP" : 28,
            "PGEMSTAT" : 1,
            "VIN" : 113,
            "VCAP" : 81,
            "VC1" : 69,
            "VC2" : 68,
            "VC3" : 68,
            "VC4" : 67,
            "VC5" : 67,
            "VC6" : 67,
            "TIME" : 43.32546305656433
        }, 
        {
            "READINESS" : 12,
            "RESERVED" : 69,
            "TEMP" : 28,
            "TIME" : 46.42251110076904,
            "VIN" : 113,
            "VC2" : 70,
            "VC1" : 71,
            "VCAP" : 84,
            "VC3" : 70,
            "VC4" : 70,
            "VC5" : 70,
            "VC6" : 69,
            "PGEMSTAT" : 1
        }, 
        {
            "READINESS" : 12,
            "RESERVED" : 72,
            "TEMP" : 29,
            "PGEMSTAT" : 1,
            "VIN" : 113,
            "VCAP" : 87,
            "VC1" : 73,
            "VC2" : 73,
            "VC3" : 73,
            "VC4" : 72,
            "VC5" : 72,
            "VC6" : 72,
            "TIME" : 49.50604009628296
        }, 
        {
            "READINESS" : 12,
            "RESERVED" : 74,
            "TEMP" : 29,
            "TIME" : 52.59913897514343,
            "VIN" : 113,
            "VC2" : 75,
            "VC1" : 75,
            "VCAP" : 90,
            "VC3" : 75,
            "VC4" : 74,
            "VC5" : 75,
            "VC6" : 74,
            "PGEMSTAT" : 1
        }, 
        {
            "READINESS" : 12,
            "RESERVED" : 76,
            "TEMP" : 29,
            "PGEMSTAT" : 1,
            "VIN" : 113,
            "VCAP" : 92,
            "VC1" : 77,
            "VC2" : 78,
            "VC3" : 77,
            "VC4" : 77,
            "VC5" : 77,
            "VC6" : 76,
            "TIME" : 55.69489598274231
        }, 
        {
            "READINESS" : 12,
            "RESERVED" : 79,
            "TEMP" : 29,
            "TIME" : 58.78784394264221,
            "VIN" : 113,
            "VC2" : 80,
            "VC1" : 79,
            "VCAP" : 95,
            "VC3" : 80,
            "VC4" : 79,
            "VC5" : 79,
            "VC6" : 79,
            "PGEMSTAT" : 1
        }, 
        {
            "READINESS" : 12,
            "RESERVED" : 81,
            "TEMP" : 30,
            "PGEMSTAT" : 1,
            "VIN" : 113,
            "VCAP" : 98,
            "VC1" : 81,
            "VC2" : 82,
            "VC3" : 82,
            "VC4" : 81,
            "VC5" : 81,
            "VC6" : 81,
            "TIME" : 61.87822008132935
        }, 
        {
            "READINESS" : 12,
            "RESERVED" : 83,
            "TEMP" : 30,
            "TIME" : 64.96771812438965,
            "VIN" : 113,
            "VC2" : 84,
            "VC1" : 83,
            "VCAP" : 101,
            "VC3" : 84,
            "VC4" : 84,
            "VC5" : 84,
            "VC6" : 83,
            "PGEMSTAT" : 1
        }, 
        {
            "READINESS" : 12,
            "RESERVED" : 86,
            "TEMP" : 30,
            "PGEMSTAT" : 1,
            "VIN" : 113,
            "VCAP" : 103,
            "VC1" : 85,
            "VC2" : 87,
            "VC3" : 87,
            "VC4" : 86,
            "VC5" : 86,
            "VC6" : 86,
            "TIME" : 68.05410599708557
        }, 
        {
            "READINESS" : 12,
            "RESERVED" : 88,
            "TEMP" : 30,
            "TIME" : 71.14337515830994,
            "VIN" : 113,
            "VC2" : 89,
            "VC1" : 87,
            "VCAP" : 106,
            "VC3" : 89,
            "VC4" : 88,
            "VC5" : 88,
            "VC6" : 88,
            "PGEMSTAT" : 1
        }, 
        {
            "READINESS" : 12,
            "RESERVED" : 90,
            "TEMP" : 30,
            "PGEMSTAT" : 1,
            "VIN" : 113,
            "VCAP" : 109,
            "VC1" : 89,
            "VC2" : 91,
            "VC3" : 91,
            "VC4" : 91,
            "VC5" : 90,
            "VC6" : 90,
            "TIME" : 74.23203611373901
        }, 
        {
            "READINESS" : 12,
            "RESERVED" : 92,
            "TEMP" : 31,
            "TIME" : 77.31913614273071,
            "VIN" : 113,
            "VC2" : 93,
            "VC1" : 91,
            "VCAP" : 111,
            "VC3" : 93,
            "VC4" : 93,
            "VC5" : 93,
            "VC6" : 92,
            "PGEMSTAT" : 1
        }, 
        {
            "READINESS" : 143,
            "RESERVED" : 95,
            "TEMP" : 31,
            "PGEMSTAT" : 0,
            "VIN" : 113,
            "VCAP" : 114,
            "VC1" : 93,
            "VC2" : 95,
            "VC3" : 96,
            "VC4" : 95,
            "VC5" : 95,
            "VC6" : 95,
            "TIME" : 80.41866898536682
        }, 
        {
            "READINESS" : 143,
            "RESERVED" : 97,
            "TEMP" : 31,
            "TIME" : 83.51403594017029,
            "VIN" : 113,
            "VC2" : 97,
            "VC1" : 95,
            "VCAP" : 116,
            "VC3" : 97,
            "VC4" : 97,
            "VC5" : 97,
            "VC6" : 97,
            "PGEMSTAT" : 0
        }, 
        {
            "READINESS" : 4,
            "RESERVED" : 97,
            "TEMP" : 31,
            "PGEMSTAT" : 10,
            "VIN" : 114,
            "VCAP" : 117,
            "VC1" : 95,
            "VC2" : 98,
            "VC3" : 98,
            "VC4" : 98,
            "VC5" : 97,
            "VC6" : 97,
            "TIME" : 0.06919097900390625
        }, 
        {
            "READINESS" : 4,
            "RESERVED" : 87,
            "TEMP" : 31,
            "TIME" : 3.159016847610474,
            "VIN" : 3,
            "VC2" : 87,
            "VC1" : 77,
            "VCAP" : 103,
            "VC3" : 88,
            "VC4" : 88,
            "VC5" : 87,
            "VC6" : 87,
            "PGEMSTAT" : 10
        }, 
        {
            "READINESS" : 4,
            "RESERVED" : 79,
            "TEMP" : 31,
            "PGEMSTAT" : 10,
            "VIN" : 2,
            "VCAP" : 94,
            "VC1" : 70,
            "VC2" : 80,
            "VC3" : 80,
            "VC4" : 80,
            "VC5" : 79,
            "VC6" : 79,
            "TIME" : 6.255005836486816
        }, 
        {
            "READINESS" : 4,
            "RESERVED" : 71,
            "TEMP" : 31,
            "TIME" : 9.347369909286499,
            "VIN" : 2,
            "VC2" : 72,
            "VC1" : 63,
            "VCAP" : 84,
            "VC3" : 72,
            "VC4" : 71,
            "VC5" : 71,
            "VC6" : 71,
            "PGEMSTAT" : 10
        }, 
        {
            "READINESS" : 4,
            "RESERVED" : 63,
            "TEMP" : 31,
            "PGEMSTAT" : 10,
            "VIN" : 1,
            "VCAP" : 75,
            "VC1" : 56,
            "VC2" : 64,
            "VC3" : 64,
            "VC4" : 63,
            "VC5" : 63,
            "VC6" : 63,
            "TIME" : 12.4387378692627
        }, 
        {
            "READINESS" : 4,
            "RESERVED" : 54,
            "TEMP" : 31,
            "TIME" : 15.53131580352783,
            "VIN" : 1,
            "VC2" : 56,
            "VC1" : 49,
            "VCAP" : 65,
            "VC3" : 56,
            "VC4" : 55,
            "VC5" : 55,
            "VC6" : 54,
            "PGEMSTAT" : 10
        }, 
        {
            "READINESS" : 4,
            "RESERVED" : 46,
            "TEMP" : 31,
            "PGEMSTAT" : 10,
            "VIN" : 1,
            "VCAP" : 55,
            "VC1" : 42,
            "VC2" : 47,
            "VC3" : 47,
            "VC4" : 46,
            "VC5" : 47,
            "VC6" : 46,
            "TIME" : 18.62239503860474
        }, 
        {
            "READINESS" : 4,
            "RESERVED" : 37,
            "TEMP" : 31,
            "TIME" : 21.71210885047913,
            "VIN" : 1,
            "VC2" : 39,
            "VC1" : 34,
            "VCAP" : 45,
            "VC3" : 39,
            "VC4" : 37,
            "VC5" : 38,
            "VC6" : 37,
            "PGEMSTAT" : 10
        }
    ],
    "FWVER" : "1.1.0.00",
    "HWVER" : "000Rev01",
    "ENDUSR" : "AGIGA-02",
    "LASTCAP" : 255,
    "CAPPN" : "51040095",
    "SN" : "00000110",
    "CINT" : 46,
    "MODEL" : "501DCB00",
    "MFDATE" : "00001344"
}

def push_test_data(data):
    for i in range(0,128):
        data = data_pattern
        data["_id"] = i
        data["STATUS"] = random.randint(1, 5)
        for j in data["CYCLES7"]:
            j["VCAP"] = round(random.uniform(1,40),2)
            j["TEMP"] = round(random.uniform(1,40),2)
        status_runtime.insert_one(data)

if __name__ == "__main__":
    push_test_data(data_pattern)