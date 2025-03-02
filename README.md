# Live Cryptocurrency Data Analysis

## Project Overview
This project fetches live cryptocurrency data for the top 50 cryptocurrencies by market capitalization, analyzes the data, and presents it in a live-updating Excel sheet. The analysis includes insights into market trends, price changes, and volume metrics. The Excel sheet updates every 5 minutes with the latest prices and data.

## Features
- Fetches live cryptocurrency data for the top 50 coins.
- Displays key metrics such as Cryptocurrency Name, Symbol, Current Price (in USD), Market Capitalization, 24-hour Trading Volume, and Price Change (24-hour, percentage).
- Updates the data every 5 minutes.
- Identifies the top 5 cryptocurrencies by market capitalization.
- Performs basic analysis and calculates the average price of the top 50 cryptocurrencies.

## Technologies Used
- Python (for API requests and data processing)
- Excel (for live data display)
- Public APIs (CoinGecko, CoinMarketCap, or Binance API)
- Pandas (for data processing)
- OpenPyXL (for handling Excel files)

## How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/live-cryptocurrency-data-analysis.git
cd live-cryptocurrency-data-analysis
