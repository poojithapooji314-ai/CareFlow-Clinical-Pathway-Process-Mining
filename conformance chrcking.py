ideal = ["Admission","Diagnosis","Lab Test","Treatment Planning","Therapy","Discharge"]
import pandas as pd
df = pd.read_csv('clinical_event_log.csv')
for case, group in df.groupby('CaseID'):
    actual = list(group.sort_values('Timestamp')['Activity'])
    status = "Conforms" if actual == ideal else "Deviates"
    print(f"{case}: {status}")
