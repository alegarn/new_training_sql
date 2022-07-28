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

            # V les cl..nts
            # V Les c.rts
            # V les pr.d..ts
            # cr..r c.rt_pr.d.cts
            # m.d.f..r l.s c.rts (pr.d..ts dans c.rt_pr.d.cts aj..t.r le t.t.l)
            #prix des produits ajouter la quantité (carts t.t.l) p.r SQL
            # des ord.rs

            cursor.execute(" \
            SELECT C.cart_id \
            FROM carts as C \
            WHERE cart_id < 5;")
            myresult = cursor.fetchall()
            c_id = []
            for x in myresult:
                c_id.append(str(x[0]))

            INSERT INTO orders (cart_id)
            VALUES ('%s') , ;
            # comm.nde ins.rt each



    except cursor.Error as error:
        print("Failed to create table in MySQL: {}".format(error))

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
