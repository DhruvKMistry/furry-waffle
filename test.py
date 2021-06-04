import os
import sqlite3 as sql
import pandas as pd
import numpy as np

con = sql.connect('db.sqlite3')
cur = con.cursor()
'''
customers_sql ="""DROP TABLE ProductMovement"""
cur.execute(customers_sql)
customers_sql = """CREATE TABLE ProductMovement ( movement_id varchar PRIMARY KEY, timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ,  from_location varchar ,  to_location varchar ,  product_id varchar, qty integer) """
cur.execute(customers_sql)

customers_sql ="""DROP TABLE Product"""
cur.execute(customers_sql)
customers_sql = """CREATE TABLE Product ( product_id varchar  PRIMARY KEY) """
cur.execute(customers_sql)

customers_sql ="""DROP TABLE Location"""
cur.execute(customers_sql)
customers_sql = """CREATE TABLE Location ( location_id varchar  PRIMARY KEY) """
cur.execute(customers_sql)
'''
'''
location_id='bhopal'
con = sql.connect('db.sqlite3')
cur = con.cursor()
cur.execute("SELECT * FROM Location WHERE location_id=?",(location_id,))
    
if cur.fetchall():
    con.commit()
    con.close()
    print(True)
else:
    con.commit()
    con.close()
    print(False)
'''
'''
con = sql.connect('db.sqlite3')
cur = con.cursor()
cur.execute("DELETE FROM Location")
cur.execute("DELETE FROM Product")
cur.execute("DELETE FROM ProductMovement")
con.commit()
con.close()
'''
'''
def regiondata(data):
    Final_data = []
    print(data)
    for i in data:
        if i[3]:
            print('1')
            if i[3]+' '+i[4] in Final_data:
                Final_data[Final_data.index(i[3]+' '+i[4])][1]=Final_data[Final_data.index(i[3]+' '+i[4])][1]+i[5]
                print("index",Final_data.index(i[3]+' '+i[4]))
                print('1.1')
            else:
                Final_data.append([i[3]+' '+i[4],i[5]])
                print('1.2')
        if i[2]:
            print('2')
            if i[2]+' '+i[4] in Final_data:
                if Final_data[Final_data.index(i[2]+' '+i[4])][1]>=i[5]:
                    Final_data[Final_data.index(i[2]+' '+i[4])][1]=Final_data[Final_data.index(i[2]+' '+i[4])][1]-i[3]
                    print('2.1')
                else:
                    print('2.2')
                    Final_data[Final_data.index(i[1]+' '+i[2])][1]=0
            else:
                print('3')
                Final_data.append([i[2]+' '+i[4],0])
        print(Final_data)
        print(i[2]+i[3]+i[4])
        print(type(i[2]+i[3]+i[4]))
        
    print(Final_data)
    return True

con = sql.connect('db.sqlite3')
cur = con.cursor()
cur.execute("""SELECT * FROM ProductMovement""")
cur_data=cur.fetchall()
con.close() 
data=[]
for row in cur_data:
    data_temp = [row[0], row[1], row[2],row[3],row[4],row[5]]
    data.append(data_temp)

regiondata = regiondata(data)
'''
'''
con = sql.connect('db.sqlite3')
cur = con.cursor()
cur.execute("""SELECT * FROM ProductMovement""")
cur_data=cur.fetchall()
con.close() 
data=[]
for row in cur_data:
    data_temp = [row[0], row[1], row[2],row[3],row[4],int(row[5])]
    data.append(data_temp)
data.append(["","","Vadodara","Bhopal","D13",2])
data.append(["","","Bhopal","","S14",2])
data1 = pd.DataFrame(data=data)
data1 = data1.iloc[:,2:]
data1_1 =data1.iloc[:,[0,2,3]]
data2 = data1_1.groupby([2, 4])[5].sum()
data3 = data2.where(fill1 & fill2, inplace = True)
#data2 = data2[data2.duplicated()]
#print(data1)
print(data1_1)
print(data2)
print(data3)
'''
con = sql.connect('db.sqlite3')
cur = con.cursor()
cur.execute("""SELECT * FROM ProductMovement""")
cur_data=cur.fetchall()
con.close() 
data=[]
for row in cur_data:
    data_temp = [row[0], row[1], row[2],row[3],row[4],int(row[5])]
    data.append(data_temp)

Final_data=[]

for row in data:
    flag=0
    flag1=0
    print(row)
    for i in Final_data:
        print(i)
        if row[2]==i[0] and i[1]==row[4]:
            i[2]-=row[5]
            flag=1
            print("1")
        elif row[3]==i[0] and row[4]==i[1]:
            i[2]+=row[5]
            flag1=1
            print("2")
    if flag==0:
        Final_data.append([row[2],row[4],row[5]])
        print("3")
    if flag1==0:
        Final_data.append([row[3],row[4],row[5]])
        print("3")

print(Final_data)