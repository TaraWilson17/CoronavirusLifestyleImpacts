"""
This script tests the DataVisualizer class to ensure it is working
as expected. The DataVisualizer class handles creating a visualization
of the Coronavirus and PyTrends data for the
CoronavirusLifestyleImpacts package.
"""

import unittest
import os.path
from coronavirus_lifestyle_impacts.data_generator import DataGenerator
from coronavirus_lifestyle_impacts.data_processor import DataProcessor
from coronavirus_lifestyle_impacts.data_visualizer import DataVisualizer

class UnitTests(unittest.TestCase):
    """
    This class uses the Python unittest package to run
    a series of tests validating the DataVisualizer class.
    """

    def setUp(self):
        """
        Sets up the tests for the data visualizer. Creates an instance of
        the DataGenerator class with a state set to 'Washington' and keywords
        set to 'Bars near me' and 'Home workouts.' Creates an instance of the
        DataProcessor class with the results from the DataGenerator and runs
        the processed data. Finally, creates an instance of the DataVisualizer
        class to create the visualization to be tested.
        """
        self.state = "Washington"
        self.keywords = ["Bars near me", "Home workouts"]
        self.data_generator = DataGenerator(self.state, self.keywords)
        self.data_generator.get_data()
        data_frames = [self.data_generator.covid_data, self.data_generator.trend_data]
        self.data_processor = DataProcessor(self.data_generator.keywords, data_frames=data_frames)
        self.data_processor.run()
        all_data = self.data_processor.agg_data_frame
        self.data_visualizer = DataVisualizer(self.state, self.keywords, all_data)
        self.data_visualizer.show()

    def test_visualization_generated(self):
        """
        Tests that the DataVisualizer class successfully creates an output
        visualization in the intended folder.
        """
        filepath = "coronavirus_lifestyle_impacts/" + self.state + "_coronavirus_trend_impacts.png"
        self.assertTrue(os.path.isfile(filepath))

if __name__ == '__main__':
    unittest.main()
