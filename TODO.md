# TODO


## On Hold

- [ ] Incorporate BPTIME CSV (for G0G1)
- [ ] How to validate (and deal with) unusual values for CYC[1-3]
    - Recode 400 to None? Leave others the same
    - Recode 400 to -99 "Missing"?
- [ ] Values for BPSL like 00:00:21 -> should this instead be 21:00:00?
- [ ] Instances where SLPT < BPSL and WKBP < WKT
- [ ] Four cases for `G222_WKT` between 15:00 and 19:00 (for waking time!)

## Later

- [/] Refine and formalise tests between raw to interim, and interim to processed
- [ ] Create generic validation function which tests values in set for metadata with field values
- [ ] Add expected type schema to apply for test_validate

## Queries

- [x] Check what options were available for "state" after cycling erg
    - *1: "Awake, quiet", 2: "Awake, active/excited" (from FileMaker/Alex - 11/9)*
- [x] For Y8, cycle erg was monitored at 1.5, 3.5 and 5.5 minutes; for Y14 and Y17, it was every minute.
    - Do post-exercise variables harmonise in that case? Was the total duration same or different?
    - Confirm that post-exercise increments were consistently 1 minute
    - *Y8 should NOT be harmonised with Y14 and Y17. They had different protocols, and the Y8 data wasn't well collected (Alex 11/9)*

## Done

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


- [x] Create a main script which makes new interim data and processes it
- [x] Turn `validate.py` into a legitimate test with pytest - can run tests to ensure changes are correct
    - [x] Write tests from the beginning for validations and testing harmonisation functions
    - [x] Use as part of the data exploration phase
