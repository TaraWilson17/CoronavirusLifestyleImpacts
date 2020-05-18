import unittest
import functions as func

class UnitTests(unittest.TestCase):
    
    def test_covid_data_is_not_empty(self):
        self.assertFalse(covid_data.empty)
        
    def test_trend_data_is_not_empty(self):
        self.assertFalse(trend_data.empty)
        
    def test_trend_data_has_expected_columns(self):
        expected_columns = keywords + ["isPartial"]
        self.assertCountEqual(list(trend_data.columns), expected_columns)
        
    def test_covid_data_is_for_correct_state(self):
        state_col = list(covid_data.AdminRegion1)
        self.assertListEqual(state_col, [state] * len(state_col))
        
    def test_covid_data_contains_needed_columns(self):
        expected_columns = ["Updated", "Deaths", "Recovered", "AdminRegion1"]
        self.assertTrue(all(x in list(covid_data.columns) for x in expected_columns))
    

if __name__ == '__main__':
    state = "Washington"
    keywords = ["Bars near me", "Home workouts"]
    covid_data, trend_data = func.get_data(state, keywords)
    unittest.main()