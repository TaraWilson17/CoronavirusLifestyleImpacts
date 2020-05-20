from datetime import datetime, timedelta
import pandas as pd
import us
from pytrends.request import TrendReq

class DataGenerator:
    def __init__(self, args):
        self.args = args
        self.covid_data = None
        self.trend_data = None

    def run(self):
        print("Generating data...")
        self.covid_data, self.trend_data = self.get_data("Washington", ["Bars near me", "Home workouts"])

    @staticmethod
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
        domain = "https://raw.githubusercontent.com/microsoft"
        covid_project = "/Bing-COVID-19-Data/master/data/Bing-COVID19-Data.csv"
        url = domain + covid_project
        state_data = pd.read_csv(url)
        covid_data = state_data[(state_data.AdminRegion1 == state) &
                                (state_data.AdminRegion2.isnull())]
        today = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        one_year_ago = (datetime.now() - timedelta(days=366)).strftime("%Y-%m-%d")
        user_timeframe = one_year_ago + " " + today
        area_code = "en-US-" + state_abbr
        pytrend = TrendReq(hl=area_code, tz=480)
        pytrend.build_payload(kw_list=keywords, timeframe=user_timeframe)
        trend_data = pytrend.interest_over_time()
        return(covid_data, trend_data)

    def fetch_data_1(self, args):
        """
        Used to fetch from data source 1
        """
        #self.build_request_1(args)
        return "My fetched data"

    def fetch_data_2(self, args):
        """
        Used to fetch from data source 2
        """
        #self.build_request_2(args)
        pass

    # Helpers
    def build_request_1(self, args):
        pass

    def build_request_2(self, args):
        pass
