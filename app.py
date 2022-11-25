from pickle import FALSE
from flask import Flask, render_template, request, redirect, url_for, session
#import ibm_db
import json
import requests
app = Flask(__name__)
Dict = {'admin@gmail.com': 'welcome'} 
ListDict = [{'username': 'gishalin', 'password': 'rufina','email':'gishalin@gmail.com','mobile':954567899}]
prodDict = [{'productcode': 'P001', 'productname': 'cloths','productprice':200 ,'stock':1 }]
SalesDict = [{'productcode': 'P002', 'Quantitys': 2 ,'place':'Nagercoil'}]
totalproducts = len(prodDict)
# #conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=3883e7e4-18f5-4afe-be8c-fa31c41761d2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31498;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=sch83401;PWD=j7QZUHGAtUGbPhns",'','')
# conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=0c77d6f2-5da9-48a9-81f8-86b520b87518.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31198;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=tqz07844;PWD=8gtHDbCP5WHYQU9r",'','')
@app.route('/registration')
def registration():
    return render_template('register.html')
@app.route('/r1',methods=['POST'])
def r1():
    user = request.form['name']
    passw = request.form['passw']
    print(user,passw)
    account = True
    for i,j in Dict.items(): 
        if(i == user or j == passw):
           account = False
           break
    if account:
        return render_template('login.html', msg ="Already a member,login again")
    else:
       Dict.update({user: passw})
       return render_template('login.html', msg = 'registered') 

@app.route('/')    
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/loginpage',methods=['POST','GET'])
def loginpage():
    user = request.form['user']
    passw = request.form['passw']
    # sql = "SELECT * FROM user_detail WHERE username =? AND password=?"
    # stmt = ibm_db.prepare(conn, sql)
    # ibm_db.bind_param(stmt,1,user)
    # ibm_db.bind_param(stmt,2,passw)
    # ibm_db.execute(stmt)
    # account = ibm_db.fetch_assoc(stmt)
    # print (account)
    print(user,passw)
    account = False
    msg = "login here"
    value = user
    for i,j in Dict.items(): 
        if(i == user and j == passw):
           account = True
           break
    print(account)
    if account:
         return render_template('index.html', value = user,v1 = len(prodDict),totaluser = len(ListDict)) 
    else:
        msg = 'Incorrect username / password !'
        return render_template('login.html', msg = 'Incorrect username / password !') 


@app.route('/adduser')
def adduser():
    return render_template('buttons.html')
@app.route('/add',methods=['POST'])
def add():
    user = request.form['name']
    passw = request.form['passw']
    mobiles = request.form['mobile']
    emails = request.form['email']
    print(user,passw,mobiles,emails)
    if (user == "" or passw == "" or mobiles == "" or emails == ""):
        return render_template('buttons.html', msg ="Fill all the values")
    else:
       dt = {'username': user, 'password': passw,'email':emails ,'mobile':mobiles}
       ListDict.append(dt)
       print(len(ListDict))
       Dict.update({user: passw})
       print(len(Dict))
       return redirect(url_for('stats'))


@app.route('/addproduct')
def addproduct():
    return render_template('addproduct.html')
@app.route('/addprod',methods=['POST','GET'])
def addprod():
    productcode = request.form['pcode']
    productname = request.form['pname']
    productprice = request.form['price']
    stock = request.form['stock']
    print(productcode,productname,productprice,stock)
    if (productcode == "" or productname == "" or productprice == "" or stock == ""):
        return render_template('addproduct.html', msg ="Fill all the values")
    else:
       dt = {'productcode': productcode, 'productname': productname ,'productprice':productprice ,'stock':stock }
       prodDict.append(dt)
       print(len(prodDict))
       return redirect(url_for('stats'))

@app.route('/addorder')
def addorder():
    return render_template('sales.html')
@app.route('/order',methods=['POST','GET'])
def order():
     pcode = request.form['ProductCode']
     Quantity = request.form['quantity']
     Address = request.form['address']
     print(pcode,Quantity,Address)
     if (pcode == "" or Quantity == "" or Address == "" ):
         return render_template('sales.html', msg ="Fill all the values")
     else:
       dt = {'productcode': pcode, 'Quantitys': Quantity ,'place':Address }
       SalesDict.append(dt)
       print(len( SalesDict))
       return redirect(url_for('stats'))

        
@app.route('/stats',methods=['POST','GET'])
def stats():
    return render_template('index.html',v1 = len(prodDict),totaluser = len(ListDict))




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

