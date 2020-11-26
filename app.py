from flask import Flask, render_template, request

from flaskext.mysql import MySQL
from datetime import date

app=Flask(__name__)

mysql=MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '8G13rm3k'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_DATABASE'] = 'rb_test'
mysql.init_app(app)


#checking connection
def connect_msql():
    conn = mysql.connect()
    if (conn):
    # Carry out normal procedure
        print ("Connection successful")
    else:
    # Terminate
        print ("Connection unsuccessful")

def insert_query(query):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

def next_id_number(table, id_number):
    conn = mysql.connect()
    cursor = conn.cursor()
    query1 = 'USE rb_test;'
    query2 = f"""SELECT {id_number} FROM rb_test.{table} WHERE {id_number} = (SELECT MAX({id_number}) FROM {table});"""
    cursor.execute(query1)
    cursor.execute(query2)
    result=cursor.fetchone()
    result = result[0]
    return int(result)+1


def display_table(table):
    conn = mysql.connect()
    cursor = conn.cursor()
    query1 = 'USE rb_test;'
    query2 = f"""SELECT * FROM rb_test.{table};"""
    cursor.execute(query1)
    cursor.execute(query2)
    results=cursor.fetchall()
    return results

def display_records(query):
    conn = mysql.connect()
    cursor = conn.cursor()
    query1 = 'USE rb_test;'
    query2 = query
    cursor.execute(query1)
    cursor.execute(query2)
    results=cursor.fetchall()
    return results

def testuje(rb_id):
    query=                  f"""SELECT
                            customer.customerID,
                            customer.rbCustomerID,
                            customer.companyName,
                            customer.companyLocalID,
                            customer.companyLocalIDType,
                            customer.custTypeID,
                            customer.startDate,
                            customer.domicile,
                            paymentschedule.paymentScheduleID,
                            paymentschedule.value as payment_value,
                            paymentschedule.frequency as payment_frequency,
                            paymentschedule.firstPaymentDate,
                            paymentschedule.startDate,
                            paymentschedule.lastPaymentDate,
                            paymentschedule.active,
                            licence.licenceID,
                            licence.type,
                            licence.issueDate,
                            licence.validFrom,
                            licence.validTo,
                            licence.activationCode,
                            user.userID,
                            user.startDate,
                            user.username,
                            user.city,
                            user.domicile,
                            contact.contactID,
                            contact.type,
                            contact.detail,
                            adminuser.adminUserID,
                            adminuser.password,
                            adminuser.paymentContact,
                            adminuser.level,
                            keycode.keyCodeID,
                            keycode.keyCodeVersion,
                            keycode.keyCode,
                            keycode.active,
                            keycode.date
                            FROM customer
                            LEFT JOIN paymentschedule on customer.customerID=paymentschedule.customerID
                            LEFT JOIN licence on licence.customerID=paymentschedule.customerID
                            LEFT JOIN user on user.customerID=licence.customerID
                            LEFT JOIN contact on contact.customerID=customer.customerID
                            LEFT JOIN adminuser on adminuser.userID=user.userID
                            LEFT JOIN keycode on keycode.licenceID=licence.licenceID
                            WHERE customer.rbCustomerID = '{rb_id}';"""
    conn = mysql.connect()
    cursor = conn.cursor()
    query1 = 'USE rb_test;'
    query2 = query
    cursor.execute(query1)
    cursor.execute(query2)
    results=cursor.fetchall()
    return results

def one_table(results):
    base_record = list(results[0])
    list_of_multiple_values=[]
    for result in results:
        for column_value in result:
            if column_value not in base_record:
                list_of_multiple_values.append([result.index(column_value), column_value])

    return list_of_multiple_values

def one_table2(results):
    same_cust_ID = []
    
    base_record = list(results[0])
    list_of_multiple_values=[] 
    for result in results:
        for column_value in result:
            if column_value != base_record[result.index(column_value)]:
                list_of_multiple_values.append([result.index(column_value), column_value])

    return list_of_multiple_values

