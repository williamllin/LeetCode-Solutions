import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    '''
    employees['total_time'] = employees['out_time'] - employees['in_time']
    #group by "event_day", "emp_id", and sum up "total_time"
    #keep as columns not index
    result = employees.groupby(['event_day', 'emp_id'], as_index=False)['total_time'].sum()
    
    result.rename(columns={'event_day': 'day'}, inplace=True)
    return result
    '''

    employees['total_time'] = employees['out_time'] - employees['in_time'] #new column

    #group by event_day and emp_id. Sum up total time
    result = employees.groupby(['event_day','emp_id'], as_index=False)['total_time'].sum()
    result.rename(columns={'event_day':'day'}, inplace=True)
    return result


