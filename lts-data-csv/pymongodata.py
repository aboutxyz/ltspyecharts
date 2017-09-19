%%time
#! python2
#coding:utf-8

import pymongo
from bson.son import SON
from collections import Counter,OrderedDict
import operator
connection = pymongo.MongoClient("localhost", 27017)
db = connection.ltsdata
collection = db.data


voyagename = ['CAT','NEAX','PAN NKT1','SITC NJ1','SITC NA1','SCT', 'NT1','ST2','CPS','CPF','CHS','CTI','EASNSP']
pipeline = [{"$group": {"_id" :{"voyage":"$航线"} , "count": {"$sum": "$TEU"}}}]
voyagelist = list(collection.aggregate(pipeline))
voyagelist.sort(key=lambda x:voyagename.index(x['_id']['voyage']))
datalist =[]
for i in voyagelist:
    datalist.append(i['count'])
print datalist

# datalist = [0 for i in range(len(voyagename))]
# for i in list(collection.aggregate(pipeline)):
    # if i["_id"]["voyage"] in voyagename:
        # datalist[voyagename.index(i["_id"]["voyage"])] = i["count"]
        
# print datalist


# 试试json