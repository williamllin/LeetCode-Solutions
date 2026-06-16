import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    merge_df = employee.merge(
        employee,
        left_on = 'id',
        right_on = 'managerId',
        suffixes=('_mgr','_emp')
    )#101 links to all 'managerId 101'

    group = merge_df.groupby('id_mgr').size().reset_index(name='report_count') #count the number of mrg_id
    valid_managers = group[group['report_count']>=5]
    result = employee[employee['id'].isin(valid_managers['id_mgr'])][['name']]

    return result