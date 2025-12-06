"""
Report Generation Script
This script generates reports and exports data from the database.

TODO: Complete functions to export CSV and generate text reports.
"""

import sqlite3
import csv
from datetime import datetime


def export_to_csv(data, filename, headers):
    """Export query results to CSV file.

    Args:
        data (list): List of tuples containing data
        filename (str): Output CSV filename
        headers (list): Column headers

    TODO: Write data to CSV file with headers
    Hint: Use csv.writer and writerow/writerows
    """
    # TODO: Open file and create CSV writer
    # TODO: Write headers
    # TODO: Write data rows
    pass


def get_top_products(db_path, limit=10):
    """Get top products by revenue.

    Args:
        db_path (str): Path to database
        limit (int): Number of top products

    Returns:
        list: List of tuples (product_name, category, units_sold, total_revenue)

    TODO: Write query to:
    - Join orders and products
    - Calculate total units sold (SUM of quantity)
    - Calculate total revenue (SUM of quantity * price)
    - Group by product
    - Order by revenue descending
    - Limit to top N
    """
    # TODO: Implement this query
    pass


def generate_summary_report(db_path, output_file="reports/summary_report.txt"):
    """Generate a text-based summary report with key business metrics.

    Args:
        db_path (str): Path to database
        output_file (str): Output file path

    TODO: Calculate and write to file 3-5 simple summary statistics.
    Examples (pick any 3-5):
    - Total revenue
    - Total number of orders
    - Number of customers
    - Average order value
    - Best selling category
    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        # TODO: Query for total revenue
        # Hint: SELECT SUM(o.quantity * p.price) FROM orders o JOIN products p ...

        # TODO: Query for total orders
        # Hint: SELECT COUNT(*) FROM orders

        # TODO: Query for total customers
        # Hint: SELECT COUNT(*) FROM customers

        # TODO: Calculate average order value (total_revenue / total_orders)

        # TODO: Query for best selling category
        # Hint: Similar to revenue by category query

        pass

    # TODO: Write all statistics to text file
    # Hint: Open file with 'w' mode
    # Hint: Format nicely with line breaks and spacing
    pass


def main():
    """Main function to generate reports."""
    import os

    # Create reports directory if it doesn't exist
    os.makedirs("reports", exist_ok=True)

    DB_PATH = "data/ecommerce.db"

    print("📊 Generating Reports...\n")

    # TODO: Export top products to CSV
    # print("1. Exporting top products...")
    # top_products = get_top_products(DB_PATH, limit=10)
    # export_to_csv(
    #     top_products,
    #     "reports/top_products.csv",
    #     ["Product Name", "Category", "Units Sold", "Total Revenue"]
    # )

    # TODO: Generate summary report
    # print("\n2. Generating summary report...")
    # generate_summary_report(DB_PATH)

    # print("\n✅ All reports generated successfully!")


if __name__ == "__main__":
    main()