def one_table3(results):
    list_of_records=[]
    for result in results:
        list_of_values =[]
        for column_value in result:
          list_of_value_options =[]
          list_of_value_options.append(column_value)
          list_of_values.append(list_of_value_options)
        list_of_records.append(list_of_values)

    return list_of_records


def list_of_column_values(results):
    columns =[]
    i=0
    while i<38:
        my_list=[]
        for record in results:
            my_list.append(record[i])
        i+=1
        columns.append(my_list)
            
    return columns
    
@app.route('/', methods=  ['GET', 'POST'])
def home_page():
    search_input = ""
    if request.method =='POST' and 'search_input' in request.form:
        search_input = request.form.get('search_input')
    query_all_tables = """SELECT
                            customer.customerID,
                            customer.rbCustomerID,
                            customer.companyName,
                            customer.companyLocalID,
                            customer.companyLocalIDType,
                            customer.custTypeID,
                            customer.startDate,
                            customer.domicile,
                            paymentschedule.paymentScheduleID,
                            paymentschedule.value as payment_value,
                            paymentschedule.frequency as payment_frequency,
                            paymentschedule.firstPaymentDate,
                            paymentschedule.startDate,
                            paymentschedule.lastPaymentDate,
                            paymentschedule.active,
                            licence.licenceID,
                            licence.type,
                            licence.issueDate,
                            licence.validFrom,
                            licence.validTo,
                            licence.activationCode,
                            user.userID,
                            user.startDate,
                            user.username,
                            user.city,
                            user.domicile,
                            contact.contactID,
                            contact.type,
                            contact.detail,
                            adminuser.adminUserID,
                            adminuser.password,
                            adminuser.paymentContact,
                            adminuser.level,
                            keycode.keyCodeID,
                            keycode.keyCodeVersion,
                            keycode.keyCode,
                            keycode.active,
                            keycode.date
                            FROM customer
                            LEFT JOIN paymentschedule on customer.customerID=paymentschedule.customerID
                            LEFT JOIN licence on licence.customerID=paymentschedule.customerID
                            LEFT JOIN user on user.customerID=licence.customerID
                            LEFT JOIN contact on contact.customerID=customer.customerID
                            LEFT JOIN adminuser on adminuser.userID=user.userID
                            LEFT JOIN keycode on keycode.licenceID=licence.licenceID;"""
    query_specific_record = f"""SELECT
                            customer.customerID,
                            customer.rbCustomerID,
                            customer.companyName,
                            customer.companyLocalID,
                            customer.companyLocalIDType,
                            customer.custTypeID,
                            customer.startDate,
                            customer.domicile,
                            paymentschedule.paymentScheduleID,
                            paymentschedule.value as payment_value,
                            paymentschedule.frequency as payment_frequency,
                            paymentschedule.firstPaymentDate,
                            paymentschedule.startDate,
                            paymentschedule.lastPaymentDate,
                            paymentschedule.active,
                            licence.licenceID,
                            licence.type,
                            licence.issueDate,
                            licence.validFrom,
                            licence.validTo,
                            licence.activationCode,
                            user.userID,
                            user.startDate,
                            user.username,
                            user.city,
                            user.domicile,
                            contact.contactID,
                            contact.type,
                            contact.detail,
                            adminuser.adminUserID,
                            adminuser.password,
                            adminuser.paymentContact,
                            adminuser.level,
                            keycode.keyCodeID,
                            keycode.keyCodeVersion,
                            keycode.keyCode,
                            keycode.active,
                            keycode.date
                            FROM customer
                            LEFT JOIN paymentschedule on customer.customerID=paymentschedule.customerID
                            LEFT JOIN licence on licence.customerID=paymentschedule.customerID
                            LEFT JOIN user on user.customerID=licence.customerID
                            LEFT JOIN contact on contact.customerID=customer.customerID
                            LEFT JOIN adminuser on adminuser.userID=user.userID
                            LEFT JOIN keycode on keycode.licenceID=licence.licenceID
                            WHERE customer.companyName LIKE '%{search_input}%' or customer.rbCustomerID = '{search_input}';"""
    all_records_and_tables = display_records(query_all_tables)
    spcific_record_all_tables =  display_records(query_specific_record)
    return render_template('home_page.html', all_records_and_tables=all_records_and_tables, spcific_record_all_tables=spcific_record_all_tables)

