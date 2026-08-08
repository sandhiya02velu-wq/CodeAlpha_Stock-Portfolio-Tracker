# Stock Portfolio Tracker
# CodeAlpha Internship - Task 2

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 185,
    "MSFT": 420
}

portfolio = []
total_investment = 0


print("=" * 60)
print("              📈 STOCK PORTFOLIO TRACKER")
print("=" * 60)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock:<8} - ${price} per share")

print("\n" + "-" * 60)

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Invalid stock symbol. Please try again.\n")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("❌ Quantity must be greater than 0.\n")
            continue

        price = stock_prices[stock]
        investment = price * quantity

        portfolio.append((stock, quantity, price, investment))
        total_investment += investment

        print(f"✅ {stock} added successfully!")
        print(f"Investment: ${investment}\n")

    except ValueError:
        print("❌ Please enter a valid quantity.\n")


print("\n" + "=" * 60)
print("                 PORTFOLIO SUMMARY")
print("=" * 60)

if portfolio:
    print(f"{'Stock':<10}{'Quantity':<12}{'Price':<12}{'Investment'}")
    print("-" * 60)

    for stock, quantity, price, investment in portfolio:
        print(
            f"{stock:<10}"
            f"{quantity:<12}"
            f"${price:<11}"
            f"${investment}"
        )

    print("-" * 60)
    print(f"Total Investment: ${total_investment}")
else:
    print("No stocks were added to the portfolio.")

print("=" * 60)

# Save portfolio to a text file
with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO TRACKER\n")
    file.write("=" * 50 + "\n\n")

    for stock, quantity, price, investment in portfolio:
        file.write(
            f"Stock: {stock} | "
            f"Quantity: {quantity} | "
            f"Price: ${price} | "
            f"Investment: ${investment}\n"
        )

    file.write("\n")
    file.write(f"Total Investment: ${total_investment}\n")

print("📁 Portfolio saved successfully to portfolio.txt")
print("=" * 60)
