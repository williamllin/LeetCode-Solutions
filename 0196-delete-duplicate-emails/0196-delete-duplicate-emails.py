import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    #inplace because question says modify in place
    #sort first, and keep the first id with same email(ex:id 1 and 3 is same guy)
    person.sort_values(by='id',ascending=True,inplace=True)
    person.drop_duplicates(subset = ['email'], keep='first', inplace=True)
