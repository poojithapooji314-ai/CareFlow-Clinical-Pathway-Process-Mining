# Power BI DAX Measures for Dashboard #8

## Create these Measures in Power BI:

1. Total Cases = DISTINCTCOUNT(Events[CaseID])
2. Total Events = COUNTROWS(Events)
3. Avg LOS = AVERAGEX( SUMMARIZE(Cases, Cases[CaseID], "LOS", DATEDIFF(Cases[AdmissionDate], Cases[DischargeDate], DAY)), [LOS])
4. Bottleneck Delay = MAXX(Events, Events[Duration_hours])
5. Conformance % = DIVIDE(COUNTROWS(FILTER(Cases, Cases[IsConforming]=TRUE)), [Total Cases])

## Dashboard Layout:
- Page 1: KPI Cards (4 cards on top) + Process Map (Sankey visual from AppSource)
- Page 2: Variant Analysis (Bar chart Top 5 variants)
- Page 3: Bottleneck (Column chart - Avg Duration per Activity)

## Dark Theme Settings:
Background: #121212
Card Visual: #1E1E1E, Font White, Border #333
Sankey: Oncology Blue #0078D4 to #90CAF9
