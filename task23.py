# """
# date type 
# int
# string
# float
# list
# tuple
# """

import sqlite3

# create table

db = sqlite3.connect(r"E:\py_tasks\Tasks_python\python\elzero.db")

cr = db.cursor()

cr.execute("create table if not exists users (id integer unique,name text unique,bd text unique,mail text unique)")

my_number = [1, 2, 3, 4, 5]
my_name = ["ali", "ahmed", "omer", "mohammed", "minna"]
my_bd = ["10/2/2005", "10/2/2003", "10/11/2005", "24/11/2004", "1/1/2010"]
my_mali = ["ali453@gmail.com", "ahmed43@gmail.com", "omer43098@gmail.com", "mohammed278934@gmail.com", "minna890435@gmail.com"]

for i in range(len(my_number)):
    try:
        cr.execute(f"insert into users (id,name,bd,mail) values({my_number[i]},'{my_name[i]}','{my_bd[i]}','{my_mali[i]}')")
    except:
        print("this data is already exists")

user_input = int(input("enter the number : "))
cr.execute("select id from users")
id_list = cr.fetchall()
cr.execute("select * from users")
result = cr.fetchall()
# print(result[-1])
ids = []
for n in id_list:
    ids.extend(n)
if user_input in ids:
    cr.execute(f"delete from users where id = {user_input}")
    print("User Deleted.")
    print("Show Other Data:")
    for i in range(len(result) - 1):
            print(f"id => {result[i][0]}, name => {result[i][1]}, birth day => {result[i][2]}, mail => {result[i][3]}")
else:
    print("User is not found.")

db.commit()
db.close()