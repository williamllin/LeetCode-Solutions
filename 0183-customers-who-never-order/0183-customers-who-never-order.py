import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    #how='left' -> LEFT JOIN
    #left_on-> customers' id，right_on -> orders' customerId
    df = customers.merge(orders, left_on='id', right_on='customerId', how='left')
    
    #get NA
    df1 = df[df['customerId'].isna()]
    
    #rename column
    result = df1[['name']].rename(columns={'name': 'Customers'})
    return result
