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

        while n < 1:
            n += 1
            usa_number = "+1" + str(fake.msisdn())
            row = [fake.name(), fake.address(), fake.email(), \
                usa_number, fake.city()]

            # SELECT customer_id, et injecter dans carts

            cursor.execute(" \
                SELECT C.customer_id FROM customers as C;")

            myresult = cursor.fetchall()
            c_id = []

            for x in myresult:
                c_id.append(str(x[0]))
                print(str(x[0]) + " str")
            print("Table seeded successfully ")

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

            except cursor.Error as error:
                print("Failed to insert table in MySQL: {}".format(error))


            #products
            try:
                row = [fake.job(), faker.random_int(1, 100)]
                #https://www.w3schools.com/python/python_mysql_insert.asp
                cursor.execute(" \
                                INSERT INTO products (product_name, price) \
                                VALUES ('%s', '%s');" \
                                % (row[0], row[1]))
                time.sleep(0.5)
                conn.commit()

            except cursor.Error as error:
                print("Failed to insert table in MySQL: {}".format(error))

            #remplir la table cart_products
            try:
                cursor.execute(" \
                SELECT C.cart_id FROM carts as C;")

                myresult = cursor.fetchall()
                cart_id = []
                for x in myresult:
                    cart_id.append(str(x[0]))

                row_cart_id = [random.choice(cart_id), 0]

                cursor.execute(" \
                SELECT C.cart_id FROM carts as C;")

                myresult = cursor.fetchall()
                product_id = []
                for x in myresult:
                    product_id.append(str(x[0]))

                row_product_id = [random.choice(product_id), 0]


                cursor.execute(" \
                            INSERT INTO cart_products (cart_id, product_id) \
                            VALUES ('%s', '%s');" \
                            % (row[0], row[1]))
                time.sleep(0.5)
                conn.commit()
                print(row[0])

            except cursor.Error as error:
                print("Failed to insert table in MySQL: {}".format(error))


            #prix des produits
            #ajouter la quantité (carts)
            #mettre des produits -> puis rempl.r cart_products -> en déduire le cart (mettre ça en SQL)


            # SELECT cart_id, et injecter dans orders
            try:
                cursor.execute(" \
                SELECT C.cart_id FROM carts as C;")

                myresult = cursor.fetchall()
                cart_id = []
                for x in myresult:
                    cart_id.append(str(x[0]))

                row = [random.choice(cart_id), 0]


                cursor.execute(" \
                            INSERT INTO orders (cart_id, order_number) \
                            VALUES ('%s', '%s');" \
                            % (row[0], row[1]))
                time.sleep(0.5)
                conn.commit()
                print(row[0])

            except cursor.Error as error:
                print("Failed to insert table in MySQL: {}".format(error))



    except cursor.Error as error:
        print("Failed to create table in MySQL: {}".format(error))

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
