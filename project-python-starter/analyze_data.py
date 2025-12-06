"""
Data Analysis Script
This script performs analytical queries on the e-commerce database.

TODO: Complete 5 query functions.
- Query 1-2: SQL only
- Query 3-5: BOTH SQL and Python versions (same results, different approach)
"""

import sqlite3


def query1_customers_by_city(db_path, city):
    """Find all customers from a specific city.

    Business question: Which customers are in Boston for local marketing?

    Args:
        db_path (str): Path to database
        city (str): City name to filter by

    Returns:
        list: List of tuples with customer data

    TODO: Write SQL query to select all customers where city matches the parameter
    Hint: Use parameterized query with ? placeholder
    """
    # TODO: Implement this query
    pass


def query2_revenue_by_category(db_path):
    """Calculate total revenue by product category.

    Business question: Which product categories generate the most revenue?

    Returns:
        list: List of tuples (category, total_revenue)

    TODO: Write a query that:
    - Joins orders and products tables
    - Calculates revenue (price * quantity)
    - Groups by category
    - Orders by total revenue (highest first)
    """
    # TODO: Implement this query
    pass


# ============================================================================
# Query 3: Top Customers - BOTH SQL and Python versions required!
# ============================================================================

def query3_top_customers_sql(db_path, limit=5):
    """Find top N customers by total spending - SQL VERSION.

    Business question: Who are our most valuable customers?

    TODO: Implement using SQL
    - JOIN customers, orders, and products
    - Use SUM(quantity * price) to calculate total per customer
    - GROUP BY customer
    - ORDER BY total DESC
    - LIMIT to top N
    """
    # TODO: Implement SQL version
    # Example structure:
    # query = """
    #     SELECT c.name, SUM(o.quantity * p.price) as total
    #     FROM customers c
    #     JOIN orders o ON ...
    #     JOIN products p ON ...
    #     GROUP BY ...
    #     ORDER BY ...
    #     LIMIT ?
    # """
    pass


def query3_top_customers_python(db_path, limit=5):
    """Find top N customers by total spending - PYTHON VERSION.

    Business question: Who are our most valuable customers?

    TODO: Implement using Python (NO GROUP BY in SQL!)

    Step 1: Get data with a simple JOIN (no grouping)
    query = '''
        SELECT c.customer_id, c.name, o.quantity, p.price
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        JOIN products p ON o.product_id = p.product_id
    '''

    Step 2: Process in Python
    - Create dict to accumulate: customer_spending = {customer_id: {'name': ..., 'total': 0}}
    - Loop through results
    - Calculate spending = quantity * price for each row
    - Add to customer's total in the dict

    Step 3: Sort and return top N
    - Convert dict to list of tuples (name, total)
    - Sort by total (use sorted() with key parameter or lambda)
    - Return first N items (list slicing [:limit])

    Python concepts tested:
    - Dictionaries (storing customer data)
    - Loops (processing each order)
    - Arithmetic (calculating spending)
    - Sorting (sorted() function)
    - List slicing (getting top N)
    """
    # TODO: Implement Python version following the strategy above
    pass


# ============================================================================
# Query 4: Monthly Sales Trend - BOTH SQL and Python versions required!
# ============================================================================

def query4_monthly_sales_sql(db_path):
    """Calculate monthly sales trend - SQL VERSION.

    Business question: How are our sales trending over time?

    TODO: Implement using SQL
    - Use strftime('%Y-%m', order_date) to extract year-month
    - JOIN orders and products
    - Calculate SUM(quantity * price) per month
    - GROUP BY month
    - ORDER BY month

    IMPORTANT: SQLite uses strftime() - AI might suggest MySQL's MONTH()!
    """
    # TODO: Implement SQL version
    pass