@app.route('/full_form', methods=['GET', 'POST'])
def full_form():
    rbCustomerID=''
    companyName=''
    companyLocalID=''
    companyLocalIDType=''
    custTypeID=''
    startDate=''
    domicile=''

    value=''
    frequency=''
    firstPaymentDate=''
    lastPaymentDate=''
    active=''
    customerID=''

    type=''
    issueDate=''
    validFrom=''
    validTo=''
    activationCode=''
    paymentScheduleID=''

    userStartDate=''
    username=''
    city=''
    userDomicile=''
    licenceID=''

    contactType=''
    contactDetail=''
    userID=''

    password=''
    paymentContact=''
    level=''

    keyCodeVersion=''
    keyCode=''
    codeActive=''
    codeActivationDate=''

    if request.method == 'POST' and 'rbCustomerID' in request.form:

        rbCustomerID=request.form.get('rbCustomerID')
        companyName=request.form.get('companyName')
        companyLocalID=request.form.get('companyLocalID')
        companyLocalIDType=request.form.get('companyLocalIDType')
        custTypeID=request.form.get('custTypeID')
        startDate=request.form.get('startDate')
        if startDate==None or startDate=='':
            startDate=date.today()
        domicile=request.form.get('domicile')

        value=request.form.get('value')
        frequency=request.form.get('frequency')
        firstPaymentDate=request.form.get('firstPaymentDate')
        lastPaymentDate=request.form.get('lastPaymentDate')
        active=request.form.get('active')

        type=request.form.get('type')
        issueDate=request.form.get('issueDate')
        validFrom=request.form.get('validFrom')
        validTo=request.form.get('validTo')
        activationCode=request.form.get('activationCode')

        userStartDate=request.form.get('userStartDate')
        username=request.form.get('username')
        city=request.form.get('city')
        userDomicile=request.form.get('userDomicile')

        contactType=request.form.get('contactType')
        contactDetail=request.form.get('contactDetail')

        password=request.form.get('password')
        paymentContact=request.form.get('paymentContact')
        level=request.form.get('level')

        keyCodeVersion=request.form.get('keyCodeVersion')
        keyCode=request.form.get('keyCode')
        codeActive=request.form.get('codeActive')
        codeActivationDate=request.form.get('codeActivationDate')

        customerID=next_id_number("customer", "customerID")
        paymentScheduleID=next_id_number("paymentschedule", "paymentScheduleID")
        licenceID=next_id_number("licence", "licenceID")
        userID=next_id_number("user", "userID")



        query_add_customer= f"""INSERT INTO rb_test.customer (
                            rbCustomerID,
                            companyName,
                            companyLocalID,
                            companyLocalIDType,
                            custTypeID,
                            startDate,
                            domicile)
                    VALUES ('{rbCustomerID}',
                            '{companyName}',
                            '{companyLocalID}',
                            '{companyLocalIDType}',
                            '{custTypeID}',
                            '{startDate}',
                            '{domicile}');"""
        query_add_payment= f"""INSERT INTO rb_test.paymentschedule(
                            value,
                            frequency,
                            firstPaymentDate,
                            startDate,
                            lastPaymentDate,
                            active,
                            customerID)
                    VALUES ('{value}',
                            '{frequency}',
                            '{firstPaymentDate}',
                            '{startDate}',
                            '{lastPaymentDate}',
                            '{active}',
                            '{customerID}');"""
        query_add_licence= f"""INSERT INTO rb_test.licence(
                            type,
                            issueDate,
                            validFrom,
                            validTo,
                            activationCode,
                            paymentScheduleID,
                            customerID)
                    VALUES ('{type}',
                            '{issueDate}',
                            '{validFrom}',
                            '{validTo}',
                            '{activationCode}',
                            '{paymentScheduleID}',
                            '{customerID}');"""
        query_add_user= f"""INSERT INTO rb_test.user(
                            startDate,
                            username,
                            city,
                            domicile,
                            customerID,
                            licenceID)
                    VALUES ('{userStartDate}',
                            '{username}',
                            '{city}',
                            '{userDomicile}',
                            '{customerID}',
                            '{licenceID}');"""
        query_add_contact= f"""INSERT INTO rb_test.contact(
                            type,
                            detail,
                            customerID,
                            userID)
                    VALUES ('{contactType}',
                            '{contactDetail}',
                            '{customerID}',
                            '{userID}');"""
        query_add_adminuser= f"""INSERT INTO rb_test.adminuser(
                            password,
                            paymentContact,
                            level,
                            userID)
                    VALUES ('{password}',
                            '{paymentContact}',
                            '{level}',
                            '{userID}');"""
        query_add_keycode= f"""INSERT INTO rb_test.keycode(
                            keyCodeVersion,
                            keyCode,
                            active,
                            date,
                            licenceID)
                    VALUES ('{keyCodeVersion}',
                            '{keyCode}',
                            '{codeActive}',
                            '{codeActivationDate}',
                            '{licenceID}');"""
        insert_query(query_add_customer)
        insert_query(query_add_payment)
        insert_query(query_add_licence)
        insert_query(query_add_user)
        insert_query(query_add_contact)
        insert_query(query_add_adminuser)
        insert_query(query_add_keycode)
    return render_template('full_form.html', rbCustomerID=rbCustomerID, companyName=companyName, companyLocalID=companyLocalID, companyLocalIDType=companyLocalIDType, custTypeID=custTypeID, startDate=startDate, domicile=domicile)

