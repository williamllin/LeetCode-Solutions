import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # | -> or
    is_big = (world['area']>=3000000) | (world['population']>=25000000)
    result = world[is_big][['name','population','area']]
    return result
