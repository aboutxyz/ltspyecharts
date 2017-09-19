#! python2
#coding:utf-8

import pymongo
from bson.son import SON
connection = pymongo.MongoClient("localhost", 27017)
db = connection.ltsdata
collection = db.data


voyagename = ['CAT','NEAX','PAN NKT1','SITC NJ1','SITC NA1','SCT', 'NT1','ST2','CPS','CPF','CHS','CTI','EASNSP']
pipeline = [{"$group": {"_id" :{"voyage":"$航线"} , "count": {"$sum": "$TEU"}}}]
voyagelist = list(collection.aggregate(pipeline))
voyagelist.sort(key=lambda x:voyagename.index(x['_id']['voyage']))

print [i['count'] for i in voyagelist]