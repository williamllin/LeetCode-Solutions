import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    lowrec = (products['low_fats']=='Y') & (products['recyclable']=='Y')
    result = products[lowrec][['product_id']]
    return result

