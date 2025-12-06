"""
Database Setup Script
This script creates a SQLite database and imports CSV data.

TODO: Complete the functions below to:
1. Create database tables
2. Import CSV files
3. Verify data was loaded correctly
"""

import sqlite3
import csv
import os


def create_database(db_path):
    """Create SQLite database and tables.

    Args:
        db_path (str): Path to the database file

    TODO:
    - Enable foreign key support with PRAGMA
    - Create customers table with columns: customer_id, name, email, city, join_date
    - Create products table with columns: product_id, name, category, price, cost
    - Create orders table with columns: order_id, customer_id, product_id, quantity, order_date
    - Don't forget foreign key constraints for orders table!
    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        # TODO: Enable foreign key support
        # Hint: cursor.execute("PRAGMA foreign_keys = ON;")

        # TODO: Create customers table
        # Hint: Use CREATE TABLE IF NOT EXISTS
        # Hint: customer_id should be INTEGER PRIMARY KEY

        # TODO: Create products table

        # TODO: Create orders table
        # Hint: Add FOREIGN KEY constraints referencing customers and products

        conn.commit()

    print(f"✓ Database created: {db_path}")


def import_csv(db_path, csv_file, table_name, skip_header=True):
    """Import CSV file into database table.

    Args:
        db_path (str): Path to the database file
        csv_file (str): Path to the CSV file
        table_name (str): Name of the table to import into
        skip_header (bool): Whether to skip the first row (header)

    TODO:
    - Check if CSV file exists
    - Open and read CSV file
    - Use cursor.executemany() with parameterized query
    - Remember to use ? placeholders for values
    """
    if not os.path.exists(csv_file):
        print(f"✗ Error: File not found: {csv_file}")
        return

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        # TODO: Open CSV file and read data
        # Hint: Use 'with open(csv_file, 'r', encoding='utf-8') as f:'
        # Hint: Use csv.reader(f)
        # Hint: Skip header if needed with next(csv_reader)

        # TODO: Import data using executemany
        # Example: cursor.executemany("INSERT INTO customers VALUES (?, ?, ?, ?, ?)", csv_reader)

        conn.commit()

    print(f"✓ Imported {csv_file} into {table_name}")


def verify_data(db_path):
    """Verify data was imported correctly by printing row counts.

    Args:
        db_path (str): Path to the database file

    TODO:
    - Query row count for each table
    - Print the counts
    - Show sample data from one table
    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        # TODO: Get and print row count for each table
        # Hint: SELECT COUNT(*) FROM table_name

        print("\n=== Database Verification ===")
        # TODO: Print row counts for customers, products, orders

        # TODO: Show sample data from customers table
        # Hint: SELECT * FROM customers LIMIT 5


def main():
    """Main function to set up the database."""
    # Database path
    DB_PATH = "data/ecommerce.db"

    # Create database and tables
    create_database(DB_PATH)

    # TODO: Import each CSV file
    # Uncomment and complete these lines:
    # import_csv(DB_PATH, "data/customers.csv", "customers")
    # import_csv(DB_PATH, "data/products.csv", "products")
    # import_csv(DB_PATH, "data/orders.csv", "orders")

    # Verify data
    verify_data(DB_PATH)


if __name__ == "__main__":
    main()
