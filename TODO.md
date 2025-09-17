# TODO

- [ ] Explore sleep BP variables
    - BPS, BPD, SHR
    - BPSL, BPRC, SLPT, SL_COM, WKT, WKBP

- [ ] Drop avgs for BP and HR

- [/] Check out XCAR, XCER_COM (change to XCAR_COM), TECH, PWC170, INST

- [ ] Incorporate BPTIME CSV (for G0G1)

- [ ] Continue exploring each variable (either individually, or in small groups of 3-5)
- [ ] Compare the coding versions, and check if variables with different names should be harmonised

## On Hold

- How to validate (and deal with) unusual values for CYC[1-3]
    - Recode 400 to None? Leave others the same
- G217_INST -> just drop? no real value
- Briefly investigate XCAR
    - If 1, should be no nulls for BP (right?) -> but nulls for some values of BP6[4-6]
    - If 0, should be no values (right?) -> but values for *some* BP values (started and quit the test?)
- BP avg values incorrect for G126 and G222
    - for G222, it seems like the 2 and 4 min values have been averaged
    - for G126_BPS, it's just chaos and makes no sense

## Later

- [ ] Create a main script which makes new interim data, processes it, and then runs all validations/tests, and fails if any errors occur
- [ ] Refine and formalise tests between raw to interim, and interim to processed
- [ ] Create generic validation function which tests values in set for metadata with field values
- [ ] Add expected type schema to apply for test_validate
- [ ] Turn `validate.py` into a legitimate test with pytest - can run tests to ensure changes are correct
    - [ ] Write tests from the beginning for validations and testing harmonisation functions
    - [ ] Use as part of the data exploration phase

## Queries

- [ ] Explore the # of participants whose BP/HR increased across rest periods post-cycling

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
- [x] Combine groups of validations into a single fn
- [x] Update Value Labels (add CYC) variables
- [x] Rename BP45 to BP12 (baseline state)
- [x] Rename the following to avoid cross-over from previous harmonisation
    - `G217_BP64`, `G214_BP64`, `G217_BP65`, `G214_BP65`, `G217_BP66`, `G214_BP66`
