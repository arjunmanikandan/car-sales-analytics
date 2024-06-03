#To display expensive car purchases by customers
import pandas as pd
from tabulate import tabulate
import sys

def read_input(csv_path):
    df = pd.read_csv(csv_path)
    return df

def process_input(car_sales_data):
    sorted_df = car_sales_data.sort_values(by="Price($)",ascending=False)
    return sorted_df

def display_output(customer_purchases,customer_count):
    customer_purchases = customer_purchases.head(customer_count)
    print(tabulate(customer_purchases[["Customer_Name","Price($)"]].values.tolist(),
    headers=["CUSTOMER_NAME","CAR_PRICE"],tablefmt="grid"))

def main():
    csv_path = "car_sales.csv"
    # Display number of customers based on user input
    cli_input= sys.argv
    customer_count = int(cli_input[1])
    car_sales_data = read_input(csv_path)
    customer_purchases = process_input(car_sales_data)
    display_output(customer_purchases,customer_count)

if __name__ == "__main__":
    main()