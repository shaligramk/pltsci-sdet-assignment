# Platform Science SDET Homework Assignment

#### Candidate: Shawn Shaligram 

## Running the tests
Pre-Requisite
- `python -m pip install requests`
- `pip install pytest-bdd`
- pltsci-sdet-assignment container up and running

Running the test suite
Once cloned, from the root of this repository run the following command:
- run `behave`

## Test Scenarios

Assumptions: All parameters/fields in the request body are mandatory

Test scenarios are split into 3 main categories
1. Verify the goldenpath/happy path (P0 cases)
2. Verify error messaging/status code by passing in missing mandatory fields validation
3. Verify error messaging/status code by passing in invalid values.

## Bug Reports
All defects are contained within the bug_reports.md file

## Notes

- Would consider testing the following scenarios if more time:
   - Verify that the API response times are within acceptable limits under normal load conditions
   - Conduct load testing by simulating concurrent requests and verify that the API can handle the expected load without degradation in performance.
   - Verify that the API integrates correctly with any external systems or third-party services it depends on (e.g., database, payment gateway).
   - Verify that the API handles edge cases and boundary conditions correctly (e.g., testing with minimum and maximum allowed values)
