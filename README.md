# Dispatch taxi

## Prerequisites

Install pip packages:

1. django
2. redis
3. django-redis-sessions
4. psycopg2 (database adapter that allows PostgreSQL to communicate to Python program)
   ````
   pip install
   ````

## Getting started

1. Run the Django server:
   ````
   python manage.py runserver
   ````

2. Run the Redis server (needed to store the user session):
   ````
   redis-server redis.conf
   ````

## Project guide

1. Open localhost, click sign in, click sign up to register a new user. Log in.
2. Start the Redis client by the `redis-cli` command to ensure that the session key has been generated. Enter the `select 0` command and then the `keys *` command to display the session key.
3. Fill in the "Phone number" and "Destination" fields. Register an order.
4. Log out. Enter the `keys *` command again to ensure that the session key has been removed. 
5. Log in as an Admin. Username/Password: admin. Make sure that the order is displayed in the list.
6. Run pgAdmin to ensure that PostgreSQL is connected to the project and the customer and user tables are displayed. Password: admin.