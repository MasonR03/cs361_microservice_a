import csv
import os
import time
import argparse

def update_csv(file_path):
    """Reads the CSV, recalculates totals, and writes the updated file."""
    rows = []
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return

    if not rows or len(rows) < 2:
        print("CSV file does not have the expected format.")
        return

    header = rows[0]
    new_rows = [header]
    total_balance = 0.0

    # Process each row (except header) that is not the total_balance row.
    for row in rows[1:]:
        # If the first cell is "total_balance", skip for now.
        if row and row[0] == "total_balance":
            continue
        try:
            # Expecting row format: stock_name, quantity, current_price, total
            quantity = float(row[1])
            current_price = float(row[2])
            new_total = quantity * current_price
        except Exception as e:
            print(f"Error processing row {row}: {e}")
            new_total = row[3] if len(row) > 3 else ""
        new_rows.append([row[0], row[1], row[2], str(new_total)])
        total_balance += new_total

    # Append the total_balance row at the end.
    new_rows.append(["total_balance", "", "", str(total_balance)])

    try:
        with open(file_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(new_rows)
        print(f"Updated totals in {file_path}")
    except Exception as e:
        print(f"Error writing to file {file_path}: {e}")

def monitor_file(file_path):
    """Monitors the file for changes and updates the totals when a change is detected."""
    try:
        last_mtime = os.path.getmtime(file_path)
    except Exception as e:
        print(f"Error accessing file {file_path}: {e}")
        return

    print(f"Monitoring {file_path} for changes...")
    while True:
        time.sleep(1)
        try:
            current_mtime = os.path.getmtime(file_path)
        except Exception as e:
            print(f"Error accessing file {file_path}: {e}")
            continue

        # When a change is detected, update the CSV and reset the modification time.
        if current_mtime != last_mtime:
            print("Change detected. Recalculating totals...")
            update_csv(file_path)
            last_mtime = os.path.getmtime(file_path)

def main():
    parser = argparse.ArgumentParser(description="Recalculate and update totals in a CSV file.")
    parser.add_argument("path", help="Path to the CSV file.")
    parser.add_argument("--monitor", action="store_true",
                        help="Monitor the file continuously for changes.")
    args = parser.parse_args()

    if args.monitor:
        monitor_file(args.path)
    else:
        update_csv(args.path)

if __name__ == "__main__":
    main()
