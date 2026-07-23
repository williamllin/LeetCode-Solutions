import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    
    base_df = students.merge(subjects, how='cross')#cross join students and subject
    exam_counts = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name='attended_exams')
    #number of subjects students attended

    result = base_df.merge(exam_counts, on=['student_id', 'subject_name'], how='left')
    result['attended_exams'] = result['attended_exams'].fillna(0).astype(int) #na to 0
    result = result.sort_values(by=['student_id', 'subject_name'])
    return result[['student_id', 'student_name', 'subject_name', 'attended_exams']]
