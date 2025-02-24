# Stock Balance Totals Microservice
# CS361 Microservice A

This microservice updates stock balance data stored in a CSV file by recalculating each stock's total (quantity * current_price) and ensuring that the `total_balance` row is correctly maintained. It also supports monitoring the CSV file for changes using Python's watchdog library, as well as the ability to return the total balance with a function call. 

---


## Usage

**One-time update:**

```python3 totals.py path/to/your/stock_data.csv```

**Continuous Monitoring:**

```python3 totals.py --monitor path/to/your/stock_data.csv```

<br>
<br>

## Example: Creating a CSV File for Monitoring

Below is an example of how to create a CSV file that can be monitored by the microservice:

```python
import csv

def write_csv(stocks):
    with open("example1.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)

        # Write header
        writer.writerow(["stock_name", "quantity", "current_price", "total"])

        # Write each stock row without calculations
        for stock in stocks:
            writer.writerow([stock["stock_name"], stock["quantity"], stock["current_price"], ""])
        
        # Append a row for the total balance
        writer.writerow(["total_balance", "", "", ""])
```

Then simply monitor the file with the microservice by using the monitor flag

```python3 totals.py --monitor example1.csv```    

<img width="543" alt="Screenshot 2025-02-23 at 5 35 15 PM" src="https://github.com/user-attachments/assets/63ea2615-747a-4d04-a7ee-f8948cf3f987" />


<br>

## Mitigation Plan
For which teammate did you implement “Microservice A”?

    I implemented Microservice A for Elliott.
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

