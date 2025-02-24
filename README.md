# Stock Balance Totals Microservice
# CS361 Microservice A

This microservice updates stock balance data stored in a CSV file by recalculating each stock's total (quantity * current_price) and ensuring that the `total_balance` row is correctly maintained. It also supports monitoring the CSV file for changes using Python's watchdog library.

---


## Usage

## Running the Microservice

**One-time update:**

python3 totals.py path/to/your/stock_data.csv

**Continuous Monitoring:**

python3 totals.py path/to/your/stock_data.csv --monitor


## Programmatic Request / Receive

To programmatically update the CSV file totals, call the request_update function from the microservice. This function reads your CSV file, recalculates each stock’s total (quantity * current_price), and writes back the updated data.

**Example**
    from totals import request_update

    # Replace with the path to your CSV file
    csv_path = 'path/to/your/stock_data.csv'
    request_update(csv_path)

To retrieve the updated total_balance row from your CSV file, use the read_updated_totals function.

**Example**
    from totals import read_updated_totals

    csv_path = 'path/to/your/stock_data.csv'
    total_balance = read_updated_totals(csv_path)
    print("Total Balance Row:", total_balance)
