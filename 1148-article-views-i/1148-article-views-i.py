import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id']==views['viewer_id']]
    df = df[['author_id']].drop_duplicates()
    result = df.sort_values(by='author_id').rename(columns = {'author_id':'id'})
    return result





