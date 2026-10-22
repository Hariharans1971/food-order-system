# Food Order System

A desktop food-ordering application built with **Python Tkinter** and **PostgreSQL**. Users can browse hotels, view menus, add items to a cart, place orders, and store order data in a relational database.

## Features

- User login
- Browse available hotels
- View menu items
- Add items to a cart
- Place orders
- Persist application data in PostgreSQL

## Technology

- Python 3
- Tkinter
- PostgreSQL
- psycopg2

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Hariharans1971/food-order-system.git
cd food-order-system
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

- Windows PowerShell: `.venv\Scripts\Activate.ps1`
- macOS/Linux: `source .venv/bin/activate`

### 3. Install the database driver

```bash
python -m pip install psycopg2-binary
```

### 4. Configure PostgreSQL

- Install and start PostgreSQL.
- Create a database named `food_order`.
- Create the tables expected by the application (users, hotels, menu, and orders).
- Configure the database connection using environment variables or a local configuration file.

**Security note:** never commit real database passwords, API keys, or production credentials. If the project currently stores credentials in source code, replace them with local environment configuration before deploying it. Do not use sample credentials from a public README as real login details.

### 5. Run

```bash
python main.py
```

Run the command from the repository root. If your local version uses another entry-point filename, use the actual file in the project.

## Future improvements

- Add search and menu filtering
- Improve validation and user-facing error messages
- Add automated tests for cart and order workflows
- Use database migrations and parameterized SQL
- Improve UI accessibility and responsive layouts
- Add a clear setup script and sanitized screenshots

## Author

Hariharan S. — Aspiring AI Engineer and Full-Stack Developer
