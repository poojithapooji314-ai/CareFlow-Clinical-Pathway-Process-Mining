# Power BI Data Model
Tables:
1. Cases Table: CaseID, Age, Gender, Diagnosis
2. Events Table: CaseID, Activity, Timestamp, Doctor, Department
Relationship: Cases[CaseID] -> Events[CaseID] (One to Many)

DAX Measures:
- Total Cases = COUNTROWS(Cases)
- Avg Length of Stay = AVERAGEX(Cases, Cases[Duration])
- Bottleneck Delay = MAX(Events[Duration_hours])
