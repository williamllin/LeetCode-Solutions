import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, left_on ='departmentId', right_on='id', suffixes=('_emp', '_dept'))

    df['max_salary'] = df.groupby('departmentId')['salary'].transform('max')

    result = df[df['salary'] == df['max_salary']]

    result = result[['name_dept', 'name_emp', 'salary']]
    result.columns = ['Department','Employee','Salary']
    return result
    