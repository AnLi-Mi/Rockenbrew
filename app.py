from flask import Flask, render_template, request

from flaskext.mysql import MySQL



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
app.config['MYSQL_DATABASE_DATABASE'] = 'rockenbrew'
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
    customerID=''
    rbCustomerID=''
    companyName=''
    companyLocalID=''
    companyLocalIDType=''
    custTypeID=''
    startDate=''
    domicile=''
    if request.method == 'POST' and 'customerID' in request.form:
        customerID=request.form.get('customerID')
        rbCustomerID=request.form.get('rbCustomerID')
        companyName=request.form.get('companyName')
        companyLocalID=request.form.get('companyLocalID')
        companyLocalIDType=request.form.get('companyLocalIDType')
        custTypeID=request.form.get('custTypeID')
        startDate=request.form.get('startDate')
        domicile=request.form.get('domicile')
        query_add_customer= f"""INSERT INTO `customer` (`customerID`,
                            `rbCustomerID`,
                            `companyName`,
                            `companyLocalID`,
                            `companyLocalIDType`,
                            `custTypeID`,
                            `startDate`,
                            `domicile`)
                    VALUES ({customerID},
                            {rbCustomerID},
                            {companyName},
                            {companyLocalID},
                            {companyLocalIDType},
                            {custTypeID},
                            {startDate},
                            {domicile});"""
        insert_query(query)
    return render_template('full_form.html', customerID=customerID, rbCustomerID=rbCustomerID, companyName=companyName, companyLocalID=companyLocalID, companyLocalIDType=companyLocalIDType, custTypeID=custTypeID, startDate=startDate, domicile=domicile)


