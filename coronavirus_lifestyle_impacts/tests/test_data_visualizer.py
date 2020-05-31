"""
This script tests the DataVisualizer class to ensure it is working
as expected. The DataVisualizer class handles the downloading
and retrieving of the Coronavirus and PyTrends data for the
CoronavirusLifestyleImpacts package.
"""

from context import coronavirus_lifestyle_impacts
import unittest
import os.path
from coronavirus_lifestyle_impacts.data_generator import DataGenerator
from coronavirus_lifestyle_impacts.data_processor import DataProcessor

class UnitTests(unittest.TestCase):
    """
    This class uses the Python unittest package to run
    a series of tests validating the DataVisualizer class.
    """

    def setUp(self):
        self.state = "Washington"
        self.keywords = ["Bars near me", "Home workouts"]
        self.dg = DataGenerator(self.state, self.keywords)
        self.dg.get_data()
        self.data_processor = DataProcessor(self.dg.keywords, data_frames=[self.dg.covid_data, self.dg.trend_data])
        self.data_processor.run()
        
    def test_visualization_generated(self):
        filepath = "../" + self.state + "_coronavirus_trend_impacts_lines.png"
        print(filepath)
        self.assertTrue(os.path.isfile(filepath))

if __name__ == '__main__':
    unittest.main()
