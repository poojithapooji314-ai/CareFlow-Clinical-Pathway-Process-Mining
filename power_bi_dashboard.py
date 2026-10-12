import pandas as pd
import matplotlib.pyplot as plt

# Load event log
df = pd.read_csv('clinical_event_log.csv')
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# --- KPI CARDS CALCULATION (for Power BI) ---
total_cases = df['CaseID'].nunique()
total_events = len(df)
avg_events_per_case = total_events / total_cases

# Calculate Length of Stay per case
df_sorted = df.sort_values(['CaseID', 'Timestamp'])
los = df_sorted.groupby('CaseID')['Timestamp'].agg(['min','max'])
los['LOS_days'] = (los['max'] - los['min']).dt.days
avg_los = los['LOS_days'].mean()

print(f"KPI 1 - Total Cases: {total_cases}")
print(f"KPI 2 - Total Events: {total_events}")
print(f"KPI 3 - Avg Events/Case: {avg_events_per_case:.1f}")
print(f"KPI 4 - Avg Length of Stay: {avg_los:.1f} days")

# --- PROCESS MAP DATA (for Sankey in Power BI) ---
df_sorted['Next_Activity'] = df_sorted.groupby('CaseID')['Activity'].shift(-1)
process_map = df_sorted.dropna().groupby(['Activity','Next_Activity']).size().reset_index(name='Count')
process_map.to_csv('process_map_for_powerbi.csv', index=False)
print("\nProcess Map saved to process_map_for_powerbi.csv")
print(process_map)

# Save KPI for Power BI
kpi_df = pd.DataFrame([{
    'Total_Cases': total_cases,
    'Total_Events': total_events,
    'Avg_LOS': avg_los
}])
kpi_df.to_csv('kpi_cards.csv', index=False)
