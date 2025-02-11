import csv
import os
import time
import logging
from datetime import datetime
import argparse

# Import watchdog modules for file monitoring
try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ImportError:
    print("Please install watchdog: pip install watchdog")
    exit(1)

# Set up error logging with timestamp and error code
logging.basicConfig(
    filename='error.log',
    level=logging.ERROR,
    format='%(asctime)s %(levelname)s %(message)s'
)


def request_update(csv_file_path):
    """
    Reads the CSV file, recalculates each stock’s total (quantity * current_price),
    updates the file with correct totals, and updates (or creates) the total_balance row.
    
    Parameters:
        csv_file_path (str): The path to the CSV file.
        
    Behavior:
        - If a valid CSV file is provided, the function recalculates the totals.
        - If an error occurs (e.g. missing file, bad data), an error is logged.
    """
    try:
        if not os.path.exists(csv_file_path):
            raise FileNotFoundError(f"CSV file not found: {csv_file_path}")

        # Read the CSV file
        with open(csv_file_path, mode='r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)

        if not rows:
            raise ValueError("CSV file is empty.")

        header = rows[0]
        # Validate header (expecting at least four columns)
        header = [col.strip().lower() for col in header]  # Trim spaces
        if header != ['stock_name', 'quantity', 'current_price', 'total']:
            total_sum = 0.0
            new_rows = [header]
            total_balance_index = None

        # Process each row (starting from the second row)
        for i, row in enumerate(rows[1:], start=1):
            # Skip empty rows
            if not row or len(row) < 4:
                continue

            # Check if this is the total_balance row (case-insensitive)
            if row[0].strip().lower() == "total_balance":
                total_balance_index = i
                # Append the row now; we will update the total later
                new_rows.append(row)
                continue

            try:
                # Convert quantity and current_price to numbers (supporting decimals)
                quantity = float(row[1])
                current_price = float(row[2])
            except ValueError as ve:
                raise ValueError(f"Invalid numeric value in row {i}: {row}") from ve

            # Recalculate the total for this stock
            new_total = quantity * current_price
            row[3] = str(new_total)
            total_sum += new_total
            new_rows.append(row)

        # Update or add the total_balance row
        if total_balance_index is not None:
            total_balance_row = new_rows[total_balance_index]
            total_balance_row[3] = str(total_sum)
            new_rows[total_balance_index] = total_balance_row
        else:
            # Append a new total_balance row if one was not found
            new_rows.append(["total_balance", "", "", str(total_sum)])

        # Write the updated rows back to the CSV file
        with open(csv_file_path, mode='w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(new_rows)

        print(f"CSV file '{csv_file_path}' updated successfully.")

    except Exception as e:
        error_code = "ERR001"
        logging.error(f"{error_code}: Error processing CSV file {csv_file_path}: {str(e)}")
        print(f"Error processing CSV file {csv_file_path}. See error.log for details.")


def read_updated_totals(csv_file_path):
    """
    Reads the CSV file and returns the total_balance row.

    Parameters:
        csv_file_path (str): The path to the CSV file.

    Returns:
        list or None: The total_balance row as a list, or None if not found or error occurs.
    """
    try:
        with open(csv_file_path, mode='r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row and row[0].strip().lower() == "total_balance":
                    return row
    except Exception as e:
        logging.error(f"ERR002: Error reading updated totals from CSV file {csv_file_path}: {str(e)}")
    return None


class CSVFileEventHandler(FileSystemEventHandler):
    """
    A file system event handler that listens for modifications to the target CSV file.
    When a change is detected, it calls the request_update function.
    """
    def __init__(self, csv_file_path):
        self.csv_file_path = os.path.abspath(csv_file_path)
        super().__init__()

    def on_modified(self, event):
        # Check if the modified file is the target CSV file
        if os.path.abspath(event.src_path) == self.csv_file_path:
            print(f"Detected change in '{self.csv_file_path}'. Updating totals...")
            request_update(self.csv_file_path)


def monitor_csv(csv_file_path):
    """
    Monitors the specified CSV file for any changes and automatically updates totals
    whenever a modification is detected.
    
    Parameters:
        csv_file_path (str): The path to the CSV file.
    """
    event_handler = CSVFileEventHandler(csv_file_path)
    observer = Observer()

    # Monitor the directory containing the CSV file (non-recursive)
    directory = os.path.dirname(os.path.abspath(csv_file_path))
    observer.schedule(event_handler, directory, recursive=False)
    observer.start()
    print(f"Monitoring '{csv_file_path}' for changes. Press Ctrl+C to stop.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping file monitor.")
        observer.stop()
    observer.join()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Stock Balance Totals Calculator Microservice"
    )
    parser.add_argument("csv_file_path", help="Path to the CSV file containing stock balance data")
    parser.add_argument(
        "--monitor",
        action="store_true",
        help="Continuously monitor the CSV file for changes and update totals automatically."
    )
    args = parser.parse_args()

    if args.monitor:
        monitor_csv(args.csv_file_path)
    else:
        request_update(args.csv_file_path)