@app.route('/customer_form', methods = ['GET', 'POST'])
def customer_form():
    rbCustomerID=''
    companyName=''
    companyLocalID=''
    companyLocalIDType=''
    custTypeID=''
    startDate=''
    domicile=''
    if request.method == 'POST' and 'rbCustomerID' in request.form:
        rbCustomerID=request.form.get('rbCustomerID')
        companyName=request.form.get('companyName')
        companyLocalID=request.form.get('companyLocalID')
        companyLocalIDType=request.form.get('companyLocalIDType')
        custTypeID=request.form.get('custTypeID')
        startDate=request.form.get('startDate')
        if startDate==None or startDate=='':
            startDate=date.today()
        domicile=request.form.get('domicile')

        query_add_customer= f"""INSERT INTO rb_test.customer (
                        rbCustomerID,
                        companyName,
                        companyLocalID,
                        companyLocalIDType,
                        custTypeID,
                        startDate,
                        domicile)
                VALUES ('{rbCustomerID}',
                        '{companyName}',
                        '{companyLocalID}',
                        '{companyLocalIDType}',
                        '{custTypeID}',
                        '{startDate}',
                        '{domicile}');"""

        insert_query(query_add_customer)
    return render_template('customer_form.html')

@app.route('/paymentschedule_form', methods=['GET','POST'])
def paymentschedule_form():
    value=''
    frequency=''
    firstPaymentDate=''
    lastPaymentDate=''
    active=''
    customerID=''
    if request.method=='POST' and 'value' in request.form:
        value=request.form.get('value')
        frequency=request.form.get('frequency')
        firstPaymentDate=request.form.get('firstPaymentDate')
        lastPaymentDate=request.form.get('lastPaymentDate')
        active=request.form.get('active')
        customerID=request.form.get('customerID')
        query_add_payment= f"""INSERT INTO rb_test.paymentschedule(
                                value,
                                frequency,
                                firstPaymentDate,
                                startDate,
                                lastPaymentDate,
                                active,
                                customerID)
                        VALUES ('{value}',
                                '{frequency}',
                                '{firstPaymentDate}',
                                '{startDate}',
                                '{lastPaymentDate}',
                                '{active}',
                                '{customerID}');"""
        insert_query(query_add_payment)
    return render_template('paymentschedule_form.html')

