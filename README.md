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

### 2. Create and activate a virtual environment

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
- Copy `.env.example` as a reference for the required environment variables. The application reads environment variables directly; it does not automatically load a `.env` file.

Set the variables in Windows PowerShell:

```powershell
$env:FOOD_ORDER_DB_NAME = "food_order"
$env:FOOD_ORDER_DB_USER = "postgres"
$env:FOOD_ORDER_DB_PASSWORD = "your-local-password"
$env:FOOD_ORDER_DB_HOST = "localhost"
$env:FOOD_ORDER_DB_PORT = "5432"
```

Or in macOS/Linux:

```bash
export FOOD_ORDER_DB_NAME=food_order
export FOOD_ORDER_DB_USER=postgres
export FOOD_ORDER_DB_PASSWORD='your-local-password'
export FOOD_ORDER_DB_HOST=localhost
export FOOD_ORDER_DB_PORT=5432
```

Use your own local PostgreSQL password. Never commit real passwords, API keys, or production credentials. The `.gitignore` excludes local `.env` files and common Python artifacts.

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
