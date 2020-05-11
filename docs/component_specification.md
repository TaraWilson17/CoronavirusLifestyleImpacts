# Coronavirus Lifestyle Impacts

## Component Specification

![](Project.PNG)

The Project contains the following components:
    1. Extraction
    2. Aggregation/Manipulation
    3. Visualization
    
###  1. Extraction:
Input: Timeperiod and source data set links to be provided for the module.
Output: Data specific to corona virus infections, fatalities by state and Search and Twitter trends by state are extracted
What does this module do: This module extracts the necessary data from the two data sources.

### 2. Aggregation/Manipulation:
Input: Data extracted from the two data sources
Output: Aggregated across the dimensons of state or search terms 
What this modul does: This module combines the data from these two data sources into a single table and aggregates it into the format which is consumable for visualization.

### 3. Visualization
Input: Aggregated data from the prior module
Output: Graphs of the final data.
What this module does: This module provides a graph overlaying the corona virus data with the Lifestyle trend shifts.


### User Interactions
1. User will input the timeperiod and the lifestyle trend they would like to observe the shifts. These lifestyle trends are going to be pre-selected.
2. User also gets to choose if they want to look at a specific state or for the country (USA).
3. Once they get the vizualization they can, make changes to make the graphs interactive
