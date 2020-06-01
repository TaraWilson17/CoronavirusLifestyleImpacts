"""
This script tests the DataProcessor class to ensure it is working
as expected. The DataProcessor class handles the cleaning
and organizing of the Coronavirus and PyTrends data for the
CoronavirusLifestyleImpacts package. This is then handed off to
another module for data visualization.
"""

from context import coronavirus_lifestyle_impacts
import unittest
from coronavirus_lifestyle_impacts.data_generator import DataGenerator
from coronavirus_lifestyle_impacts.data_processor import DataProcessor

class UnitTests(unittest.TestCase):
    """
    This class uses the Python unittest package to run
    a series of tests validating the DataProcessor class.
    """

    def setUp(self):
        self.state = "Washington"
        self.keywords = ["Bars near me", "Home workouts"]
        self.data_generator = DataGenerator(self.state, self.keywords)
        self.data_generator.get_data()
        df = [self.data_generator.covid_data, self.data_generator.trend_data]
        self.data_processor = DataProcessor(self.data_generator.keywords, df)
        self.data_processor.run()

    def test_input_data_is_not_empty(self):
        """
        Asserts that the initial input dataframe recieved from the data 
        generator is not empty.
        """
        self.assertTrue(self.data_processor.input_data_frames)

    def test_clean_data_is_not_empty(self):
        """
        Asserts that the cleaned data assigned from the clean_data method
        is not an empty array.
        """
        self.assertTrue(self.data_processor.clean_data_frame)

    def test_agg_data_is_not_empty(self):
        """
        Asserts that the joined aggregated data assigned from the 
        clean_data method is not an empty array.
        """
        self.assertFalse(self.data_processor.agg_data_frame.empty)

    def test_agg_data_has_expected_columns(self):
        """
        Asserts that the PyTrends dataframe contains a column for each
        keyword as well as a column for `isPartial` which denotes if the
        data for a given week is completed or not.
        """
        expected_columns = self.keywords + ["Date", "Confirmed", 
            "ConfirmedChange", "Deaths", "DeathsChange", "Recovered",
            "RecoveredChange", "Country", "State"]
        self.assertEqual(set(list(self.data_processor.agg_data_frame.columns)),\
            set(expected_columns))

    def test_no_missing_data(self):
        """
        Asserts that the data in the Coronavirus dataframe has been filtered
        to only include data from the specified state.
        """
        self.assertFalse(self.data_processor.agg_data_frame.isnull().values.any())

    def test_covid_data_is_for_correct_state(self):
        """
        Asserts that the data in the Coronavirus dataframe has been filtered
        to only include data from the specified state.
        """
        self.assertEqual(self.state, self.data_processor.agg_data_frame['State'].values.all())

if __name__ == '__main__':
    unittest.main()
