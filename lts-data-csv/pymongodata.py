%%time
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

datalist = [0 for i in range(len(voyagename))]
for i in list(collection.aggregate(pipeline)):
    if i["_id"]["voyage"] in voyagename:
        datalist[voyagename.index(i["_id"]["voyage"])] = i["count"]
        
print datalist

# datadict= {}
# for j in list(collection.aggregate(pipeline)):
    # datadict[j["_id"]["voyage"]] = j["count"]
# print sorted(datadict.iteritems(),key = lambda x:voyagename.index(x[0]))


# 试试json