@app.route('/licence_form', methods=['GET','POST'])
def licence_form():
    type=''
    issueDate=''
    validFrom=''
    validTo=''
    activationCode=''
    paymentScheduleID=''
    customerID=''
    if request.method=='POST' and 'type' in request.form:
        type=request.form.get('type')
        issueDate=request.form.get('issueDate')
        validFrom=request.form.get('validFrom')
        validTo=request.form.get('validTo')
        activationCode=request.form.get('activationCode')
        paymentScheduleID=request.form.get('paymentScheduleID')
        customerID=request.form.get('customerID')
        query_add_licence= f"""INSERT INTO rb_test.licence(
                            type,
                            issueDate,
                            validFrom,
                            validTo,
                            activationCode,
                            paymentScheduleID,
                            customerID)
                    VALUES ('{type}',
                            '{issueDate}',
                            '{validFrom}',
                            '{validTo}',
                            '{activationCode}',
                            '{paymentScheduleID}',
                            '{customerID}');"""
        insert_query(query_add_licence)
    return render_template('licence_form.html')

@app.route('/user_form', methods=['GET','POST'])
def user_form():
    userStartDate=''
    username=''
    city=''
    userDomicile=''
    customerID=''
    licenceID=''
    if request.method=='POST' and 'userStartDate' in request.form:
        userStartDate=request.form.get('userStartDate')
        username=request.form.get('username')
        city=request.form.get('city')
        userDomicile=request.form.get('userDomicile')
        customerID=request.form.get('customerID')
        licenceID=request.form.get('licenceID')
        query_add_user= f"""INSERT INTO rb_test.user(
                            startDate,
                            username,
                            city,
                            domicile,
                            customerID,
                            licenceID)
                    VALUES ('{userStartDate}',
                            '{username}',
                            '{city}',
                            '{userDomicile}',
                            '{customerID}',
                            '{licenceID}');"""
        insert_query(query_add_user)
    return render_template('user_form.html')

@app.route("/contact_form", methods = ['GET', 'POST'])
def contact_form():
    contactType=''
    contactDetail=''
    customerID=''
    userID=''
    if request.method=="POST" and "type" in request.form:
        contactType=request.form.get('contactType')
        contactDetail=request.form.get('contactDetail')
        customerID=request.form.get('customerID')
        userID=request.form.get('userID')

        query_add_contact= f"""INSERT INTO rb_test.contact(
                            type,
                            detail,
                            customerID,
                            userID)
                    VALUES ('{contactType}',
                            '{contactDetail}',
                            '{customerID}',
                            '{userID}');"""
        insert_query(query_add_contact)
    return render_template('contact_form.html')

@app.route("/adminuser_form", methods = ['GET', 'POST'])
def adminuser_form():
    password=''
    paymentContact=''
    level=''
    userID=''
    if request.method=="POST" and "type" in request.form:
        password=request.form.get('password')
        paymentContact=request.form.get('paymentContact')
        level=request.form.get('level')
        userID=request.form.get('userID')
        query_add_adminuser= f"""INSERT INTO rb_test.adminuser(
                            password,
                            paymentContact,
                            level,
                            userID)
                    VALUES ('{password}',
                            '{paymentContact}',
                            '{level}',
                            '{userID}');"""
        insert_query(query_add_adminuse)
    return render_template('adminuser_form.html')

