# Simple Stock Portfolio Tracker

# fixed stock prices
stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 200
}

total_investment = 0

print("Available stocks:", list(stocks.keys()))
print("Type 'done' when you finish.\n")

while True:
    stock_name = input("Enter stock name: ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stocks:
        quantity = int(input("Enter quantity: "))
        price = stocks[stock_name]
        total = price * quantity
        total_investment += total
        print("Added", stock_name, "Value:", total)
    else:
        print("Stock not found in list.")

print("\nTotal Investment Value:", total_investment)

# optional: save result in a text file
file = open("portfolio.txt", "w")
file.write("Total Investment Value: " + str(total_investment))
file.close()

print("Result saved in portfolio.txt")