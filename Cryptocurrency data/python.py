from fpdf import FPDF


# Data (provided by user)
data = [
    {"name": "Bitcoin", "symbol": "btc", "current_price": 85956, "market_cap": 1.70574e+12, "total_volume": 22408151018, "price_change_percentage_24h": 1.14088},
    {"name": "Ethereum", "symbol": "eth", "current_price": 2217.4, "market_cap": 2.67534e+11, "total_volume": 14481826085, "price_change_percentage_24h": -0.72542},
    {"name": "Tether", "symbol": "usdt", "current_price": 0.999484, "market_cap": 1.4234e+11, "total_volume": 20392642500, "price_change_percentage_24h": -0.00169},
    {"name": "XRP", "symbol": "xrp", "current_price": 2.28, "market_cap": 1.31808e+11, "total_volume": 2717522728, "price_change_percentage_24h": 4.76007},
    # Add other coins in the same format...
]

# Analysis function to extract key insights
def analyze_data(data):
    highest_price = max(data, key=lambda x: x['current_price'])
    lowest_price = min(data, key=lambda x: x['current_price'])
    highest_market_cap = max(data, key=lambda x: x['market_cap'])
    lowest_market_cap = min(data, key=lambda x: x['market_cap'])
    
    analysis_text = [
        f"Highest Price: {highest_price['name']} ({highest_price['symbol']}) - ${highest_price['current_price']}",
        f"Lowest Price: {lowest_price['name']} ({lowest_price['symbol']}) - ${lowest_price['current_price']}",
        f"Highest Market Cap: {highest_market_cap['name']} ({highest_market_cap['symbol']}) - ${highest_market_cap['market_cap']}",
        f"Lowest Market Cap: {lowest_market_cap['name']} ({lowest_market_cap['symbol']}) - ${lowest_market_cap['market_cap']}",
        "\nPrice Changes over the Last 24 Hours:",
    ]
    
    for coin in data:
        analysis_text.append(f"{coin['name']} ({coin['symbol']}): {coin['price_change_percentage_24h']}% change")

    return "\n".join(analysis_text)

# Generate PDF Report
def generate_pdf_report(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Title
    pdf.cell(200, 10, txt="Cryptocurrency Data Analysis Report", ln=True, align="C")
    pdf.ln(10)
    
    # Write analysis to PDF
    pdf.multi_cell(0, 10, analyze_data(data))
    
    # Save PDF
    pdf.output("crypto_analysis_report.pdf")
    print("PDF Report Generated: crypto_analysis_report.pdf")


# Main function
if __name__ == "__main__":
    # Generate the reports
    generate_pdf_report(data)  # For PDF
