from flask import Flask, render_template, request

from flaskext.mysql import MySQL
from datetime import date



#query_add_customer= f"""INSERT INTO `customer` (`customerID`,
 #                           `rbCustomerID`,
  #                          `companyName`,
   #                         `companyLocalID`,
    #                        `companyLocalIDType`,
     #                       `custTypeID`,
      #                      `startDate`,
       #                     `domicile`)
        #            VALUES ({default_id},
         #                   {rb_id},
          #                  {compay_name},
           #                 {company_local_id},
            #                {local_id_type},
             #               {cust_type_id},
              #              {start_date},
               #             {domicile});"""

#query_add_payment_schedule = f"""INSERT INTO `paymentschedule` (`paymentScheduleID`,
 #                                  `value`,
  ##                                 `frequency`,
     #                              `firstPaymentDate`,
      #                             `startDate`,
       #                            `lastPaymentDate`,
        #                           `active`,
         #                          `customerID`)
          #                 VALUES ({paymentScheduleID},
           #                        {value},
            #                       {frequency},
             #                      {firstPaymentDate},
              #                     {startDate},
               #                    {lastPaymentDate},
                #                   {active},
                 #                  {customerID});"""

#query_add_payment_schedule =

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

def display_table(query):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(query)
    result=cursor.fetchall()
    result = result[0]
    result = result[0]
    return result

@app.route('/', methods=['GET', 'POST'])
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
    if request.method == 'POST' and 'rbCustomerID' in request.form:
        rbCustomerID=request.form.get('rbCustomerID')
        companyName=request.form.get('companyName')
        companyLocalID=request.form.get('companyLocalID')
        companyLocalIDType=request.form.get('companyLocalIDType')
        custTypeID=request.form.get('custTypeID')
        if custTypeID==None or custTypeID=='':
            custTypeID=0
        startDate=request.form.get('startDate')
        if startDate==None or startDate=='':
            startDate=date.today()
        domicile=request.form.get('domicile')
        value=request.form.get('value')
        frequency=request.form.get('frequency')
        firstPaymentDate=request.form.get('firstPaymentDate')
        lastPaymentDate=request.form.get('lastPaymentDate')
        active=request.form.get('active')
        customerID=request.form.get('customerID')
        type=request.form.get('type')
        issueDate=request.form.get('issueDate')
        validFrom=request.form.get('validFrom')
        validTo=request.form.get('validTo')
        activationCode=request.form.get('activationCode')
        paymentScheduleID=request.form.get('paymentScheduleID')
        userStartDate=request.form.get('userStartDate')
        username=request.form.get('username')
        city=request.form.get('city')
        userDomicile=request.form.get('userDomicile')
        licenceID=request.form.get('licenceID')

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
        insert_query(query_add_customer)
        insert_query(query_add_payment)
        insert_query(query_add_licence)
        insert_query(query_add_user)
    return render_template('full_form.html', rbCustomerID=rbCustomerID, companyName=companyName, companyLocalID=companyLocalID, companyLocalIDType=companyLocalIDType, custTypeID=custTypeID, startDate=startDate, domicile=domicile)
