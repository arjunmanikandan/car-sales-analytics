#To display highest car sales volume by each company
import pandas as pd
from tabulate import tabulate

def read_input(csv_path):
    df = pd.read_csv(csv_path)
    return df

def process_input(car_sales_data):
    car_sales_data= car_sales_data.groupby("Company")["Price($)"].sum()
    # Reset index and rename columns to avoid Companies as index labels
    car_sales_data = car_sales_data.reset_index()
    car_sales_data = car_sales_data.rename(columns = {'Price($)': 'TOTAL_REVENUE($)'})
    return car_sales_data

def display_output(customer_purchases):
    print(tabulate(customer_purchases.values.tolist(),
    headers=list(customer_purchases),tablefmt="grid"))
    
def main():
    csv_path = "car_sales.csv"
    car_sales_data = read_input(csv_path)
    company_sales = process_input(car_sales_data)
    display_output(company_sales)

if __name__ == "__main__":
    main()