CREATE DATABASE Test_SQL;
USE Test_SQL;


DROP TABLE cart_products;
DROP TABLE products;
DROP TABLE orders;
DROP TABLE carts;
DROP TABLE customers;

/* first table https://www.sqlstyle.guide/#create-syntax*/
CREATE TABLE customers (
  customer_id INT NOT NULL AUTO_INCREMENT, --AUTO_INCREMENT in MySQL
  customer_name VARCHAR(80) NOT NULL,
  customer_address VARCHAR(255), --if pas d'addresse, éviter d'aj..ter des c.mm.nd.s
  customer_email VARCHAR (50),
  customer_phone VARCHAR(15),
  customer_city VARCHAR(30),
  PRIMARY KEY(customer_id)
);

-- Populate the customers Table with test data


CREATE TABLE carts (
  cart_id INT NOT NULL AUTO_INCREMENT,
  customer_id INT,
  total DECIMAL DEFAULT 0,
    CONSTRAINT total
    CHECK(total >= 0),

  PRIMARY KEY(cart_id)
);

/* https://www.w3schools.com/mysql/mysql_foreignkey.asp */
ALTER TABLE carts
  ADD CONSTRAINT customer_in_cart_fk1 FOREIGN KEY (customer_id) REFERENCES customers(customer_id);

-- Populate the carts Table with test data



CREATE TABLE orders (
  order_id INT NOT NULL AUTO_INCREMENT,
  cart_id INT,
  order_date DATE DEFAULT GETDATE(), -- special MySQL: TIMESTAMP DEFAULT NOW(),

  PRIMARY KEY(order_id)
);

ALTER TABLE orders
  ADD CONSTRAINT cart_in_order_fk1 FOREIGN KEY (cart_id) REFERENCES carts(cart_id);

-- Populate the orders Table with test data


CREATE TABLE products (
  product_id INT NOT NULL AUTO_INCREMENT,
  product_name VARCHAR(150) NOT NULL,
  price DECIMAL(10,2) NOT NULL,
  created_at DATE DEFAULT GETDATE(), -- special MySQL: TIMESTAMP DEFAULT NOW(),

  PRIMARY KEY(product_id)
);

-- Populate the products Table with test data


CREATE TABLE cart_products (
  cart_product_id INT NOT NULL AUTO_INCREMENT,
  cart_id INT,
  product_id INT,
  quantity INT,
  created_at DATE DEFAULT GETDATE(), -- special MySQL: TIMESTAMP DEFAULT NOW(),

  PRIMARY KEY(cart_product_id)
);

ALTER TABLE cart_products
  ADD CONSTRAINT cart_in_cart_products_fk1 FOREIGN KEY (cart_id) REFERENCES carts(cart_id),
  ADD CONSTRAINT product_id_in_cart_products_fk2 FOREIGN KEY(product_id) REFERENCES products(product_id);

/* table customers, products + https://www.w3schools.com/python/python_mysql_create_db.asp*/
/* https://www.w3schools.com/mysql/mysql_create_index.asp */

-- Populate the cart_products Table with test data
