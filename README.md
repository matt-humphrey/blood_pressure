---
author: Matt Humphrey
date_started: 9/9/2025
date_completed:
type: harmonisation
status: in-progress
---

# Harmonising Blood Pressure Variables

The purpose of this project was to harmonise the XX blood pressure variables, which existed across
the XX physical assessment datasets.

## Key Changes

1. **Issue**

Description

**Outcome**:

Reference: `harmonise.py: XX`

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
