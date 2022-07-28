#Create database Test_SQL;

#https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1
import os
from dotenv import load_dotenv

load_dotenv()

host_username = os.getenv('USER')
host_password = os.getenv('PASSWORD')


#https://gist.github.com/bmillemathias/f4ae3d8739b4b30c6d18164c4a70b7c2
import time
import os

import mysql.connector
from mysql.connector import Error
from faker import Faker

#https://pynative.com/python-mysql-database-connection/#h-create-mysql-table-from-python
import mysql.connector

fake = Faker()


try:
    conn = mysql.connector.connect(host='localhost',
                                         database='Test_SQL',
                                         user=host_username,
                                         password=host_password)

    mysql_drop_table_query = """DROP TABLE cart_products;
                                DROP TABLE products;
                                DROP TABLE orders;
                                DROP TABLE carts;
                                DROP TABLE customers;"""




    mySql_Create_custo_Query = """CREATE TABLE customers (
                                customer_id INT NOT NULL AUTO_INCREMENT,
                                customer_name VARCHAR(80) NOT NULL,
                                customer_address VARCHAR(255),
                                customer_email VARCHAR (50),
                                customer_phone VARCHAR(15),
                                customer_city VARCHAR(30),
                                PRIMARY KEY(customer_id)
                                ); """

    if conn.is_connected():
        cursor = conn.cursor()

    try:
        cursor.execute(mySql_Create_custo_Query)
        print("Table created")

#Populate the customers Table with test data
n = 0

    while n < 11:
        n += 1
        row = [fake.name(), fake.address(), fake.email(), \
            fake.phone_number(), fake.city()]

            cursor.execute(' \
            INSERT INTO `customers` (customer_name, customer_address, customer_email, customer_phone, customer_city) \
            VALUES ("%s", "%s", "%s", %s, "%s"); \
            ' % (row[0], row[1], row[2], row[3], row[4]))

            if n == 10:
                print("iteration %s" % n)
                time.sleep(0.5)
                conn.commit()



    mySql_Create_carts_Query = """CREATE TABLE carts (
                                cart_id INT NOT NULL AUTO_INCREMENT,
                                customer_id INT,
                                total DECIMAL DEFAULT 0,
                                CONSTRAINT total
                                CHECK(total >= 0),
                                PRIMARY KEY(cart_id)
                                );"""

    mysql_alter_carts_query = """ALTER TABLE carts
                                  ADD CONSTRAINT customer_in_cart_fk1 FOREIGN KEY (customer_id) REFERENCES customers(customer_id);"""

#Populate the carts Table with test data

    mySql_Create_orders_Query = """CREATE TABLE orders (
                                        order_id INT NOT NULL AUTO_INCREMENT,
                                        cart_id INT,
                                        order_number INT NOT NULL,
                                        order_date DATE DEFAULT GETDATE(),
                                        PRIMARY KEY(order_id)
                                        );"""

    mysql_alter_orders_query = """ALTER TABLE orders
                                        ADD CONSTRAINT cart_in_order_fk1 FOREIGN KEY (cart_id) REFERENCES carts(cart_id);"""

#Populate the orders Table with test data

         mySql_Create_products_Query = """CREATE TABLE products (
                                        product_id INT NOT NULL AUTO_INCREMENT,
                                        product_name VARCHAR(150) NOT NULL,
                                        price DECIMAL(10,2) NOT NULL,
                                        created_at DATE DEFAULT GETDATE(),
                                        PRIMARY KEY(product_id)
                                        );
                                        """

#Populate the products Table with test data


    mySql_Create_cart_products_Query = """CREATE TABLE cart_products (
                                        cart_product_id INT NOT NULL AUTO_INCREMENT,
                                        cart_id INT,
                                        product_id INT,
                                        order_date DATE DEFAULT GETDATE(),
                                        PRIMARY KEY(cart_product_id)
                                        );"""


    mySql_alter_cart_products_Query = """ALTER TABLE cart_products
                                        ADD CONSTRAINT cart_in_cart_products_fk1 FOREIGN KEY (cart_id) REFERENCES carts(cart_id),
                                        ADD CONSTRAINT product_id_in_cart_products_fk2 FOREIGN KEY(product_id) REFERENCES products(product_id);"""

#Populate the cart_products Table with test data

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Laptop Table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
#https://pynative.com/python-mysql-database-connection/#h-python-mysql-crud-operation

#https://www.freecodecamp.org/news/python-sql-how-to-use-sql-databases-with-python/

con = psycopg2.connect(dbname= "db_name", host=config[hostname], port = config["port"],user=config["user_id"], password=config["password_key"])
cur = con.cursor()
query = "SELECT *
        FROM League JOIN Country
            ON Country.id = League.country_id;"
#Runs your SQL query
execute1 = cur.execute(query)
result = cur.fetchall()

#https://pynative.com/python-mysql-insert-data-into-database-table/
#https://www.w3schools.com/python/python_mysql_insert.asp

#closing database connection.
if(conn and conn.is_connected()):
    conn.commit()
    cursor.close()
    conn.close()
