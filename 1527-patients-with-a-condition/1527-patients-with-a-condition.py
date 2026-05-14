import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:

    pattern = r'^DIAB1|.* DIAB1' #starts with DIAB1 or a char+space then DIAB1
    con1 = patients['conditions'].str.contains(pattern, na=False)
    df = patients[con1]
    result = df[['patient_id','patient_name','conditions']]
    return result
