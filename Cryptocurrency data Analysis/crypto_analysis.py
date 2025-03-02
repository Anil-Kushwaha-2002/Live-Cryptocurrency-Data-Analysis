import requests
import pandas as pd
import time

import smtplib
import os

# Function to fetch live cryptocurrency data
def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,  # Fetch top 50 cryptocurrencies
        "page": 1,
        "sparkline": False
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data. Status Code:", response.status_code)
        return None

# Function to process data and convert it into a Pandas DataFrame
def process_data(crypto_data):
    df = pd.DataFrame(crypto_data, columns=["name", "symbol", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"])
    return df

# Function to perform analysis
def analyze_data(df):
    # Identify the top 5 cryptocurrencies by market cap
    top_5_cryptos = df.nlargest(5, "market_cap")[["name", "market_cap"]]
    
    # Calculate the average price of the top 50 cryptocurrencies
    average_price = df["current_price"].mean()
    
    # Find the highest and lowest 24-hour percentage price change
    highest_change = df.loc[df["price_change_percentage_24h"].idxmax()]
    lowest_change = df.loc[df["price_change_percentage_24h"].idxmin()]
    
    # Print analysis results
    print("\nTop 5 Cryptocurrencies by Market Cap:\n", top_5_cryptos)
    print(f"\nAverage Price of Top 50 Cryptocurrencies: ${average_price:.2f}")
    print(f"\nHighest 24-hour % Change: {highest_change['name']} ({highest_change['price_change_percentage_24h']}%)")
    print(f"Lowest 24-hour % Change: {lowest_change['name']} ({lowest_change['price_change_percentage_24h']}%)")
    
    return {
        "top_5_cryptos": top_5_cryptos,
        "average_price": average_price,
        "highest_change": highest_change,
        "lowest_change": lowest_change
    }


# Function to remove locked Excel file (if it's not open)
def remove_excel_file(filename):
    try:
        if os.path.exists(filename):
            os.remove(filename)
            print(f" Old file '{filename}' removed.")
    except PermissionError:
        print(f"Cannot delete '{filename}' - It's open in another program.")


# Function to update Excel file with live cryptocurrency data

def update_excel():
    while True:
        crypto_data = fetch_crypto_data()
        if crypto_data:
            df = process_data(crypto_data)
            filename = "crypto_live_data.xlsx"

            remove_excel_file(filename)  # Remove old file if possible

            try:
                df.to_excel(filename, index=False)
                print(f"\nExcel file '{filename}' updated successfully.")
            except PermissionError:
                print(f"⚠ Permission denied: '{filename}'. Close the file and retry.")

        time.sleep(300)  # Update every 5 minutes


# Run the script to update the Excel file continuously
update_excel()



# Function to send email alerts for significant price changes
def send_email_alert(crypto, price_change):
    sender = "kumaranil48309@gmail.com"  # Your email
    receiver = "kumaranil48309@gmail.com"  # Your email (or recipient's email)
    password = "123"  # App password (not your regular password)

    subject = f" Crypto Alert: {crypto} Price Change!"
    body = f"The price of {crypto} has changed by {price_change}% in the last 24 hours."

    message = f"Subject: {subject}\n\n{body}"

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, message)
        print(f" Alert Sent: {crypto} changed by {price_change}%")
    except Exception as e:
        print(f" Failed to send email: {e}")

