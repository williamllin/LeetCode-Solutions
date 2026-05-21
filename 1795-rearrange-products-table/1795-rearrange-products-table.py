import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    result = pd.melt(
        products, 
        id_vars=['product_id'], 
        value_vars=['store1', 'store2', 'store3'], #columns to put together into one
        var_name='store', #the name of the new column
        value_name='price'#name of the value column
    )
    result = result.dropna(subset=['price'])
    
    return result
    