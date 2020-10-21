

query_add_customer=
f"""INSERT INTO `customer` (`customerID`,
                            `rbCustomerID`,
                            `companyName`,
                            `companyLocalID`,
                            `companyLocalIDType`,
                            `custTypeID`,
                            `startDate`,
                            `domicile`)
                    VALUES ({defauult_id},
                            {rb_id},
                            {compay_name},
                            {company_local_id},
                            {local_id_type},
                            {cust_type_id},
                            {start_date},
                            {domicile});"""

query_add_payment_schedule =
f"""INSERT INTO `paymentschedule` (`paymentScheduleID`,
                                   `value`,
                                   `frequency`,
                                   `firstPaymentDate`,
                                   `startDate`,
                                   `lastPaymentDate`,
                                   `active`,
                                   `customerID`)
                           VALUES ({paymentScheduleID},
                                   {value},
                                   {frequency},
                                   {firstPaymentDate},
                                   {startDate},
                                   {lastPaymentDate},
                                   {active},
                                   {customerID});"""

query_delete=

query_amend=

query_show= 
