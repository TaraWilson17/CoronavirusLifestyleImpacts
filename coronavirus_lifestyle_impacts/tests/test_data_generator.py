"""
This script tests the DataGenerator class to ensure it is working
as expected. The DataGenerator class handles the downloading
and retrieving of the Coronavirus and PyTrends data for the
CoronavirusLifestyleImpacts package.
"""

from context import coronavirus_lifestyle_impacts
import unittest
from coronavirus_lifestyle_impacts.data_generator import DataGenerator

class UnitTests(unittest.TestCase):
    """
    This class uses the Python unittest package to run
    a series of tests validating the DataGenerator class.
    """

    def test_covid_data_is_not_empty(self):
        """
        Asserts that the Coronavirus dataframe is not empty.
        """
        self.assertFalse(DG.covid_data.empty)

    def test_trend_data_is_not_empty(self):
        """
        Asserts that the PyTrends dataframe is not empty.
        """
        self.assertFalse(DG.trend_data.empty)

    def test_trend_data_has_expected_columns(self):
        """
        Asserts that the PyTrends dataframe contains a column for each
        keyword as well as a column for `isPartial` which denotes if the
        data for a given week is completed or not.
        """
        expected_columns = KEYWORDS + ["isPartial"]
        self.assertCountEqual(list(DG.trend_data.columns), expected_columns)

    def test_covid_data_is_for_correct_state(self):
        """
        Asserts that the data in the Coronavirus dataframe has been filtered
        to only include data from the specified state.
        """
        state_col = list(DG.covid_data.AdminRegion1)
        self.assertListEqual(state_col, [STATE] * len(state_col))

    def test_covid_data_contains_needed_columns(self):
        """
        Asserts that the Coronavirus dataframe contains at least the expected
        columns. The needed columns are `Updated` which represents the date field,
        `Deaths` which is the daily count of deaths, `Recovered` which is the
        daily count of recovered patients and `AdminRegion1` which denotes the
        state.
        """
        expected_columns = ["Updated", "Deaths", "Recovered", "AdminRegion1"]
        self.assertTrue(all(x in list(DG.covid_data.columns) for x in expected_columns))


if __name__ == '__main__':
    STATE = "Washington"
    KEYWORDS = ["Bars near me", "Home workouts"]
    DG = DataGenerator([STATE, KEYWORDS])
    DG.run()
    unittest.main()
