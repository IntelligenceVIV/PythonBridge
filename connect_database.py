# @Time    : 2019/4/18 6:34
# @Author  : Noah
# @File    : connect_database.py
# @Software: PyCharm
# @description: connect to database
#####################################################################################
# MySQL

# CREATE TABLE `users` (
#     `id` int(11) NOT NULL AUTO_INCREMENT,
#     `email` varchar(255) COLLATE utf8_bin NOT NULL,
#     `password` varchar(255) COLLATE utf8_bin NOT NULL,
#     PRIMARY KEY (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin
# AUTO_INCREMENT=1 ;

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='147258',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()

# Final output: {'id': 1, 'password': 'very-secret'}
#####################################################################################
# mongoDB

import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.test

print(db.name)

print(db.my_collection)

print(db.my_collection.insert_one({"x": 10}).inserted_id)

print(db.my_collection.insert_one({"x": 8}).inserted_id)

print(db.my_collection.insert_one({"x": 11}).inserted_id)

print(db.my_collection.find_one())

for item in db.my_collection.find():
    print(item["x"])

print(db.my_collection.create_index("x"))

for item in db.my_collection.find().sort("x", pymongo.ASCENDING):
    print(item["x"])

print([item["x"] for item in db.my_collection.find().limit(2).skip(1)])

#####################################################################################
# postgresql

import psycopg2

# Connect to an existing database
conn = psycopg2.connect(database="test",
                        user="postgres",
                        password="147258",
                        host="127.0.0.1",
                        port="5432")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))

# Query the database and obtain data as Python objects
cur.execute("SELECT * FROM test;")
print(cur.fetchone())

# Make the changes to the database persistent
conn.commit()

# Close communication with the database
cur.close()
conn.close()

#####################################################################################
# Redis

from redis import StrictRedis

r = StrictRedis(host='localhost', port=6379, db=0, password=None)
r.set('foo', 'bar')
print(r.get('foo'))

#####################################################################################
