import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:

    df = views[views['author_id'] == views['viewer_id']]#condition
    df = df[['author_id']].drop_duplicates()#drop duplicates
    
    #sort(pick column at same time), and rename
    result = df.sort_values(by='author_id').rename(columns={'author_id':'id'})
    return result








