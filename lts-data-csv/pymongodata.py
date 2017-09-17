#! python2
#coding:utf-8

import pymongo
from bson.son import SON
from collections import Counter,OrderedDict
connection = pymongo.MongoClient("localhost", 27017)
db = connection.ltsdata
collection = db.data


voyagename = ['CAT','NEAX','PAN NKT1','SITC NJ1','SITC NA1','SCT', 'NT1','ST2','CPS','CPF','CHS','CTI','EASNSP']

pipeline = [{"$group": {"_id" :{"voyage":"$航线"} , "count": {"$sum": "$TEU"}}}]

datadict= {}
for j in list(collection.aggregate(pipeline)):
    datadict[j["_id"]["voyage"]] = j["count"]

datalist = []
for i in voyagename:
    datalist.append(datadict[i])
print datalist