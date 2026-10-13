# CareFlow - KPI Definitions

This document defines the KPIs for the CareFlow Clinical Pathway Process Mining dashboard planning phase as per Week 1 guide.

## 1. Total Events
- **Definition:** Count of valid event records; shows event-log size.
- **Calculation:** Count of rows with valid event data.
- **Required Fields:** Event ID / record
- **Validation Status:** Preliminary - Candidate events 2,222 (Not yet final validated count)

## 2. Total Cases
- **Definition:** Distinct validated case IDs; represents process instances.
- **Calculation:** Count distinct Case ID values.
- **Required Fields:** Case ID
- **Validation Status:** Preliminary - Candidate IDs 328 (ID semantics must be confirmed with data owner)

## 3. Unique Activities
- **Definition:** Count of distinct activity names in the log.
- **Calculation:** Count distinct normalized Activity names.
- **Required Fields:** Activity
- **Validation Status:** Preliminary - Activity names 36 (Check normalization and validity)

## 4. Unique Transitions
- **Definition:** Distinct consecutive activity pairs (e.g., Registration -> Waiting Room).
- **Calculation:** For each case, sort by timestamp, create pairs of Activity_n -> Activity_n+1, count distinct pairs.
- **Required Fields:** Case ID, Activity, Timestamp
- **Validation Status:** To be validated after activity normalization

## 5. Missing Timestamps
- **Definition:** Records missing required timestamps.
- **Calculation:** Count where Timestamp is null/invalid.
- **Required Fields:** Timestamp, End Timestamp (optional)
- **Validation Status:** Preliminary - Missing end timestamps 577 (May be legitimate if end times are not required)

## 6. Missing Activities
- **Definition:** Records without an activity name.
- **Calculation:** Count where Activity is null/empty.
- **Required Fields:** Activity
- **Validation Status:** To be checked during validation

## 7. Average Events per Case
- **Definition:** Average number of events recorded per case.
- **Calculation:** Valid event count / Distinct validated cases
- **Required Fields:** Case ID
- **Validation Status:** Exploratory

## 8. Median Elapsed Time
- **Definition:** Median time between consecutive event timestamps within a case.
- **Calculation:** Sort events within each validated case, calculate differences between consecutive timestamps, and take the median.
- **Required Fields:** Case ID, Timestamp
- **Validation Status:** Exploratory - Differences between event start times do not automatically equal actual waiting time.

## 9. Most Frequent Activity
- **Definition:** Activity with the highest event count.
- **Calculation:** Group by Activity, count, take max.
- **Required Fields:** Activity
- **Validation Status:** To be confirmed after normalization

## 10. Most Frequent Transition
- **Definition:** Consecutive activity pair with the highest count.
- **Calculation:** Count of most common Activity_n -> Activity_n+1 pair.
- **Required Fields:** Case ID, Activity, Timestamp
- **Validation Status:** To be confirmed

## Important Notes (from PDF Page 4 & 7)
- These figures are exploratory, not final validated KPIs.
- Missing end timestamps do not automatically mean an event is unusable.
- Case identification must be confirmed - do not assume every ID is a confirmed patient case.
- Time gaps should not be treated as confirmed waiting time without validation.
- Privacy: Hospital data must be handled according to authorization.
