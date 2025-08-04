def stock_tracker():
    stock_price={"AAPL": 180, "TSLA": 250, "GOOG": 280, "MSFT": 310, "AMZN": 265}
    n=int(input("Enter number of stocks you want to buy : "))
    portfolio={}
    
    for i in range (n):
        stock=input("Enter stock symbol (eg., APPL/TSLA/GOOG/MSFT/AMZN) : ")
        quantity=int(input("Enter quantity of stock : "))
        if stock in stock_price:
            portfolio[stock]=quantity
        else:
            print("Stock not found!")
        
    price = sum(stock_price[stock] * quantity for stock, quantity in portfolio.items())
    print("Total stock value = $", price)
    
    with open ("stock portfilio.txt", 'w') as f:
        for stock, quantity in portfolio.items():
            f.write(f"{stock} : {quantity} x {stock_price[stock]} = {quantity * stock_price[stock]}\n")
        f.write(f"Total = ${price}")
        
stock_tracker()
        