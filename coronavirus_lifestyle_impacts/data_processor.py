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
        covid = self.clean_data_frame[0]
        trend = self.clean_data_frame[1]
        agg = covid.join(trend, how='outer')
        agg.reset_index(inplace = True)
        agg= agg.rename(columns={'index': 'Date'})
        #agg[agg[9]==""] = np.NaN

        # Forward Fill in non-existent values for google trends
        agg['Bars near me'].fillna(method='ffill', inplace=True)
        agg['Home workouts'].fillna(method='ffill', inplace=True)

        # Forward Fill missing covid data with values
        agg.iloc[0, agg.columns.get_loc('Confirmed')] = 0
        agg['Confirmed'].fillna(method='ffill', inplace=True)

        agg.iloc[0, agg.columns.get_loc('ConfirmedChange')] = 0
        agg['ConfirmedChange'].fillna(method='ffill', inplace=True)

        agg.iloc[0, agg.columns.get_loc('Deaths')] = 0
        agg['Deaths'].fillna(method='ffill', inplace=True)

        agg.iloc[0, agg.columns.get_loc('DeathsChange')] = 0
        agg['DeathsChange'].fillna(method='ffill', inplace=True)

        agg.iloc[0, agg.columns.get_loc('Recovered')] = 0
        agg['Recovered'].fillna(method='ffill', inplace=True)

        agg.iloc[0, agg.columns.get_loc('RecoveredChange')] = 0
        agg['RecoveredChange'].fillna(method='ffill', inplace=True)
        
        # Backfill State and Country data
        agg['Country'].fillna(method='bfill', inplace=True)
        agg['State'].fillna(method='bfill', inplace=True)

        self.agg_data_frame = agg
        
        pass

    # More data processing
