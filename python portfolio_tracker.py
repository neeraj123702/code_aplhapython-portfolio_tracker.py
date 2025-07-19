
stock_prices = {
    "AAPL": 15000,
    "TSLA": 21000,
    "GOOGL": 12000,
    "AMZN": 11000,
    "MSFT": 26500
}

portfolio = {}

print("📈 Stock Portfolio Tracker (INR ₹)")
print("Available stocks:", ", ".join(stock_prices.keys()))
print("Enter stock symbols and quantities (type 'done' to finish):")

while True:
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("❌ Stock not found. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        if quantity <= 0:
            print("❌ Quantity must be greater than 0.")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    except ValueError:
        print("❌ Invalid number. Please enter digits only.")

total = 0
print("\n📊 Investment Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total += value
    print(f"{stock} - Qty: {qty}, Price: ₹{price}, Value: ₹{value}")

print(f"\n💰 Total Investment: ₹{total}")

save = input("\nDo you want to save this report to 'portfolio.txt'? (yes/no): ").lower()
if save == "yes":
    with open("portfolio.txt", "w") as f:
        f.write("Stock Portfolio Summary (INR ₹)\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            f.write(f"{stock} - Qty: {qty}, Price: ₹{price}, Value: ₹{value}\n")
        f.write(f"\nTotal Investment: ₹{total}")
    print("✅ Report saved to 'portfolio.txt'")
