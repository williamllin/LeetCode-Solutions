import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df_count = orders.groupby('customer_number', as_index = False)['order_number'].count()
    df_sort = df_count.sort_values(by='order_number', ascending = False)#sort by descending order
    result = df_sort.head(1)[['customer_number']]#get top 1 from order
    return result