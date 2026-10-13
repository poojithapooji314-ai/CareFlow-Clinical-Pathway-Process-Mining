# CareFlow - KPI Definitions

## KPI 1: Average Length of Stay (ALOS)
- Definition: Avg time from Registration to Discharge
- Formula: SUM(Discharge Time - Registration Time) / Total Cases
- Why important: Shows overall hospital efficiency
- Target: < 4 hours for general cases

## KPI 2: Activity Waiting Time
- Definition: Time patient waits before each activity starts
- Example: Time between Triage End and Consultation Start
- Formula: Activity Start Time - Previous Activity End Time
- Visualization: Bar chart

## KPI 3: Bottleneck Rate
- Definition: Activities where waiting time > 30 mins
- Formula: Count of cases with waiting > 30 mins / Total cases * 100
- Action: Highlight these activities in dashboard

## KPI 4: Department Utilization
- Definition: How busy each department is
- Formula: Total cases handled by department / Total time
- Example: Lab department had 120 cases on 12th Oct

## KPI 5: Process Compliance Rate
- Definition: How many cases followed ideal pathway: Registration -> Triage -> Consultation -> Lab -> Pharmacy -> Discharge
- Formula: Compliant Cases / Total Cases * 100
- Low compliance means process deviation

## KPI 6: Rework Rate
- Definition: Patient returning to same activity (e.g., Consultation again)
- Formula: Cases with repeated activity / Total cases
