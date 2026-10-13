# CareFlow - Dashboard Requirements
Team: CareFlow Team - Sprint 1 (Week 1)
Members: Poojitha (Team Lead), Amarnath, Md Saquib Ansari
Repo: CareFlow-Clinical-Pathway-Process-Mining-1b8d9ccc
Date: 13 Oct 2026

## 1. Project Objective
To analyze hospital event logs and build a dashboard that shows patient flow, delays in departments, and bottlenecks in clinical pathways.

## 2. Who will use the dashboard?
- Doctors: to see patient waiting time
- Admin staff: to manage department load
- Our project guide: to evaluate process mining results

## 3. Data Requirements
- Input: Event log CSV (CaseID, Activity, Timestamp, Department, Resource)
- Minimum 500 cases for Sprint 1 testing
- Data cleaning needed for missing timestamps

## 4. Functional Requirements
- FR1: Show total cases, active cases, completed cases
- FR2: Show average time per activity (Registration, Triage, Consultation, Lab, Pharmacy)
- FR3: Show bottleneck activities highlighted in red
- FR4: Filter by department and date range
- FR5: Export filtered data as CSV

## 5. Non-Functional Requirements
- Dashboard should load in <3 seconds
- Simple UI, no complex graphs for Week 1
- Works on laptop screen (no mobile needed for now)

## 6. Tools for Sprint 1
- GitHub for collaboration (Done - invites sent)
- Python (pandas, pm4py for later)
- PowerBI / Streamlit (will decide in Week 2)
- Docs folder for all planning

## 7. Team Work Division
- Poojitha: GitHub setup + Documentation
- Amarnath: Data collection and cleaning logic
- Saquib: KPI definitions and layout design
