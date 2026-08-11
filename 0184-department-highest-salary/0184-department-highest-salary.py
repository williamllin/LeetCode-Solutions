import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    #merge, max_sal in department, select max_sal rows for result
    df = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('_emp','_dep'))
    df['max_salary'] = df.groupby('departmentId')['salary'].transform('max')
    result = df[df['salary'] == df['max_salary']]

    #select which columns to show and rename
    result = result[['name_dep','name_emp','salary']]
    result.columns = ['Department','Employee','Salary']
    return result
    

    '''
    import pandas as pd

    df = employee.merge(department, left_on='departmentId', right_on='id', suffixes=('_emp','_dep'))
    df['max_salary'] = df.groupby('departmentId')['salary'].transform('max')
    result = df[df['salary']==df['max_salary']]

    result = result[['name_dep','name_emp','salary']]
    result.columns = ['Department','Employee','Salary']
    return result
    '''




    