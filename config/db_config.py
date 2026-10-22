"""PostgreSQL connection configuration.

Set FOOD_ORDER_DB_NAME, FOOD_ORDER_DB_USER, FOOD_ORDER_DB_PASSWORD,
FOOD_ORDER_DB_HOST, and FOOD_ORDER_DB_PORT in your environment.
Do not commit real credentials to the repository.
"""
import os

import psycopg2


def connect_db():
    """Open a PostgreSQL connection using environment-based settings."""
    password = os.getenv("FOOD_ORDER_DB_PASSWORD")
    if not password:
        raise RuntimeError(
            "Missing FOOD_ORDER_DB_PASSWORD. Set it in your environment "
            "before starting the Food Order System."
        )

    return psycopg2.connect(
        database=os.getenv("FOOD_ORDER_DB_NAME", "food_order"),
        user=os.getenv("FOOD_ORDER_DB_USER", "postgres"),
        password=password,
        host=os.getenv("FOOD_ORDER_DB_HOST", "localhost"),
        port=os.getenv("FOOD_ORDER_DB_PORT", "5432"),
    )
