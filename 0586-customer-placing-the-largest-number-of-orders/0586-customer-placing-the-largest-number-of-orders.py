import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    

    df = orders.groupby('customer_number',as_index=False)['order_number'].count()
    df_sort = df.sort_values(by='order_number', ascending = False)
    result = df_sort.head(1)[['customer_number']]
    return result