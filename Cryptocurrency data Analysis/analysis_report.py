import pandas as pd
import requests

# Function to fetch cryptocurrency data
def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
        "sparkline": False
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data")
        return None

# Fetch data
crypto_data = fetch_crypto_data()

# Convert to DataFrame
if crypto_data:
    df = pd.DataFrame(crypto_data, columns=["name", "symbol", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"])

    # Top 5 Cryptos by Market Cap
    top_5 = df.nlargest(5, "market_cap")
    print("\nTop 10 Cryptocurrencies by Market Cap:\n", top_5)

    # Save Report as Excel File
    df.to_excel("crypto_analysis_report.xlsx", index=False)
    print("\nAnalysis Report Saved Successfully as 'crypto_analysis_report.xlsx'.")

else:
    print("\nFailed to fetch cryptocurrency data.")
