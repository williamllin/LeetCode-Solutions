import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    '''
    if N<=0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    

    unique_salaries = employee['salary'].drop_duplicates()
    sorted_salaries = unique_salaries.sort_values(ascending=False)
    if N > len(sorted_salaries):
        ans = None
    else:
        ans = sorted_salaries.iloc[N-1]

    return pd.DataFrame({f'getNthHighestSalary({N})': [ans]})
    '''
    if N<=0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    unique_salary = employee['salary'].drop_duplicates()
    sorted_salary = unique_salary.sort_values(ascending=False)

    if N>len(sorted_salary):
        ans = None
    else:
        ans = sorted_salary.iloc[N-1]
    return pd.DataFrame({f'getNthHighestSalary({N})': [ans]})