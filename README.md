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


<br>

## Mitigation Plan
For which teammate did you implement “Microservice A”?

    I implemented Microservice A for [Teammate Name].
Current status of the microservice:

    The microservice is complete and fully functional.
Access Details:

    You can clone the repository from GitHub using the following link:
    https://github.com/MasonR03/cs361_microservice_a

Execution: 
    
    The microservice is designed to be run locally. You should run the code on your local machine.

In case of issues accessing/calling the microservice:

    If you experience any issues, please contact me directly via Discord or email rauschkm@oregonstate.edu
    I am available during regular working hours (9 AM – 5 PM, Monday to Friday).
    Please inform me within 24 hours of an assignment due date if you encounter issues.

Dependencies:

    Ensure that all dependencies (Python module watchdog) are installed.
    If not, please install them using "pip install watchdog".

