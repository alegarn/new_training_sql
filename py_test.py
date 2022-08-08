#Create database Test_SQL;

#https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1
import os
from dotenv import load_dotenv

load_dotenv()


host_password = os.getenv('PASSWORD')

#https://gist.github.com/bmillemathias/f4ae3d8739b4b30c6d18164c4a70b7c2
import time
import os

import mysql.connector
from mysql.connector import Error
from faker import Faker

import random

#https://pynative.com/python-mysql-database-connection/#h-create-mysql-table-from-python
import mysql.connector

fake = Faker('en_US')
Faker.seed(0)

try:
    conn = mysql.connector.connect(host='localhost',
                                         database='Test_SQL',
                                         user='root',
                                         password=host_password)

    try:
        cursor = conn.cursor()
#Populate the customers Table with test data
        n = 0

        while n < 19:
            n += 1
            usa_number = "+1" + str(fake.msisdn())
            row = [fake.name(), fake.address(), fake.email(), \
                usa_number, fake.city()]

            cursor.execute(" \
                INSERT INTO customers (customer_name, customer_address, customer_email, customer_phone, customer_city) \
                VALUES ('%s', '%s', '%s', '%s', '%s');" \
                % (row[0], row[1], row[2], row[3], row[4]))

            if n == 10:
                print("iteration %s" % n)
                time.sleep(0.5)
                conn.commit()

                print("Table seeded successfully ")

        n = 0
        #products
        while n < 11:

            row = [fake.job(), random.randrange(101)]

            cursor.execute(" \
                            INSERT INTO products (product_name, price) \
                            VALUES ('%s', '%s');" \
                            % (row[0], row[1]))
            if n == 10:
                print("iteration %s" % n)
                time.sleep(0.5)
                conn.commit()
            n = n + 1

        #SELECT customer_id, et injecter dans carts
        n = 0

        while n < 71:
            cursor.execute(" \
                SELECT C.customer_id FROM customers as C;")

            myresult = cursor.fetchall()
            c_id = []

            for x in myresult:
                c_id.append(str(x[0]))
                print(str(x[0]) + " str")

            row = [random.choice(c_id), 0]
            print(row[0])

            try:
                cursor.execute(" \
                    INSERT INTO carts (customer_id, total) \
                    VALUES ('%s', '%s');" \
                    % (row[0], row[1]))
                time.sleep(0.5)
                conn.commit()


                myresult = cursor.fetchall()

                for x in myresult:
                    print(str(x[0]) + " str")

                n = n + 1

            except cursor.Error as error:
                print("Failed to insert table in MySQL: {}".format(error))

        #remplir la table cart_products
        n = 0
        while n < 71:

            try:
                cursor.execute(" \
                SELECT C.cart_id FROM carts as C;")

                myresult = cursor.fetchall()
                cart_id = []
                for x in myresult:
                    cart_id.append(str(x[0]))

                row_cart_id = [random.choice(cart_id)]

                cursor.execute(" \
                SELECT P.product_id FROM products as P;")

                myresult = cursor.fetchall()
                product_id = []
                for x in myresult:
                    product_id.append(str(x[0]))

                row_product_id = [random.choice(product_id)]

                cursor.execute(" \
                            INSERT INTO cart_products (cart_id, product_id, quantity) \
                            VALUES ('%s', '%s', '%s');" \
                            % (row_cart_id[0], row_product_id[0], random.randrange(1, 3)))
                time.sleep(0.5)
                conn.commit()

            except cursor.Error as error:
                print("Failed to insert table in MySQL: {}".format(error))
            n = n + 1


        #carts total update
        try: # Arranging Rows within Partitions
            # https://stackoverflow.com/questions/11588710/mysql-update-query-with-sub-query
            cursor.execute(" \
                        UPDATE carts as C \
        	               INNER JOIN ( \
        		                 SELECT 	C.cart_id, \
        				                    C.product_id, \
        				                    C.quantity, \
        				                    P.price, \
        				                    (quantity * P.price) AS total_prod, \
        				                    (sum(quantity * P.price) \
        					                               OVER ( \
        						                                 PARTITION BY cart_id \
        						                                 ORDER BY cart_id)) AS sum_cart \
        		                 FROM cart_products as C \
        		                 INNER JOIN products as P \
        		                 ON C.product_id = P.product_id \
        		                 ORDER BY C.cart_id \
        		           ) as cart_sum ON C.cart_id = cart_sum.cart_id \
                         SET total = total + cart_sum.sum_cart;")
            myresult = cursor.fetchall()
            time.sleep(0.5)
            conn.commit()
        except Exception as e:
            raise



        #taking ord.rs c.nt..n.ng only complete carts, contain.ng pr.d.cts
        cursor.execute(" \
            SELECT DISTINCT C.cart_id \
            FROM cart_products as C \
            ")

        myresult = cursor.fetchall()
        c_id = []
        for x in myresult:
            c_id.append(str(x[0]))

        try:
            cursor.execute(" \
                    INSERT INTO orders (cart_id) \
                    SELECT DISTINCT cart_id  \
                    FROM carts  \
                    WHERE carts.total > 0 AND cart_id < 70 \
                    GROUP BY cart_id \
                    ORDER BY RAND() \
                    ;")

            time.sleep(0.5)
            conn.commit()

        except cursor.Error as e:
            print("Failed to insert table in MySQL: {}".format(e))





        n = 0
        # SELECT cart_id, et injecter dans orders (total des )
        #while n < 11:

            #try:
            #    cursor.execute(" \
            #    SELECT C.cart_id FROM carts as C;")

            #    myresult = cursor.fetchall()
            #    cart_id = []
            #    for x in myresult:
            #        cart_id.append(str(x[0]))
#
            #    row = [random.choice(cart_id), 0]

                #no order_number
            #    cursor.execute(" \
            #                INSERT INTO orders (cart_id, order_number) \
            #                VALUES ('%s', '%s');" \
            #                % (row[0], row[1]))
            #    time.sleep(0.5)
            #    conn.commit()
            #    print(row[0])

            #except cursor.Error as error:
            #    print("Failed to insert table in MySQL: {}".format(error))

    except cursor.Error as error:
        print("Failed to create table in MySQL: {}".format(error))

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
