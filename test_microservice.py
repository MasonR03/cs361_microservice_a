import csv
import random
import time

# Initial stock data
stocks = [
    {"stock_name": "AAPL", "quantity": 68, "current_price": 11},
    {"stock_name": "GOOGL", "quantity": 4, "current_price": 10},
    {"stock_name": "AMZN", "quantity": 1, "current_price": 10},
    {"stock_name": "TSLA", "quantity": 1, "current_price": 100}
]

def write_csv(stocks):
    with open("example1.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        # Write header
        writer.writerow(["stock_name", "quantity", "current_price", "total"])
        # Write stock rows without any calculations (total left blank)
        for stock in stocks:
            writer.writerow([stock["stock_name"], stock["quantity"], stock["current_price"], ""])
        # Write total_balance row with blank total_balance
        writer.writerow(["total_balance", "", "", ""])

while True:
    # Update the quantity for each stock randomly (between 1 and 100)
    for stock in stocks:
        stock["quantity"] = random.randint(1, 100)
    
    # Write the updated data to the CSV file
    write_csv(stocks)
    print("CSV updated with new random quantities.")
    
    # Wait for 10 seconds before the next update
    time.sleep(5)
