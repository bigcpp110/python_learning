from pymongo import MongoClient
conn=MongoClient(host="localhost",port=27017)
db=conn.mydb
my_set=db.test_set
my_set.insert_one({"name":"zhangsan","age":18})
users=[{"name":"zhangsan","age":18},{"name":"lisi","age":20}]  
my_set.insert_many(users) 

for i in my_set.find():
    print(i)
#查询name=zhangsan的
for i in my_set.find({"name":"zhangsan"}):
    print(i)
print(my_set.find_one({"name":"zhangsan"}))
my_set.update({"name":"zhangsan"},{'$set':{"age":20}})