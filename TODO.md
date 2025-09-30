# TODO

- [ ] Finalise README

## On Hold



## Later

- [ ] Create generic validation function which tests values in set for metadata with field values
- [ ] Add expected type schema to apply for test_validate
- [ ] Add validation for comment fields?
    - write a regex to filter out unwanted characters (or look only for wanted characters)

## Queries

- [x] Check what options were available for "state" after cycling erg
    - *1: "Awake, quiet", 2: "Awake, active/excited" (from FileMaker/Alex - 11/9)*
- [x] For Y8, cycle erg was monitored at 1.5, 3.5 and 5.5 minutes; for Y14 and Y17, it was every minute.
    - Do post-exercise variables harmonise in that case? Was the total duration same or different?
    - Confirm that post-exercise increments were consistently 1 minute
    - *Y8 should NOT be harmonised with Y14 and Y17. They had different protocols, and the Y8 data wasn't well collected (Alex 11/9)*
- [x] How to  deal with unusual values for CYC[1-3]?
    - Recode 400W to None or -99 (Missing)?
    - What about values like 26W? (should likely be 25W - 26 is too specific)
    - *Leave data as is - too many specific instances to parse; leave it to researchers (Alex 23/9)*
- [x] Four cases for `G222_WKT` between 15:00 and 19:00 (for waking time!)
    - *Corrected as of data from FileMaker (30/9)*
- [x] Values for BPSL like 00:00:21 -> should this instead be 21:00:00?
    - *Corrected as of data from FileMaker (30/9)*
- [x] Instances where SLPT < BPSL and WKBP < WKT
    - *Discrepancies exist in Filemaker. Too time-intensive to try and correct these. Just leave as is and let researchers identify and deal with them (30/9)*

## Done

### Project-specific

- [x] Read through all relevant questionnaire/coding versions and identify related variables
- [x] Identify all variables in the value labels spreadsheet, and mark them as in-progress
- [x] Add relevant variables to the `config/variables.py` dictionary
- [x] Explore each variable (either individually, or in small groups of 3-5)
- [x] Compare the coding versions, and check if variables with different names should be harmonised
- [x] Combine groups of validations into a single fn
- [x] Update Value Labels (add CYC) variables
- [x] Rename BP45 to BP12 (baseline state)
- [x] Rename the following to avoid cross-over from previous harmonisation
    - `G217_BP64`, `G214_BP64`, `G217_BP65`, `G214_BP65`, `G217_BP66`, `G214_BP66`
- [x] Drop avgs for BP and HR
- [x] Explore sleep BP variables
    - [x] BPS, BPD, SHR
    - [x] BPSL, SLPT, SL_COM, WKT, WKBP, SPRAT
- [x] Convert SLPT from AM to PM -> add 12 hours
- [x] Write validations to check SLPT > BPSL (some cases where this is not true)
- [x] Write validations to check WKBP >= WKT
- [x] Check out XCAR, XCER_COM (change to XCAR_COM), TECH, PWC170, INST
- [x] Briefly investigate XCAR
    - If 1, should be no nulls for BP (right?) -> but nulls for some values of BP6[4-6]
    - If 0, should be no values (right?) -> but values for *some* BP values (started and quit the test?)
- [x] Add field values for BP state metadata (ie. Awake, quiet...)
- [x] Clean sleep comment field (and look for other sleep comment variables missed)
- [x] Incorporate "check variables"
- [x] Incorporate BPTIME CSV
- [x] Create changelog (CSV/XLSX) file to outline all variables that have been changed, renamed, and/or deleted
- [x] Fill out tracking log for each file

### Higher Level

- [x] Create a main script which makes new interim data and processes it
- [x] Turn `validate.py` into a legitimate test with pytest - can run tests to ensure changes are correct
    - [x] Write tests from the beginning for validations and testing harmonisation functions
    - [x] Use as part of the data exploration phase
- [x] Write tests to check transformation from raw to interim datasets
- [x] Write tests to check transformation from interim to processed datasets