@app.route("/keycode_form", methods = ['GET', 'POST'])
def keycode_form():
    keyCodeVersion=''
    keyCode=''
    codeActive=''
    codeActivationDate=''
    licenceID=''
    if request.method=="POST" and "type" in request.form:
        keyCodeVersion=request.form.get('keyCodeVersion')
        keyCode=request.form.get('keyCode')
        codeActive=request.form.get('codeActive')
        codeActivationDate=request.form.get('codeActivationDate')
        licenceID=request.form.get('licenceID')
        query_add_keycode= f"""INSERT INTO rb_test.keycode(
                            keyCodeVersion,
                            keyCode,
                            active,
                            date,
                            licenceID)
                    VALUES ('{keyCodeVersion}',
                            '{keyCode}',
                            '{codeActive}',
                            '{codeActivationDate}',
                            '{licenceID}');"""
        insert_query(query_add_keycode)
    return render_template('keycode_form.html')

@app.route('/all_customers', methods = ['GET', 'POST'])
def all_customers():
    results=display_table("customer")
    return render_template('all_customers.html', results=results)

@app.route('/all_paymentschedules', methods = ['GET', 'POST'])
def all_paymentschedules():
    results=display_table("paymentschedule")
    return render_template('all_paymentschedules.html', results=results)

@app.route('/all_licences', methods = ['GET', 'POST'])
def all_licences():
    results=display_table("licence")
    return render_template('all_licences.html', results=results)

@app.route('/all_users', methods = ['GET', 'POST'])
def all_users():
    results=display_table("user")
    return render_template('all_users.html', results=results)

@app.route('/all_contacts', methods = ['GET', 'POST'])
def all_contacts():
    results=display_table("contact")
    return render_template('all_contacts.html', results=results)

@app.route('/all_adminusers', methods = ['GET', 'POST'])
def all_adminusers():
    results=display_table("adminuser")
    return render_template('all_adminusers.html', results=results)

@app.route('/all_keycodes', methods = ['GET', 'POST'])
def all_keycodes():
    results=display_table("keycode")
    return render_template('all_keycodes.html', results=results)

@app.route('/edit_record/<customerID>', methods=['GET', 'POST'])
def edit_record(customerID):
    display_record = f"""SELECT
                            customer.customerID,
                            customer.rbCustomerID,
                            customer.companyName,
                            customer.companyLocalID,
                            customer.companyLocalIDType,
                            customer.custTypeID,
                            customer.startDate,
                            customer.domicile,
                            paymentschedule.paymentScheduleID,
                            paymentschedule.value as payment_value,
                            paymentschedule.frequency as payment_frequency,
                            paymentschedule.firstPaymentDate,
                            paymentschedule.startDate,
                            paymentschedule.lastPaymentDate,
                            paymentschedule.active,
                            licence.licenceID,
                            licence.type,
                            licence.issueDate,
                            licence.validFrom,
                            licence.validTo,
                            licence.activationCode,
                            user.userID,
                            user.startDate,
                            user.username,
                            user.city,
                            user.domicile,
                            contact.contactID,
                            contact.type,
                            contact.detail,
                            adminuser.adminUserID,
                            adminuser.password,
                            adminuser.paymentContact,
                            adminuser.level,
                            keycode.keyCodeID,
                            keycode.keyCodeVersion,
                            keycode.keyCode,
                            keycode.active,
                            keycode.date
                            FROM customer
                            LEFT JOIN paymentschedule on customer.customerID=paymentschedule.customerID
                            LEFT JOIN licence on licence.customerID=paymentschedule.customerID
                            LEFT JOIN user on user.customerID=licence.customerID
                            LEFT JOIN contact on contact.customerID=customer.customerID
                            LEFT JOIN adminuser on adminuser.userID=user.userID
                            LEFT JOIN keycode on keycode.licenceID=licence.licenceID
                            WHERE customer.customerID = {customerID};"""

    spcific_record_all_tables =  display_records(display_record)

    return render_template('edit_record.html', spcific_record_all_tables=spcific_record_all_tables)
