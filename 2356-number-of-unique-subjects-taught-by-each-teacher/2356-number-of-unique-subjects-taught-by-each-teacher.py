import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    result = teacher.groupby('teacher_id', as_index=False)['subject_id'].nunique()
    #teacher 1 teaches sub 2 twice, but we count as 1 so use nunique()
    result.rename(columns={'subject_id':'cnt'}, inplace=True)
    return result