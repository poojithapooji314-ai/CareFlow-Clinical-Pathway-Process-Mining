import pandas as pd
df = pd.read_csv('clinical_event_log.csv')
variants = df.groupby('CaseID')['Activity'].apply(lambda x: ' -> '.join(x)).value_counts().head(5)
print("Top 5 pathway variations:")
print(variants)
