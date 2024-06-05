#To generate Total Customer Count and sort in desc order
import sys
import pandas as pd
from tabulate import tabulate

def read_input(csv_path):
    df = pd.read_csv(csv_path)
    return df

def calc_report(user_query):
    generated_report = user_query["car_sales"].agg(user_query["report"]).reset_index()
    generated_report = generated_report.rename(columns={"Car_id": user_query['col_name']}).sort_values(by=user_query["col_name"],ascending=False).head()
    return generated_report

def process_input(user_query):
    user_query["car_sales"] =  user_query["data"].groupby(user_query["field_name"])["Car_id"]
    customer_count = calc_report(user_query)
    return customer_count

def display_output(customer_purchases):
    print(tabulate(customer_purchases.values.tolist(),
    headers=list(customer_purchases),tablefmt="grid"))

def main():
    #User Input:Field Name ReportToGenerate NewColumnName 
    # sample Customer_Name count TOTAL_NO_OF_PERSONS
    field_name = sys.argv[1]
    report_to_generate = sys.argv[2]
    col_rename = sys.argv[3]
    csv_path = "car_sales.csv"
    car_sales_data = read_input(csv_path)
    user_query = {
    "data":car_sales_data,
    "field_name":field_name,
    "report": report_to_generate,
    "col_name": col_rename}
    company_sales = process_input(user_query)
    display_output(company_sales)

if __name__ == "__main__":
    main()
