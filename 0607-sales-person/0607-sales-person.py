import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    order_with_company = orders.merge(company, on='com_id', how='inner')
    red_sales_id = order_with_company.loc[order_with_company['name'] == 'RED', 'sales_id']

    result = sales_person [~sales_person['sales_id'].isin(red_sales_id)]
    return result[['name']]