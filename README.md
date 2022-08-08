# new_training_sql

There is a repo to train (my)SQL!

Look at:
- database.sql (Instant creation of 'Test_SQL' DB)
- database.py (Fully manual, with Faker, seed in Python)
- Training_SQL.ipynb (SQL queries)

### Purposes:

- Play with (my)SQL
- Being able to do a **pure** SQL DBMS
- Testing Windows functions


### The steps:

- Install (Python Librairies):
	- [Python](https://www.python.org/downloads/)
	- [os](https://docs.python.org/fr/3/library/os.html)
	- [dotenv](https://pypi.org/project/python-dotenv/)
	- [time](https://docs.python.org/3/library/time.html)
	- [mysql.connector](https://dev.mysql.com/doc/connector-python/en/ )
	- [Faker](https://faker.readthedocs.io/)

- Create db schema (with ERD): (https://app.diagrams.net/)

- Create the database (mySQL)
	- Run code in mySQL (database_in_mysql.sql / database.sql)

- Python (database.py)
	- mysql.connector (connect to the database)
	- insert the datas (through faker) using SQL

- Database "good" for queries

**Some basic questions**:
- In this database, show the customers, products, finally the orders. 
- Display customers that put stuff in their carts, who ordered, pending carts.

**Calculations**:
- In this database, display the total number of customers, products and orders.
- In this database, show the number of pending carts. 
- In this database, display the total orders amount (let's change the times, 1 month)
- In this database, find the top 5 customers (ordered by spending amount)
- In this database find the flop 5 customers (ordered by spending amount)
- In this database, find the top 5 products. (ordered most, in quantity)
- In this database, find the average order, product's price.
- In this database, find the median order, product price.
- In this database, find ordered amount quartils
- In this database, find max et min total amount order
- In this database, find max et min total quantity ordered
- In this database, find max and min price products.
- Find all pending carts accumulated values

**Introduce Windows Functions**:
- Find the best amount spent by customer (max 1 order)
- Find all pending carts accumulated values
- For customers who ordered, display spending total amounts ranking by deciles
- Find per customer, the transactions ranks
- Let's rank ordered products by quantity send
- Get the average order per group of customer total spending


**Mix all queries**:
- Temporary column: Product's price classes (**low** < *33* < **medium** < *66* < **high**)
- Find the amount spend per customer
- Find the most ordered categories
- Display the total profits per category 
