import unittest
from data_generator import DataGenerator

class UnitTests(unittest.TestCase):

    def test_covid_data_is_not_empty(self):
        self.assertFalse(dg.covid_data.empty)

    def test_trend_data_is_not_empty(self):
        self.assertFalse(dg.trend_data.empty)

    def test_trend_data_has_expected_columns(self):
        expected_columns = keywords + ["isPartial"]
        self.assertCountEqual(list(dg.trend_data.columns), expected_columns)

    def test_covid_data_is_for_correct_state(self):
        state_col = list(dg.covid_data.AdminRegion1)
        self.assertListEqual(state_col, [state] * len(state_col))

    def test_covid_data_contains_needed_columns(self):
        expected_columns = ["Updated", "Deaths", "Recovered", "AdminRegion1"]
        self.assertTrue(all(x in list(dg.covid_data.columns) for x in expected_columns))
    

if __name__ == '__main__':
    dg = DataGenerator([])
    dg.run()
    state = "Washington"
    keywords = ["Bars near me", "Home workouts"]
    unittest.main()
