from flask import Flask, request, render_template, jsonify, make_response
from flaskext.mysql import MySQL
import yaml
import json
import simplejson as _json

app = Flask(__name__)

# Configure db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_DATABASE_HOST'] = db['mysql_host']
app.config['MYSQL_DATABASE_PORT'] = db['mysql_port']
app.config['MYSQL_DATABASE_USER'] = db['mysql_user']
app.config['MYSQL_DATABASE_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DATABASE_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('customerDetails.html')

@app.route('/endpoint1/<customerName>', methods=['GET'])
def endpoint1(customerName):
    if request.method == 'GET':
        cur = mysql.get_db().cursor()
        rows = 0
        rows = cur.execute("SELECT customerNumber, CONCAT(RTRIM(LTRIM(COALESCE(contactFirstName,''))),' ', RTRIM(LTRIM(COALESCE(contactLastName,'')))), CONCAT(RTRIM(LTRIM(COALESCE(addressLine1,''))), ', ', RTRIM(LTRIM(COALESCE(addressLine2,'')))), country, creditLimit FROM customers WHERE CONCAT(RTRIM(LTRIM(COALESCE(contactFirstName,''))),' ', RTRIM(LTRIM(COALESCE(contactLastName,''))))='" + customerName + "' ORDER BY creditLimit")
        if rows==0:
            rows = cur.execute("SELECT customerNumber, CONCAT(RTRIM(LTRIM(COALESCE(contactFirstName,''))),' ', RTRIM(LTRIM(COALESCE(contactLastName, '')))), CONCAT(RTRIM(LTRIM(COALESCE(addressLine1,''))), ', ', RTRIM(LTRIM(COALESCE(addressLine2,'')))), country, creditLimit FROM customers ORDER BY creditLimit")
        if rows>0:
            result = cur.fetchall()
            result=list(result)
            for i in range(rows):
                result[i] = list(result[i])
                result[i][4] = int(result[i][4])
            res = make_response(jsonify(result))
            cur.close()
            return res
        cur.close()
        return 'Fail'
    return 'Fail'

@app.route('/endpoint2/<customerNumber>', methods=['GET'])
def endpoint2(customerNumber):
    if request.method == 'GET':
        cur = mysql.get_db().cursor()
        rows = cur.execute("SELECT * FROM customers WHERE customerNumber=" + customerNumber)
        if rows>0:
            result = cur.fetchall()
            result=list(result)
            for i in range(rows):
                result[i] = list(result[i])
                result[i][12] = int(result[i][12])
            res = make_response(jsonify(result))
            cur.close()
            return res
        cur.close()
        return 'Fail'
    return 'Fail'

@app.route('/endpoint3', methods=['POST'])
def endpoint3():
    if request.method == 'POST':
        data = request.json
        customerNumber = str(data["ID"])
        customerFName = str(data["Update"]["firstName"])
        customerLName = str(data["Update"]["lastName"])
        creditLimit = str(data["CreditLimit"])
        cur = mysql.get_db().cursor()
        cur.execute("UPDATE customers SET contactLastName='"+customerLName+"', contactFirstName='"+customerFName+"' ,creditLimit="+creditLimit+" WHERE customerNumber="+customerNumber)
        mysql.get_db().commit()
        cur.close()
        res = make_response(jsonify("Sucessful Update"))
        return res
    return 'Fail'

if __name__=='__main__':
    app.run(debug=True)


