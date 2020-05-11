# Coronavirus Lifestyle Impacts Functional Specification

## Background

The COVID-19 Pandemic has led many unanticipated lifestyle changes, human behaviors, and product trends. What better way to tap in to some of these interesting pandemic-influenced lifestyle impacts than through our world's search history? This tool allows a user to choose a trend of their choosing (big cats, baking, home fitness equipment sales) and see how this Google search keyword has coincided with the COVID-19 pandemic. 

## User Profile

Users of this tool are anyone who is interested about the impacts of coronavirus on various parts of our lives. No matter how big or small, comedic or serious. Users could be looking for fun, for business reasons, economic applications, or academic reasearch. This tool is for anyone who would benefit from a quick, easy, automatically generated visualization of google trends data relative to the onset of coronavirus. 

**Additional examples of users:** 
* An academic researcher or student who wanted to include some coronvirus graphics in a presentation
* A marketing brand manager looking at topical trends in their industry
* A personal investor checking a few hypothesis about product trends to influence a next buy

## Data Sources

* [COVID-19 Data](https://ourworldindata.org/coronavirus)
* [Google Trends Data](https://trends.google.com/trends/?geo=US)

## Use Cases

**Use Case 1:** User wants to understand a change in lifestyle trends relative to the onset of the COVID-19 pandemic.

> Expected interactions:
* User: Inputs keyword of google trend of interest
* User: Specifies what type of COVID data is desired (i.e. infections, deaths, recovered cases)
* Tool: Joins worldwide google trend data with worldwide COVID data.
* Tool: Data visualization generated for user(s)

**Use Case 2:** User wants to compare multiple changes in lifestyle trends relative to the onset of the COVID-19 pandemic.

> Expected interactions:
* User: Inputs keywords (up to 5 as a list) of google trends of interest
* User: Specifies what type of COVID data is desired (i.e. infections, deaths, recovered cases)
* Tool: Joins worldwide google trend data with worldwide COVID data
* Tool: Data visualization(s) generated for user

**Use Case 3:** User wants to understand a change in lifestyle trends relative to the onset of the COVID-19 pandemic in their region.

> Expected interactions:
* User: Inputs keywords (up to 5 as a list) of google trends of interest
* User: Specifies what type of COVID data is desired (i.e. infections, deaths, recovered cases)
* User: Specifies what region (country) they would like COVID data for
* User: Specifies what region (country) they would like google tren data for
* Tool: Joins worldwide google trend data with worldwide COVID data
* Tool: Data visualization generated for user(s)


