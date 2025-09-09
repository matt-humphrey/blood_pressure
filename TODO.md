# TODO

- [ ] Continue exploring each variable (either individually, or in small groups of 3-5)
- [ ] Compare the coding versions, and check if variables with different names should be harmonised

- [ ] Rename the following to avoid cross-over from previous harmonisation
    - `G217_BP64`, `G214_BP64`, `G217_BP65`, `G214_BP65`, `G217_BP66`, `G214_BP66`

## Later

- [ ] Create a main script which makes new interim data, processes it, and then runs all validations/tests, and fails if any errors occur
- [ ] Refine and formalise tests between raw to interim, and interim to processed
- [ ] Create generic validation function which tests values in set for metadata with field values
- [ ] Add expected type schema to apply for test_validate
- [ ] Turn `validate.py` into a legitimate test with pytest - can run tests to ensure changes are correct
    - [ ] Write tests from the beginning for validations and testing harmonisation functions
    - [ ] Use as part of the data exploration phase

## On Hold

G227_BP10_1 was previously harmonised to G227_BP64, and so on to G227_BP27_1 -> G227_BP81

## Done

- [x] Read through all relevant questionnaire/coding versions and identify related variables
- [x] Identify all variables in the value labels spreadsheet, and mark them as in-progress
- [x] Add relevant variables to the `config/variables.py` dictionary
