import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_sal = (accounts['income']<20000).sum()#sum() will sum up all True(1) in condition
    avg_sal = ((accounts['income']>=20000) & (accounts['income']<=50000)).sum()
    hig_sal = (accounts['income']>50000).sum()

    result = pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [low_sal, avg_sal, hig_sal]
    })
    return result