import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    #if score table is empty, return empty table
    if scores.empty:
        return pd.DataFrame(columns=['score', 'rank'])
    
    #method='dense' -> if same score, get same rank
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)

    result = scores.sort_values(by='score',ascending = False)[['score','rank']]
    return result
    