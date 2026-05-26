import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:

    low_count = (accounts['income'] < 20000).sum() #sum() will sum up number of True (1)
    average_count = ((accounts['income'] >= 20000) & (accounts['income'] <= 50000)).sum()
    high_count = (accounts['income'] > 50000).sum()
    

    res = pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [low_count, average_count, high_count]
    })
    
    return res