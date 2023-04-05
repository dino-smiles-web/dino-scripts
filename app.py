import pymysql
pymysql.install_as_MySQLdb() 
from flask import Flask, render_template, request
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
# start the connection



app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/DinoSmilesMainPage')
def DinoSmilesMainPage():
    return render_template('DinoSmilesMainPage.html')

@app.route('/BranchInfoPage')
def BranchInfoPage():
    return render_template('BranchInfoPage.html')

@app.route('/DinoSmilesTeam')
def DinoSmilesTeam():
    return render_template('DinoSmilesTeam.html')

@app.route('/TestimonialsPage')
def TestimonialsPage():
    return render_template('TestimonialsPage.html')

@app.route('/UserPortalv1')
def UserPortalv1():
    return render_template('UserPortalv1.html')


@app.route('/submit', methods=['POST'])
def submit(): 
   #Connection to SQL server on Azure
    cnxn = pymysql.connect(
        user="headdino", 
        password="P@ssw0rd", 
        host="dinosmiles-db2.mysql.database.azure.com", 
        port=3306, 
        database="dino_smiles", 
        ssl_ca="DigiCertGlobalRootCA.crt (2).pem", 
        ssl_disabled=True
    )
    #Declare variables 
    name = request.form['name']
    lastname = request.form['lastname']
    date = request.form['date']
    time = request.form['time']
    email = request.form['email']
    phone = request.form['phone']
    location = request.form['location']

    #Post variables on SQL table
    cursor = cnxn.cursor()
    sql = "INSERT INTO appointments (name, lastname, date, time, email, phone, location) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (name, lastname, date, time, email, phone, location)
    cursor.execute(sql,val)
    
    #Commit and close
    cnxn.commit()
    cursor.close()
    cnxn.close()

    return render_template('Appointment.html')
    #return f"Name: {name}, Last Name: {lastname}, Date: {date}, Time: {time}, Email: {email}, Phone: {phone}"
# return render_template('Confirmation.html',Name = name, Last Name =lastname, Date= date, Time= time, Email= email, Phone= phone)

if __name__ == '__main__':
    app.run(debug=True)

