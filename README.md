# Coronavirus Lifestyle Impacts Project 

[![Build Status](https://travis-ci.org/TaraWilson17/CoronavirusLifestyleImpacts.svg?branch=master)](https://travis-ci.org/TaraWilson17/CoronavirusLifestyleImpacts)

[![Coverage Status](https://coveralls.io/repos/github/TaraWilson17/CoronavirusLifestyleImpacts/badge.svg?branch=master)](https://coveralls.io/github/TaraWilson17/CoronavirusLifestyleImpacts?branch=master)

This is the final project for Data 515 at the University of Washington, Spring 2020.  

This project is designed to help users view how lifestyles have been influenced by the 2019 novel coronavirus using Google Trends data. The tool allows people to input geographical locations and keywords to have visualizations and summary statistics generated to summarize the impact.    

## Table of contents  

## Data sources

There are two datasets used in this project:  
1. [Bing COVID-19 Tracker](www.bing.com/covid)
    * Data is available in a csv format in [this Github repository](https://github.com/microsoft/Bing-COVID-19-Data)  
    * This data is updated daily (around 3AM PST), with a 24-hour delay
    * Data contains the [following columns](https://github.com/microsoft/Bing-COVID-19-Data/tree/master/data):

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

2. [PyTrends Data](https://pypi.org/project/pytrends/)
    * Accessed via PyTrends python package which is an "Unofficial API for Google Trends"
    * Data is aggregated at a weekly level
    * Google Trends data is reported between 0 to 100, based on the relitive proportion of a keyword to all included in the search over time
    * Interest over time query contains the following columns:  

        | Column header | Description |
        | --- | --- |
        | date | First day of the week for which the data represents |
        | Trend keyword(s) | Trend keyword(s) you pass into the query, e.g. "Dogs for adoption" |
        | isPartial | Boolean indicator of whether of not the full week of data for that trend is available yet |

## Team Members  
* David Wei  
* Lauren Heintz  
* Ratna Chembrolu   
* Tara Wilson  
* Zack Garcia  

## References
- [How to setup Travis CI](https://github.com/dacb/codebase)
