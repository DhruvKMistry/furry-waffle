from flask import Flask, render_template,request
import os
import sqlite3 as sql

app = Flask(__name__)
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')

def changedata(data):
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
            elif row[3]==i[0] and row[4]==i[1]:
                i[2]+=row[5]
                flag1=1
        if flag==0 and row[2]:
            Final_data.append([row[2],row[4],-1*row[5]])
        if flag1==0 and row[3]:
            Final_data.append([row[3],row[4],row[5]])
    return Final_data

@app.route('/')
def index():
    con = sql.connect('db.sqlite3')
    cur = con.cursor()
    cur.execute("""SELECT * FROM ProductMovement""")
    cur_data=cur.fetchall()
    con.close() 
    data=[]
    for row in cur_data:
        data_temp = [row[0], row[1], row[2],row[3],row[4],row[5]]
        data.append(data_temp)
    regiondata = changedata(data)
    return render_template("View.html",data=data,data1=regiondata)
 
    

    
@app.route('/location',methods=['POST'])
def location():
    location =request.form['location']
    con = sql.connect('db.sqlite3')
    cur = con.cursor()
    cur.execute("INSERT INTO Location (location_id) VALUES (?)",(location,))
    con.commit()
    con.close()
    return (index())

@app.route('/product',methods=['POST'])
def product():
    product =request.form['product']
    con = sql.connect('db.sqlite3')
    cur = con.cursor()
    cur.execute("INSERT INTO Product (product_id) VALUES (?)",(product,))
    con.commit()
    con.close()
    return (index())

@app.route('/productmovment',methods=['POST'])
def productmovment():
    movement_id =request.form['movement']
    from_location =request.form['from']
    to_location =request.form['to']
    product_id =request.form['product']
    qty =request.form['qty']
    if (not from_location) and (not to_location):
        print('1')
        return (index())

    if from_location:
        if not checkloc(from_location):
            print('2')
            return (index())
            
    
    if to_location:
        if not checkloc(to_location):
            print('3')
            return (index())
    
    if not checkprod(product_id) or qty=="0":
        print('4')
        return (index())

    con = sql.connect('db.sqlite3')
    cur = con.cursor()
    cur.execute("INSERT INTO ProductMovement (movement_id, from_location, to_location, product_id, qty) VALUES (?,?,?,?,?)",(movement_id, from_location, to_location, product_id, qty,))
    con.commit()
    con.close()
    return (index())

if __name__ == '__main__':
    app.run(debug=True)

def checkprod(product_id):
    con = sql.connect('db.sqlite3')
    cur = con.cursor()
    cur.execute("SELECT * FROM Product WHERE product_id=? ",(product_id,))
    if cur.fetchall():
        con.commit()
        con.close()
        return True
    else:
        con.commit()
        con.close()
        return False

def checkloc(location_id):
    con = sql.connect('db.sqlite3')
    cur = con.cursor()
    cur.execute("SELECT * FROM Location WHERE location_id=? ",(location_id,))
    
    if cur.fetchall():
        con.commit()
        con.close()
        return True
    else:
        con.commit()
        con.close()
        return False


