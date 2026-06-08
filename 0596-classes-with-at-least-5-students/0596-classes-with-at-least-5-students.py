import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.drop_duplicates() #prevent a student choose same class more than once
    class_count = df.groupby('class', as_index = False)['student'].count() #count students in each class
    result = class_count[class_count['student']>=5]
    return result[['class']]
    