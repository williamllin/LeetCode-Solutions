# Write your MySQL query statement below
select patient_id, patient_name, conditions
from patients
where conditions like '% DIAB1%'
    or conditions like 'DIAB1%'


#where conditions like '%DIAB1%' (X), since it doesn't specify the position