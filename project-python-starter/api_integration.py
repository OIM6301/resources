"""
API Integration Script
This script demonstrates how to integrate external APIs with your database.

TODO: Choose ONE of the following options:
- Option A: Integrate a public API (weather, stock, geocoding, etc.)
- Option B: Use OpenAI API for data insights

Complete the template for your chosen option.
"""

import sqlite3
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


# ============================================================================
# OPTION A: Public API Integration
# ============================================================================

def fetch_weather_data(city):
    """Fetch weather data for a given city using OpenWeather API.

    Example API Integration: Weather data for customer cities

    Args:
        city (str): City name

    Returns:
        dict: Weather data including temperature, description, etc.
    """
    import urllib.request
    import urllib.parse

    API_KEY = os.getenv("OPENWEATHER_API_KEY")

    if not API_KEY:
        print("Error: OPENWEATHER_API_KEY not found in .env file")
        return None

    try:
        # Construct API URL
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'  # Use Celsius
        }
        url = f"{base_url}?{urllib.parse.urlencode(params)}"

        # Make API request
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())

        # Extract relevant info
        weather_info = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity']
        }

        return weather_info

    except urllib.error.URLError as e:
        print(f"API Error: {e}")
        return None


def analyze_weather_impact(db_path):
    """Analyze if weather affects sales in different cities.

    Business question: Do sales patterns vary with weather conditions?

    TODO: Implement this function to:
    1. Get unique cities from customers table
    2. Fetch weather for each city
    3. Get sales data by city
    4. Combine and analyze

    Args:
        db_path (str): Path to database
    """
    # TODO: Implement your analysis
    pass


# ============================================================================
# OPTION B: OpenAI API Integration
# ============================================================================

def get_data_summary_for_ai(db_path):
    """Extract key metrics from database to send to AI.

    Args:
        db_path (str): Path to database

    Returns:
        str: Formatted summary text
    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        # Get summary statistics
        total_revenue = cursor.execute("""
            SELECT SUM(o.quantity * p.price)
            FROM orders o
            JOIN products p ON o.product_id = p.product_id
        """).fetchone()[0]

        # TODO: Add more metrics (top products, customer count, etc.)

        # Format summary
        summary = f"""
E-commerce Database Summary:

Total Revenue: ${total_revenue:,.2f}
[TODO: Add more metrics here]

Top 5 Products by Revenue:
[TODO: Query and format top products]

Sales by Category:
[TODO: Query and format category sales]
"""

    return summary


def generate_ai_insights(data_summary):
    """Use OpenAI API to generate business insights from data.

    Args:
        data_summary (str): Text summary of data

    Returns:
        str: AI-generated insights
    """
    from openai import OpenAI

    API_KEY = os.getenv("OPENAI_API_KEY")

    if not API_KEY:
        print("Error: OPENAI_API_KEY not found in .env file")
        return None

    client = OpenAI(api_key=API_KEY)

    try:
        prompt = f"""
You are a business analyst reviewing e-commerce sales data.
Based on the following data summary, provide 3-5 actionable insights
and recommendations for the business:

{data_summary}

Focus on:
1. Trends and patterns
2. Growth opportunities
3. Potential risks or concerns
4. Specific, actionable recommendations

Be concise and business-focused.
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Use mini model to save costs
            messages=[
                {"role": "system", "content": "You are an expert business data analyst."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )

        insights = response.choices[0].message.content
        return insights

    except Exception as e:
        print(f"OpenAI API Error: {e}")
        return None


# ============================================================================
# Main Functions
# ============================================================================

def main_option_a():
    """Main function for public API integration."""
    DB_PATH = "data/ecommerce.db"

    print("🌤️  Weather API Integration Demo\n")

    # Example: Get weather for a city
    city = "Boston"
    weather = fetch_weather_data(city)

    if weather:
        print(f"Weather in {weather['city']}:")
        print(f"  Temperature: {weather['temperature']}°C")
        print(f"  Conditions: {weather['description']}")
        print(f"  Humidity: {weather['humidity']}%")

    # TODO: Implement more sophisticated integration
    # analyze_weather_impact(DB_PATH)


def main_option_b():
    """Main function for OpenAI API integration."""
    DB_PATH = "data/ecommerce.db"

    print("🤖 AI Insights Generation\n")

    # Get data summary
    print("1. Extracting data summary...")
    summary = get_data_summary_for_ai(DB_PATH)
    print(summary)

    # Generate insights
    print("\n2. Generating AI insights...")
    insights = generate_ai_insights(summary)

    if insights:
        print("\n" + "=" * 60)
        print("AI-GENERATED BUSINESS INSIGHTS")
        print("=" * 60)
        print(insights)
        print("=" * 60)

        # Save to file
        with open("reports/ai_insights.txt", "w", encoding="utf-8") as f:
            f.write("AI-Generated Business Insights\n")
            f.write("=" * 60 + "\n\n")
            f.write(insights)

        print("\n✓ Insights saved to reports/ai_insights.txt")


def main():
    """Main function to run API demonstration."""
    print("Choose your API integration option:")
    print("A - Public API (Weather, Stock, etc.)")
    print("B - OpenAI API for insights")

    choice = input("\nEnter your choice (A/B): ").strip().upper()

    if choice == "A":
        main_option_a()
    elif choice == "B":
        main_option_b()
    else:
        print("Invalid choice. Please run again and choose A or B.")


if __name__ == "__main__":
    main()