def query4_monthly_sales_python(db_path):
    """Calculate monthly sales trend - PYTHON VERSION.

    Business question: How are our sales trending over time?

    TODO: Implement using Python (NO GROUP BY in SQL!)

    Step 1: Get data with simple JOIN (no grouping)
    query = '''
        SELECT o.order_date, o.quantity, p.price
        FROM orders o
        JOIN products p ON o.product_id = p.product_id
    '''

    Step 2: Process in Python
    - Create dict: monthly_sales = {}  # {year_month: total_revenue}
    - Loop through results
    - Extract month from order_date using string slicing:
      year_month = order_date[:7]  # '2024-01-15' → '2024-01'
    - Calculate revenue = quantity * price
    - Add to monthly total:
      if year_month in monthly_sales:
          monthly_sales[year_month] += revenue
      else:
          monthly_sales[year_month] = revenue

    Step 3: Sort and convert to list of tuples
    - Use sorted(monthly_sales.items()) to sort by month
    - Returns list of (month, revenue) tuples

    Python concepts tested:
    - Dictionaries (grouping by month)
    - String slicing (extracting date parts)
    - Loops (processing orders)
    - Conditionals (checking if key exists)
    - Dictionary methods (.items(), sorted())
    """
    # TODO: Implement Python version
    pass


# ============================================================================
# Query 5: Your Creative Analysis - BOTH SQL and Python versions required!
# ============================================================================

def query5_custom_sql(db_path):
    """Your own creative analysis - SQL VERSION.

    Business question: [TODO: Define your own question]

    Example ideas:
    - Product profitability: (SUM(quantity * price) - SUM(quantity * cost)) per product
    - Customer purchase frequency: COUNT(DISTINCT order_id) per customer
    - Best selling products: SUM(quantity) per product, ordered DESC
    - Average order value per city: AVG(quantity * price) grouped by city

    TODO: Design and implement your own query using SQL JOIN and GROUP BY
    """
    # TODO: Implement your creative SQL query
    pass


def query5_custom_python(db_path):
    """Your own creative analysis - PYTHON VERSION.

    Business question: [Same as SQL version]

    TODO: Implement the same analysis using Python
    Strategy (example for product profitability):
    1. Query: SELECT p.name, o.quantity, p.price, p.cost FROM orders o JOIN products p
    2. Python dict: product_profit = {product_name: 0}
    3. Loop: calculate profit = quantity * (price - cost), add to dict
    4. Sort by profit
    5. Return top results

    Adapt this strategy to your chosen analysis!

    Make sure to use:
    - Dictionaries for grouping/aggregating
    - Loops for processing
    - Conditionals if needed
    - Sorting
    """
    # TODO: Implement Python version
    pass


def main():
    """Main function to run all queries."""
    DB_PATH = "data/ecommerce.db"

    print("=== Analysis Results ===\n")

    # TODO: Run Query 1
    # print("1. Customers in Boston:")
    # results = query1_customers_by_city(DB_PATH, "Boston")
    # for row in results:
    #     print(row)

    # TODO: Run Query 2
    # print("\n2. Revenue by Category:")
    # results = query2_revenue_by_category(DB_PATH)
    # for row in results:
    #     print(f"  {row[0]}: ${row[1]:,.2f}")

    # TODO: Run Query 3 - BOTH versions and verify they match
    # print("\n3. Top 5 Customers:")
    # print("  (a) SQL version:")
    # results_sql = query3_top_customers_sql(DB_PATH, 5)
    # for row in results_sql:
    #     print(f"    {row[0]}: ${row[1]:,.2f}")
    #
    # print("  (b) Python version:")
    # results_python = query3_top_customers_python(DB_PATH, 5)
    # for row in results_python:
    #     print(f"    {row[0]}: ${row[1]:,.2f}")
    #
    # # Verify results match
    # if results_sql == results_python:
    #     print("  ✓ Both versions produce the same results!")

    # TODO: Run Query 4 - BOTH versions

    # TODO: Run Query 5 - BOTH versions


if __name__ == "__main__":
    main()
