import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    

    unique_salaries = employee['salary'].drop_duplicates()
    sorted_salaries = unique_salaries.sort_values(ascending = False)

    #put this condition here, not at beginning, since after remove dups, len might <2 (ex:all id have same salary)
    if len(sorted_salaries)<2: 
        ans = None
    else:
        ans = sorted_salaries.iloc[1]

    return pd.DataFrame({f'SecondHighestSalary': [ans]})
    