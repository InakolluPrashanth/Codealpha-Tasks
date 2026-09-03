# CodeAlpha Internship - Task 2
# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180,
    "META": 500,
    "NVDA": 120
}

portfolio = {}
total_investment = 0

print("=" * 45)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 45)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

print("\nEnter 'done' when you have finished adding stocks.")

# Take user input
while True:
    stock = input("\nEnter stock symbol: ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not found. Please choose from the available stocks.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))

        if quantity <= 0:
            print("❌ Quantity must be greater than 0.")
            continue

    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    # Store stock quantity
    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Calculate total investment
print("\n" + "=" * 45)
print("          PORTFOLIO SUMMARY")
print("=" * 45)

report = []
report.append("STOCK PORTFOLIO TRACKER")
report.append("=" * 45)

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    result = (
        f"{stock} | Quantity: {quantity} | "
        f"Price: ${price} | Value: ${investment}"
    )

    print(result)
    report.append(result)

print("-" * 45)
print(f"TOTAL INVESTMENT: ${total_investment}")
print("=" * 45)

report.append("-" * 45)
report.append(f"TOTAL INVESTMENT: ${total_investment}")
report.append("=" * 45)

# Save result to text file
with open("portfolio_report.txt", "w") as file:
    file.write("\n".join(report))

print("\n✅ Portfolio report saved as 'portfolio_report.txt'")