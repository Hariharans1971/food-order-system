from config.db_config import connect_db

def get_hotels():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM hotels")
    data = cur.fetchall()

    conn.close()
    return data


def get_menu(hotel_id):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute(
        "SELECT item_name, price FROM menu WHERE hotel_id=%s",
        (hotel_id,)
    )

    data = cur.fetchall()

    conn.close()
    return data