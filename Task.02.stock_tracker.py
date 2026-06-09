def stock_tracker():
    # Hardcoded dictionary
    prices = {"aapl": 180, "tsla": 258, "goog": 150, "msft": 400}
    portfolio = {}
    
    print("--- Stock Portfolio Tracker ---")
    print(f"Available stocks: {list(prices.keys())}")
    
    while True:
        stock = input("\nEnter stock symbol (or 'done' to calculate): ").lower()
        if stock == 'done': break
        
        if stock in prices:
            try:
                qty = int(input(f"Enter quantity for {stock}: "))
                portfolio[stock] = portfolio.get(stock, 0) + qty
            except ValueError:
                print("Invalid quantity! Please enter a number.")
        else:
            print("Stock symbol not found in our system!")

    total_value = sum(prices[s] * q for s, q in portfolio.items())
    
    # Display and Save
    result = f"Portfolio Summary: {portfolio}\nTotal Investment: ${total_value}"
    print(f"\n{result}")
    
    with open("portfolio_summary.txt", "w") as f:
        f.write(result)
        print("Result saved to 'portfolio_summary.txt'")

if __name__ == "__main__":
    stock_tracker()
  
