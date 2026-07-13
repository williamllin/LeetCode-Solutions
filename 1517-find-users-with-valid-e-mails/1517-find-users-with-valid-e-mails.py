import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$'
    condition = users['mail'].str.match(pattern, na=False)
    return users[condition]
    
    #or
    #pattern = r'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$'
    #con1 = users['mail'].str.match(pattern, na=False)
    #df=users[con1]
    #result = df[['user_id','name','mail']]
    #return result
    