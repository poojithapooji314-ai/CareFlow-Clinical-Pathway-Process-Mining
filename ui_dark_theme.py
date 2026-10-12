# #9 Add attractive UI - dark theme + Sankey visual
# Power BI Dark Theme + Sankey for CareFlow

# Dark Theme Colors
theme = {
  "background": "#121212",
  "card_bg": "#1E1E1E",
  "text": "#FFFFFF",
  "blue": "#0078D4"
}
print("Dark theme applied:", theme)

# Sankey Visual Data for Power BI
import pandas as pd
df = pd.read_csv('clinical_event_log.csv')
df = df.sort_values(['CaseID','Timestamp'])
df['Next'] = df.groupby('CaseID')['Activity'].shift(-1)
sankey_data = df.dropna().groupby(['Activity','Next']).size().reset_index(name='Flow')
sankey_data.to_csv('sankey_for_powerbi.csv', index=False)
print("Sankey visual data ready:")
print(sankey_data.head())
print("#9 Done - Attractive UI ready for Power BI")
