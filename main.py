#To provide summary or fetch a record from the Dataframe based on user_input
import sys
import pandas as pd
from tabulate import tabulate

def read_input(csv_path):
    df = pd.read_csv(csv_path)
    return df

def fetch_customer_details(user_query):
    field_names_list,df = ["Customer_Name"]+user_query["field_name"].split(","),user_query["data"]
    customer_details = df.loc[df["Customer_Name"] == user_query["customer_name"],field_names_list]
    return customer_details

def calc_summary_report(user_query):
    user_query["car_sales"] =  user_query["data"].groupby(user_query["field_name"])["Car_id"]
    generated_report = user_query["car_sales"].agg(user_query["report"]).reset_index()
    generated_report = generated_report.rename(columns=
    {"Car_id": user_query['col_name']}).sort_values(by=user_query["col_name"],ascending=False).reset_index(drop=True)
    return generated_report

def calc_report(user_query):
    call_functions ={
  "summary":calc_summary_report,
  "fetch":fetch_customer_details}
    return call_functions.get(user_query["action"])(user_query)

def process_input(user_query):
    customer_count = calc_report(user_query)
    return customer_count

def display_output(customer_purchases):
    print(tabulate(customer_purchases.values.tolist(),
    headers=list(customer_purchases),tablefmt="grid"))

def parse_cli_arguments(car_sales_data):
    arguments_length = len(sys.argv)
    if arguments_length == 4:
        user_query ={"customer_name":sys.argv[2],"field_name":sys.argv[3],}
    else:
        user_query ={"field_name":sys.argv[2],"report":sys.argv[3],"col_name":sys.argv[4]}
    user_query.update({"action":sys.argv[1],"data" : car_sales_data})
    return user_query

def main():
    # cli_input: summary Customer_Name count TOTAL_NO_OF_PERSONS
    # cli_input: fetch Grace/(Any Name) Gender,Annual_Income,Dealer_Name,Company(Colns based on user input)
    csv_path = "car_sales.csv"
    car_sales_data = read_input(csv_path)
    user_query = parse_cli_arguments(car_sales_data)
    company_sales = process_input(user_query)
    display_output(company_sales)

main()