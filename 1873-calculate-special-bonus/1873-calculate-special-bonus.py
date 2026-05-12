import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:

    condition1 = employees['name'].str[0] != 'M'
    condition2 = employees['employee_id'] % 2 != 0
    
    #create bonus: if satisfy con1,2. Otherwise 0
    employees['bonus'] = np.where(condition1 & condition2, employees['salary'], 0)
    
    #sort and choose columns
    return employees.sort_values(by='employee_id')[['employee_id', 'bonus']]

