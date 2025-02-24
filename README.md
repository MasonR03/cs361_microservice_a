# Stock Balance Totals Microservice
# CS361 Microservice A

This microservice updates stock balance data stored in a CSV file by recalculating each stock's total (quantity * current_price) and ensuring that the `total_balance` row is correctly maintained. It also supports monitoring the CSV file for changes using Python's watchdog library, as well as the ability to return the total balance with a function call. 

---


## Usage

**One-time update:**

```python3 totals.py path/to/your/stock_data.csv```

**Continuous Monitoring:**

```python3 totals.py path/to/your/stock_data.csv --monitor```

<br>
<br>

**Example to Update CSV File Totals**

```python
from totals import request_update
# Replace with the path to your CSV file
csv_path = 'path/to/your/stock_data.csv'
request_update(csv_path)
```

**Example to Retrieve the Updated Total Balance**

```python
from totals import read_updated_totals
csv_path = 'path/to/your/stock_data.csv'
total_balance = read_updated_totals(csv_path)
print("Total Balance Row:", total_balance)
```
<img width="543" alt="Screenshot 2025-02-23 at 5 35 15 PM" src="https://github.com/user-attachments/assets/63ea2615-747a-4d04-a7ee-f8948cf3f987" />
