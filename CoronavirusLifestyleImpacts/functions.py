import pandas as pd
import us
from pytrends.request import TrendReq

def get_data(state, keywords):
    """
    Gathers coronavirus data for a given state from the Bing Coronavirus
    data source as well as Google Trends data from the last year for
    the given keywords.
    Inputs:
        - state: Full name of state for which to gather the data
        - keywords: List of keywords to gather Google Trends data for
    Outputs:
        - covid_data: A dataframe with coronavirus counts of confirmed cases,
        deaths, and recoveries for the given state
        - trend_data: A dataframe with Google Trends data for the given
        keywords and state over the past year, aggregated weekly
    """
    state_abbr = us.states.lookup(state).abbr
    url = "https://raw.githubusercontent.com/microsoft/Bing-COVID-19-Data/master/data/Bing-COVID19-Data.csv"
    state_data = pd.read_csv(url)
    covid_data = state_data[(state_data.AdminRegion1 == state) &
                            (state_data.AdminRegion2.isnull())]
    user_timeframe = "2019-05-11 2020-05-11"
    area_code = "en-US-" + state_abbr
    pytrend = TrendReq(hl=area_code, tz=480)
    pytrend.build_payload(kw_list=keywords, timeframe=user_timeframe)
    trend_data = pytrend.interest_over_time()
    return(covid_data, trend_data)

get_data("Washington", ["Bars near me", "Home workouts"])
