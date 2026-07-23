import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    
    
    df = employee.merge(
        employee,
        left_on = 'id',
        right_on = 'managerId',
        suffixes=('_mgr','_emp')
    )

    group = df.groupby('id_mgr').size().reset_index(name='report_count')
    valid_managers = group[group['report_count']>=5]
    result = employee[employee['id'].isin(valid_managers['id_mgr'])][['name']]
    return result