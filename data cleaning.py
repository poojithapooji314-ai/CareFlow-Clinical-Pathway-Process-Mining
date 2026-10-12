import pandas as pd

# Load data
df = pd.read_csv('clinical_event_log.csv')

# Remove duplicates
print(f"Before: {len(df)} rows")
df_cleaned = df.drop_duplicates()
print(f"After: {len(df_cleaned)} rows")

# Remove missing values
df_cleaned = df_cleaned.dropna()

# Save cleaned file
df_cleaned.to_csv('clinical_event_log_cleaned.csv', index=False)
print("Cleaned file saved!")
