# Stock Balance Totals Microservice
# CS361 Microservice A

This microservice updates stock balance data stored in a CSV file by recalculating each stock's total (quantity * current_price) and ensuring that the `total_balance` row is correctly maintained. It also supports monitoring the CSV file for changes using Python's watchdog library.

---


## Usage

**One-time update:**

```python3 totals.py path/to/your/stock_data.csv```

**Continuous Monitoring:**

```python3 totals.py path/to/your/stock_data.csv --monitor```




To programmatically update the CSV file totals, call the request_update function from the microservice. This function reads your CSV file, recalculates each stock’s total (quantity * current_price), and writes back the updated data.

**Example to Update CSV File Totals**

```python
from totals import request_update
# Replace with the path to your CSV file
csv_path = 'path/to/your/stock_data.csv'
request_update(csv_path)
```

To programmatically retrieve the updated balance, call the read_updated_totals function. This reads the totals column in the CSV file and returns
the total balance row.

**Example to Retrieve the Updated Total Balance**

```python
from totals import read_updated_totals
csv_path = 'path/to/your/stock_data.csv'
total_balance = read_updated_totals(csv_path)
print("Total Balance Row:", total_balance)
```
