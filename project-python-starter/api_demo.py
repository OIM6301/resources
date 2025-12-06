"""
API Demonstration
Simple script to demonstrate API calling ability.

TODO: Complete this script to make an interactive API call.
Make sure to ask the user for input and use it in your API call!
"""

import urllib.request
import json


def fetch_api_data(user_input):
    """Fetch data from your chosen API based on user input.

    Args:
        user_input (str): User's input (e.g., country code, stock ticker, city name)

    TODO:
    1. Choose an API from the list in project-python.md
    2. Construct the API URL using the user_input parameter
    3. Make the API call using urllib.request.urlopen()
    4. Parse the JSON response using json.loads()
    5. Extract and return the relevant data
    6. Add try/except for error handling

    Example for Public Holidays API:
        url = f"https://date.nager.at/api/v3/PublicHolidays/2025/{user_input}"
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
        return data

    Example for REST Countries API:
        url = f"https://restcountries.com/v3.1/name/{user_input}"
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
        return data
    """
    try:
        # TODO: Construct your API URL using user_input
        url = f"YOUR_API_URL_HERE/{user_input}"

        # TODO: Make API call and parse JSON response
        # Hint: with urllib.request.urlopen(url) as response:
        #           data = json.loads(response.read().decode())

        # TODO: Extract relevant data from response

        pass

    except urllib.error.URLError as e:
        print(f"API Error: {e}")
        return None
    except KeyError as e:
        print(f"JSON parsing error: {e}")
        return None


def main():
    """Main function to demonstrate API calls."""
    print("=== API Demonstration ===\n")

    # TODO: Ask user for input (e.g., country code, stock ticker, city name)
    # Examples:
    # - "Enter country code (e.g., US, CN, GB): "
    # - "Enter country name (e.g., China, USA, Japan): "
    # - "Enter stock ticker (e.g., AAPL, MSFT): "
    user_input = input("Enter YOUR_PROMPT_HERE: ")

    # TODO: Call your API function with user's input
    result = fetch_api_data(user_input)

    # TODO: Display the results in a readable format
    # Examples:
    # - For holidays: loop through and print each holiday
    # - For country info: print capital, population, languages
    # - For stock: print current price, market cap, etc.
    if result:
        print(f"\nResults: {result}")
        # TODO: Format the output better based on your chosen API

    print("\n✅ API demonstration complete!")


if __name__ == "__main__":
    main()
