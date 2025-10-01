---
author: Matt Humphrey
date_started: 9/9/2025
date_completed: 30/9/2025
type: harmonisation
status: completed
---

# Harmonising Blood Pressure Variables

The purpose of this project was to harmonise the exercise and sleep blood pressure variables, which
existed across the following physical assessment datasets:

- G126_PAdata (sleep)
- G208_PA (exercise)
- G214_PA (exercise)
- G217_PA (exercise)
- G222_PA (sleep)

## Key Changes

### 1. Overlap in different exercise variable names

For the cycle ergometer exercise testing in year 8, the McMaster protocol was used. Data was
captured in three stages - at 1.5 mins, 3.5 mins, and 5.5 mins. The variables were named
`G208_BP12_2` to `G208_BP20_2`.

For the cycle ergometer testing in years 14 and 17, the same protocol was used, but the way data was
captured was different - for example, data was captured in 1 minute increments from 1 to 6 minutes.
These variables were named `G214_BP14`, `G214_BP17`, `G214_BP20`, `G214_BP64`, `G214_BP65`, and
`G214_BP66`, as well as `G214_BP45` used to capture the participants "state of rest" at the start.
(The base names were equivalent for G217.)

**Outcome**

Because the variables `BP64` to `BP66` were used for different data in other datasets, these needed
to be renamed, and so all of the variables for G214 and G214 were renamed from `BP12` to `BP18`, as
seen in `variables.py` and `changelog.csv`.

The variables`G208_BP12_2` to `G208_BP20_2`, were subsequently renamed to `G208_BP82` to `G208_BP90`
to avoid possible confusion.

*Reference*: `variables.py`

### 2. One extreme outlier discovered for `G214_BP41`

During data validation, a value of 1110 was discovered for `G214_BP41` (blood pressure).
There was no other historical record, and thus this was assumed to be an error in manual data entry.

**Outcome**

Recoded G214_BP41 from 1110 to None.

*Reference*: `harmonise.py: 45`

### 3. Differences in coding of `XCAR`

`G214_XCAR` and `G217_XCAR` were used to capture if the participant had completed the exercise test.

For G214, values of 0 were used in two instances where the participant started, but did not complete
the test. Values of 9 represented "Missing" where they did not do the test at all.

For G217, values of 0 were used where the participant did not do the test.

**Outcome**

Values of 0 were kept for G214, and values of 9 were converted to None.
Values of 0 were converted to None for G217.

*References*: `harmonise.py: 50, 60`

### 4. All times for `G126_SLPT` were captured as AM instead of PM

For `G126_SLPT` (time went to sleep), all values ranged between 7am and 12pm.

**Outcome**

All values were offset by 12 hours to convert them to PM time (ie. between 7pm and 12am).

*Reference*: `harmonise.py: 96`

### 5. Inconsistencies in `G222_BP_TIME`

The raw data for many of the values for G222_BP_TIME ended in 59 seconds (ie. 17:50:59). This data
must have been changed somehow, because data from FileMaker had no seconds value. Furthermore, a
number of values from FileMaker didn't match what was in core.

**Outcome**

Data was pulled out of FileMaker and cleaned before merging it back into core. However, there were
issues discovered even with the FileMaker data, where there were ~150 values for blood pressure
times in the morning (unusual for a sleep study). This was assumed to be valid for ~50 cases, where
there was no sleep study conducted (thus the participants likely came in for a regular study). In
instances where there *was* a sleep study conducted, these AM times were converted to PM.

*Reference*: `harmonise.py: 106`

### 6. Inconsistencies in `G222_SLPT`

There were a range of values for `G222_SLPT` between 10am and 12pm (for sleep time).

**Outcome**

These instances were converted from AM to PM.

*Reference*: `harmonise.py: 146`

### 7. Inconsistencies in `G126_BPSL`

There were 20 cases where the value for `G126_BPSL` was a number of seconds after midnight (ie.
00:00:21). These cases were investigated, and in each instance, the value had been incorrectly
exported (ie. 00:00:21 was actually 21:45:00).

**Outcome**

These variables were re-exported from FileMaker and merged back into core.

*Reference*: `harmonise.py: 174`

### 8. Inconsistencies in `G222_WKT`

There were 6 cases where the value for `G126_WKT` (time woken up) in core differed from the data in
FileMaker. The values from core seemed obviously wrong (waking up at 12am, or 5pm).

**Outcome**

These variables were re-exported from FileMaker and merged back into core.

*Reference*: `harmonise.py: 229`

## Project Structure

### data

Contains four sub-directories with the following datasets:

- Original: as they were at the beginning of the project
- Raw: as they were prior to harmonising (some datasets may have been changed by other data officers
while the project was underway)
- Interim: processed initially to rename and delete specified variables
- Processed: with all transformations completed to harmonise the data and metadata

### docs

Contains all relevant information related to the project (ie. coding guides, protocols, etc).

### notebooks

A collection of Marimo notebooks both for experimentation, and in some cases, used for running the
functions to create the interim and processed datasets.

### src/blood_pressure

This is the where all code related to the project is stored.
The key files to be aware of are:

- `config/metadata.py`: where the metadata for each unique variable is defined
- `config/variables.py`: the variables specified for alteration/exploration, renaming, and deleting
- `harmonise.py`: contains all the logic/functions to change the raw data and harmonise the variables
