import requests  # Import the requests library for making API calls

# Your API key for the currency conversion API
API_KEY = 'YOUR_API_KEY_HERE'
# Base URL for API requests
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

# List of supported currencies
CURRENCIES = ["EUR", "USD", "JPY", "BGN", "CZK", "DKK", "GBP", "HUF", "PLN", "RON", "SEK",
              "CHF", "ISK", "NOK", "HRK", "RUB", "TRY", "AUD", "BRL", "CAD", "CNY", "HKD",
              "IDR", "ILS", "INR", "KRW", "MXN", "MYR", "NZD", "PHP", "SGD", "THB", "ZAR"]


def convert_currency(base):
    """Fetches and returns currency exchange rates from the API.

    Args:
        base (str): The base currency to convert from.

    Returns:
        dict: A dictionary containing the exchange rates, or None if an error occurs.
    """

    # Combine currencies into a comma-separated string
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={
        currencies}"  # Construct the full API request URL
    try:
        response = requests.get(url)  # Send a GET request to the API
        data = response.json()  # Parse the JSON response
        return data["data"]  # Extract the exchange rates from the response
    except:
        print("Invalid currency")
        return None


while True:
    base = input("Enter the base currency (q for quit):").upper()

    if base == 'Q':
        break

    data = convert_currency(base)
    if not data:
        continue

    del data[base]
    for ticker, value in data.items():
        print(f"{ticker}: {value}")
