import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    





    df = employee.merge(department, left_on = 'departmentId', right_on = 'id', suffixes =('_emp','_dep'))
    df['max_salary'] = df.groupby('departmentId')['salary'].transform('max')

    result = df[df['salary'] == df['max_salary']]
    result = result[['name_emp','name_dep','salary']]
    result.columns = ['Department','Employee','Salary'] 
    return result







    