# CareFlow - Dashboard Layout (Week 1 Draft)

## Overall Idea
Single page dashboard, top to bottom flow. Keeping it simple for now.

### Section A - Top Header (Row 1)
- Left: Project Title - "CareFlow - Clinical Pathway Dashboard"
- Right: Filters - Date Picker, Department Dropdown (All, Lab, Pharmacy, Consultation)
- Small text: Last updated - auto

### Section B - KPI Cards (Row 2)
4 cards in one row:
1. Total Cases - e.g., 523
2. Avg Length of Stay - e.g., 3.2 hrs
3. Bottleneck Dept - e.g., Lab (45 mins avg wait)
4. Compliance Rate - e.g., 78%

### Section C - Middle Charts (Row 3)
- Left (60% width): Process Flow Map - boxes connected with arrows, bottleneck box in red
- Right (40% width): Bar Chart - Avg waiting time per activity

### Section D - Details Table (Row 4)
Table with columns: CaseID, Current Activity, Waiting Time, Status (Delayed/On Track)
- Search box for CaseID
- Top 10 delayed cases only for Week 1

### Section E - Footer
- Team Names
- Sprint 1 - Data Understanding

## Notes for Development
- No colors except red for bottleneck
- For Week 1 we will only draw this on paper and implement wireframe later
- Feedback from guide will be taken in Week 2

Hand-drawn sketch will be added in next commit as image.
