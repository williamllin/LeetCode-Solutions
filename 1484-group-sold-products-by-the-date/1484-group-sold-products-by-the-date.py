import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    df_res = activities.groupby('sell_date')['product'].agg(
        num_sold = 'nunique',
        products = lambda x: ','.join(sorted(set(x)))
    ).reset_index()

    df_res = df_res.sort_values(by='sell_date')
    return df_res