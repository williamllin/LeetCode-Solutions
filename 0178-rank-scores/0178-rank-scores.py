import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    
    #if empty, return empty
    if scores.empty:
        return pd.DataFrame(columns=['score','rank'])

    scores['rank'] = scores['score'].rank(method='dense',ascending=False)#dense:same score get same rank

    result = scores.sort_values(by='score',ascending=False)[['score','rank']]
    return result
