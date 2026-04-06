import psycopg2

def connect_db():
    return psycopg2.connect(
        database="food_order",
        user="postgres",
        password="password",
        host="localhost",
        port="5432"
    )
