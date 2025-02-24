from totals import request_update, read_updated_totals

def main():
    test_csv = "example.csv"
    
    
    # Call the microservice to update totals in the CSV file
    request_update(test_csv)
    
    # Programmatically retrieve the updated total_balance row
    total_balance = read_updated_totals(test_csv)
    print("Updated total_balance row:", total_balance)
    

if __name__ == "__main__":
    main()
