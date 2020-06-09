# Coronavirus Lifestyle Impacts

## Overview
This document describes the high-level architecture of the tool.

## Tenets
- Easy to install
- Easy to use
- Meaningful visualization and insights
- Parallel implementation
- Privacy of user inputs: the tool does not collect or store any user input data

## Goal
- Isolated components each with single responsibility
- Extensibility: each component should be easy to extend by feature request
- Easy to test by component

## Out of Scope
- Availability: This command line tool depends on an [unofficial API](https://pypi.org/project/pytrends/) for Google trends. The availability
  of the API and Google trends directly impact the functionality of this tool
- Long-running queries: Depending on the user input, some queries will take longer to return due to data volume. The tool will have a time-out
  limit set for each query. User will be offered an option to provide custom time-out.

## Component Specification

![](Project.PNG)

The Project contains the following components:
1. CmdParser
2. DataGenerator
3. DataProcessor
4. DataVisualizer

### 1. CmdParser
This is the interface between the end-user and our service. The CommandLineParser will take the user command, validates the inputs, and pass it
down to the downstream services. It is lightweight and should always return a response to the end user.
There are two public Python command line parsers to use: [ArgParser](https://docs.python.org/3/library/argparse.html) and [Click](https://click.palletsprojects.com/en/7.x/). Click is preferred but the decision has not been made yet.

For example:
- user input: `$: covid19-impacts --state "Washington" --keywords "masks, hand sanitizer"
- outputs: all user input data returned in a json string
```
{
  "state": "Washington",
  "keywords": ['masks', 'hand sanitizer']
}
```

###  2. DataGenerator
A DataGenerator is responsible of taking the input Json blob and providing datasets in Pandas DataFrame format.
The DataGenerator is designed to have two sub-components: a `query_builder.py` module and a `query_executor.py`.
- Input: Inputs to this module are state and keywords for which the user would like the google trends for.
- Output: Data specific to corona virus infections & fatalities by state and Search trends for a given keyword.  

* COVID data:  
  
    |Column header | Description |
    |---|---|
    |ID | Unique identifier |
    |Updated| Datetime in UTC |
    |Confirmed | Confirmed case count for the region |
    |ConfirmedChange| Change of confirmed case count from the previous day |
    |Deaths| Death case count for the region |
    |DeathsChange| Change of death count from the previous day |
    |Recovered| Recovered count for the region |
    |RecoveredChange| Change of recovered case counts from the previous day |
    |Latitude| Latitude of the centroid of the region |
    |Longitude| Longitude of the centroid of the region |
    |ISO2| 2 letter country code identifier |
    |ISO3| 3 letter country code identifier |
    |Country_Region| Country/region |
    |AdminRegion1| Region within Country_region |
    |AdminRegion2| Region within AdminRegion1 |  

* PyTrends Data:  

    | Column header | Description |
    | --- | --- |
    | date | First day of the week for which the data represents |
    | Trend keyword(s) | Trend keyword(s) you pass into the query, e.g. "Dogs for adoption" |
    | isPartial | Boolean indicator of whether of not the full week of data for that trend is available yet |  


### 3. DataProcessor:
A DataProcessor is responsible of taking the provided data frame, validating the results, and performing aggregation. The output
is a structured Pandas DataFrame which can be used by the DataVisualizer.
- Input: Dataframes produced by DataGenerator, keywords list.
- Output: Single dataframe containing all the data from both data sets joined on the date

* The Aggregated Data:  
 
    | Column header | Description |
    | --- | --- |
    | Date | First day of the week for which the data represents |
    | Confirmed | Number of COVID cases |
    | ConfirmedChange | Change in number of COVID cases |
    | Deaths | Number of COVID deaths |
    | DeathsChange | Change in number of COVID deaths |
    | Recovered | Number of COVID recoveries |
    | RecoveredChange | Change in number of COVID recoveries |
    | Country | Country chosen (default United States) |
    | State | State chosen |
        | Trend keyword(s) | Trend keyword(s) you pass into the query, e.g. "Dogs for adoption" |

### 4. DataVisualizer
A DataVisualizer is responsible of rendering the final graphs for end-user by taking the input data from DataProcessor.
- Input: Aggregated data from DataProcessor, keywords, state.
- Output: Graphs to end user.

## Test
For each component, we will have a validator to unit test its functionality. We will also have a simple end-to-end integration test. The
integration test will be part of the GitHub build process and shown as the build badge at the front page of the repo.

## Sample DataFlow and UseCase
1. User will input the state and the lifestyle trend they would like to observe the shifts. There is a max of 5 keywords that can be chosen for the trend tracking. 
2. User also gets to choose what specific state they want to look at.
3. Once they get the visualization they can, they can also download a CSV which has additional data and play around with the information on their own.

## Work items and Owners
- Refine use case and build test input [team]
- Design review with team [team]
- Implementation in parallel and unit test
  - CmdParser [David]
  - DataGenerator [Tara]
  - DataProcessor [Lauren]
  - DataVisualizer [Tara]
- CI/CD: End-to-end test and release pipeline [David]
- Presentation [Zack]
- PowerBi [Ratna]
- Pylint & Pep8 [Ratna]
