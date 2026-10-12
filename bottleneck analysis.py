import pandas as pd
df = pd.read_csv('clinical_event_log.csv')
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df = df.sort_values(['CaseID','Timestamp'])
df['Duration_hours'] = df.groupby('CaseID')['Timestamp'].diff().dt.total_seconds()/3600
result = df.groupby('Activity')['Duration_hours'].mean()
print(result)
print(f"Bottleneck stage: {result.idxmax()} with {result.max()} hours delay")
