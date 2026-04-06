from config.db_config import connect_db
from database.queries import INSERT_ORDER

def place_order(customer, hotel, cart):
    if not cart:
        print("Cart is empty")
        return

    conn = connect_db()
    cur = conn.cursor()

    try:
        for item in cart:
            cur.execute(
                INSERT_ORDER,
                (customer, hotel, item['name'], 1)  # quantity for now = 1
            )

        conn.commit()
        print("Order placed successfully")

    except Exception as e:
        conn.rollback()
        print("Error placing order:", e)

    finally:
        conn.close()