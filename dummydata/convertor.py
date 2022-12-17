from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

my_path='G:\\My Drive\\testing\\my_db\\my_db.db' # update path
my_conn = create_engine("sqlite:///../data.db") # connection object

import pandas as pd 
try:
  df = pd.read_excel('items.xlsx') # create DataFrame by reading Excel
  print(df.head()) # Print top 5 rows as sample
  df.to_sql(con=my_conn,name='items',if_exists='append') # create table.
except SQLAlchemyError as e:
  #print(e)
  error = str(e.__dict__['orig'])
  print(error)
else: # show all records to confirm
    r_set=my_conn.execute('SELECT * from items');
    for row in r_set:
        print(row)

try:
  df = pd.read_excel('sellers.xlsx') # create DataFrame by reading Excel
  print(df.head()) # Print top 5 rows as sample
  df.to_sql(con=my_conn,name='sellers',if_exists='append') # create table.
except SQLAlchemyError as e:
  #print(e)
  error = str(e.__dict__['orig'])
  print(error)
else: # show all records to confirm
    r_set=my_conn.execute('SELECT * from sellers');
    for row in r_set:
        print(row)

try:
  df = pd.read_excel('orders.xlsx') # create DataFrame by reading Excel
  print(df.head()) # Print top 5 rows as sample
  df.to_sql(con=my_conn,name='orders',if_exists='append') # create table.
except SQLAlchemyError as e:
  #print(e)
  error = str(e.__dict__['orig'])
  print(error)
else: # show all records to confirm
    r_set=my_conn.execute('SELECT * from orders');
    for row in r_set:
        print(row)

try:
  df = pd.read_excel('order_item.xlsx') # create DataFrame by reading Excel
  print(df.head()) # Print top 5 rows as sample
  df.to_sql(con=my_conn,name='order_item',if_exists='append') # create table.
except SQLAlchemyError as e:
  #print(e)
  error = str(e.__dict__['orig'])
  print(error)
else: # show all records to confirm
    r_set=my_conn.execute('SELECT * from order_item');
    for row in r_set:
        print(row)