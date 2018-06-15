# TO ALLOW A USER ENTER DATA INTO A DATABASE WHILE THE CODE IS RUNNING.
print('DATABASE TO RECIEVE WEEKLY TEMPERATURE DATA AND COMPUTE THEIR AVERAGE! ')
a1 = input("enter date: ")
a = int(input("enter temperature on day 1: "))
b1 = input("enter date: ")
b = int(input("enter temperature on day 2: "))
c1 = input("enter date: ")
c = int(input("enter temperature on day 3: "))
d1 = input("enter date: ")
d = int(input("enter temperature on day 4: "))
e1 = input("enter date: ")
e = int(input("enter temperature on day 5: "))
f1 = input("enter date: ")
f = int(input("enter temperature on day 6: "))
g1 = input("enter date: ")
g = int(input("enter temperature on day 7: "))

# DATABASE PROGRAMMING
import sqlite3 as db
# CREATE DATABASE
kat = db.connect('TempTracker1.db') #creates database
cursor = kat.cursor() # to create a cursor
cursor.execute("drop table if exists tempdata") # checks if the table already exists and deletes it if true
# CREATE TABLE
cursor.execute("create table tempdata (serialNumber text, date text, temp int)") # creates the table
# UPDATE
cursor.execute("insert into tempdata values ('1.', '{}', '{}')".format(a1,a)) # inserts data into the table
cursor.execute("insert into tempdata values ('2.', '{}', '{}')".format(b1,b))
cursor.execute("insert into tempdata values ('3.', '{}', '{}')".format(c1,c))
cursor.execute("insert into tempdata values ('4.', '{}', '{}')".format(d1,d))
cursor.execute("insert into tempdata values ('5.', '{}', '{}')".format(e1,e))
cursor.execute("insert into tempdata values ('6.', '{}', '{}')".format(f1,f))
cursor.execute("insert into tempdata values ('7.', '{}', '{}')".format(g1,g))
# RETRIEVE
kat.row_factory = db.Row # to be able to select any column from table or all
cursor.execute('select * from tempdata') # to select from the table
rows = cursor.fetchall()  # to display every result
for row in rows:
    print("%s %s %s" % (row[0], row[1], row[2])) # to print
cursor.execute("select avg(temp) from tempdata") # TO COMPUTE AVARAGE
row = cursor.fetchone() # to display all data
print("the average temperature for the week was %s" % row[0]) # to print
# DELETE
h = int(input("the temperature to delete from the table: "))
cursor.execute("delete from tempdata where temp = {}".format(h)) # to delete from table
cursor.execute('select * from tempdata')
rows = cursor.fetchall()
for row in rows:
    print("%s %s %s" % (row[0], row[1], row[2]))
cursor.execute("select avg(temp) from tempdata") # TO COMPUTE AVARAGE
row = cursor.fetchone() # to displace just one result
print("the average temperature for the week was %s" % row[0]) # to print
kat.commit() # to return to the database the updated data.