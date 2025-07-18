import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = customers.merge(orders, left_on='id', right_on='customerId', how='left')
    result = merged[merged['id_y'].isna()][['name']].rename(columns={'name': 'Customers'})
    return result
