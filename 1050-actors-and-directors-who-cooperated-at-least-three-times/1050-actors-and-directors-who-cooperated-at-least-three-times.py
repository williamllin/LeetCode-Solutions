import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df_count = actor_director.groupby(['actor_id','director_id']).size().reset_index(name='co-op_times')
    df_res = df_count[df_count['co-op_times']>=3]
    
    return df_res[['actor_id','director_id']]