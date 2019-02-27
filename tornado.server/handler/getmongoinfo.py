import pymongo
import csv

import os



mongo_url = "127.0.0.1:27017"
DATABASE = "UserStudyT"
TABLE = "resultinfo2"

client = pymongo.MongoClient(mongo_url)
db_des = client[DATABASE]
db_des_collectionname = db_des[TABLE]

with open(f"{DATABASE}_{TABLE}.csv", "w", newline='') as csvfileWriter:
    writer = csv.writer(csvfileWriter)

    fieldList = [
        "_id"
    ]
    for i in range(7,82,2):
        fieldList.append(str(i)+".png")
    writer.writerow(fieldList)

    allRecordRes = db_des_collectionname.find()

    for record in allRecordRes:
        # print("record", record)
        recordValueLst = []
        if fieldList[0] in record:
            recordValueLst.append(record[fieldList[0]])
            cutFieldList = fieldList[1:]
            answerinfo = record["answerinfo"]
            for field in cutFieldList:
                for i in range(len(answerinfo)):
                    if field == answerinfo[i]["imgname"]:
                        recordValueLst.append(answerinfo[i]["answer"])
                        break
            try:
                writer.writerow(recordValueLst)
                print("ggggg")
            except Exception as e:
                print(f"write csv exception. e = {e}")
