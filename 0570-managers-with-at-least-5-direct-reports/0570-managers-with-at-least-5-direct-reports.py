import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    
    
    df = employee.merge(
        employee,
        left_on = 'id',#id_mgr
        right_on = 'managerId',#magId_emp
        suffixes=('_mgr','_emp') #employees' id(as manager table) = mananger id(employees' manager)
    )

    group = df.groupby('id_mgr').size().reset_index(name='report_count') #count the id_mgr
    valid_managers = group[group['report_count']>=5]
    result = employee[employee['id'].isin(valid_managers['id_mgr'])][['name']]
    return result

'''
table after join:
id_mgr  name_mgr   dep_mgr   magId_mgr  |   id_emp  name_emp ... magId_emp
101     John       a         nan        |   102     Dan          101
101     John       a         nan        |   103     James        101  
101     John       a         nan        |   104     Amy          101  
101     John       a         nan        |   105     Anne         101  
101     John       a         nan        |   106     Ron          101  
'''