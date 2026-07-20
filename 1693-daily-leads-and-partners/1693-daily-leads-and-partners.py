import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    df_res = daily_sales.groupby(['date_id','make_name']).agg({#because two nunique, so use agg
        'lead_id':'nunique',
        'partner_id':'nunique'
    }).reset_index()

    df_res = df_res.rename(columns={'lead_id':'unique_leads','partner_id':'unique_partners'})
    return df_res


    #result = daily_sales.groupby(['date_id', 'make_name']).agg(
    #    unique_leads=('lead_id', 'nunique'),   
    #    unique_partners=('partner_id', 'nunique')
    #).reset_index()
    
    #return result
