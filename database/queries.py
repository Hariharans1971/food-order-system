GET_USER = "SELECT * FROM users WHERE username=%s AND password=%s"
GET_HOTELS = "SELECT * FROM hotels"
GET_MENU = "SELECT * FROM menu WHERE hotel_id=%s"
INSERT_ORDER = """
INSERT INTO orders (customer_name, hotel_name, item_name, quantity)
VALUES (%s,%s,%s,%s)
"""