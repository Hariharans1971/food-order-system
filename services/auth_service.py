from config.db_config import connect_db
from database.queries import GET_USER

def login_user(username, password):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute(GET_USER, (username, password))
    user = cur.fetchone()

    conn.close()
    return user