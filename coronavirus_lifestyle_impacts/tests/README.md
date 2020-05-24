## How to write a test file
Test files for this pacakge uses Python's `unittest` library. Each test file should only
test functionality within only one component.

## How to run a test file
- To test a single test file, eg, `test_data_generator.py`:
  `pytest tests/test_data_generator.py`
- To run all tests:
  `pytest tests/`

### Sample output:
```
:coronavirus_lifestyle_impacts$ pytest tests/

run `pip install dash[testing]` if you need dash.testing

==================================== test session starts ====================================
platform darwin -- Python 3.7.3, pytest-4.3.1, py-1.8.0, pluggy-0.9.0
rootdir: /path/to/CoronavirusLifestyleImpacts, inifile:
plugins: remotedata-0.3.1, openfiles-0.3.2, doctestplus-0.3.0, arraydiff-0.3, dash-1.6.1
collected 5 items                                                                           

tests/test_data_generator.py .....                                                    [100%]

================================= 5 passed in 14.23 seconds =================================
```
