import pandas as pd

class DataProcessor:
    def __init__(self, args, data_frames = []):
        self.args = args
        self.input_data_frames = data_frames
        self.clean_data_frame = None
        self.agg_data_frame = None

    def run(self):
        print("Processing data...")
        self.clean_data(self.input_data_frames)
        self.aggregate_data()

    def clean_data(self, data_frames = []):
        covid = data_frames[0]
        trend = data_frames[1]

        covid = covid.drop(columns=['ID', 'Latitude', 'Longitude', 'ISO2', 'ISO3', 'AdminRegion2'])
        covid = covid.rename(columns={'Updated': 'Date', 'Country_Region': 'Country', 'AdminRegion1': 'State'})
        covid['Date'] = pd.to_datetime(covid['Date'])
        covid = covid.reset_index(drop=True)
        covid = covid.set_index(['Date'], drop=True)
    
        trend = trend.drop(columns='isPartial')

        self.clean_data_frame = [covid, trend]
        pass

    def aggregate_data(self, data_1 = None, data_2 = None, schema = None):
        pass

    # More data processing
