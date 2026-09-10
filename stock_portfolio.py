stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 400,
    "AMZN": 180
}

stock = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))

if stock in stock_prices:
    price = stock_prices[stock]
    total = price * quantity

    print("Stock Price:", price)
    print("Quantity:", quantity)
    print("Total Investment:", total)
else:
    print("Stock not available")
