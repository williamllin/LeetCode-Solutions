import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    

    #merge
    df = employee.merge(department, left_on='departmentId',right_on='id',suffixes=('_emp','_dep'))

    #get max salary
    df['max_salary'] = df.groupby('departmentId')['salary'].transform('max')

    #select salaries that are max 
    result = df[df['salary'] == df['max_salary']]

    #result
    result = result[['name_dep','name_emp','salary']]
    result.columns = ['Department','Employee','Salary']
    return result







    