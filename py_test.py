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



        while n < 11:
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

        while n < 11:
            #products
            row = [fake.job(), faker.random_int(1, 100)]

            cursor.execute(" \
                            INSERT INTO products (product_name, price) \
                            VALUES ('%s', '%s');" \
                            % (row[0], row[1]))
                            if n == 10:
                                print("iteration %s" % n)
                                time.sleep(0.5)
                                conn.commit()

        #carts
        row = [str(random_int(1,10))]

        cursor.execute(" \
            INSERT INTO carts (customer_id) \
            VALUES ('%s');" \
            % (row[0]))

        #orders
        row = [str(random_int(1,10))]

        cursor.execute(" \
                                INSERT INTO products (cart_id) \
                                VALUES ('%s');" \
                                % (row[0]))

          `order_id` INT NOT NULL AUTO_INCREMENT,
          `cart_id` INT,
          `order_number` INT NOT NULL,
          `order_date` TIMESTAMP DEFAULT NOW(),


          CREATE TABLE `cart_products` (
            `cart_product_id` INT NOT NULL AUTO_INCREMENT,
            `cart_id` INT,
            `product_id` INT,
            `created_at` TIMESTAMP DEFAULT NOW(),




        #c.rt
        row = [fake.name(), fake.address(), fake.email(), \
            usa_number, fake.city()]

        cursor.execute(" \
            INSERT INTO customers (customer_name, customer_address, customer_email, customer_phone, customer_city) \
            VALUES ('%s', '%s', '%s', '%s', '%s');" \
            % (row[0], row[1], row[2], row[3], row[4]))

        #carts - upd.te
        row = [ total]

        cursor.execute(" \
                    INSERT INTO carts (total) \
                    VALUES ('%s');" \
                    % (row[0]))


    except cursor.Error as error:
        print("Failed to create table in MySQL: {}".format(error))

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
