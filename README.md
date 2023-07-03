Shawn Shaligram Platform Science SDET Homework assignment
==========================================

## Test Scenarios

Assumptions: All parameters/fields in the request body are mandatory

Test scenarios are split into 3 main categories
1. Verify the goldenpath/happy path (P0 cases)
2. Verify error messaging/status code by passing in missing mandatory fields validation
3. Verify error messaging/status code by passing in invalid values.


## Bugs
The bugs found during execution are listed below:

#### Test Case: 1 No negative values should be accepted for roomSize field.

Steps to reproduce:
Send a request to 'http://localhost:8080/v1/cleaning-sessions' with the following body
{"roomSize" : [-10,-10], "coords" : [1,3], "patches" : [[1,0],[2,2],[3,3]], "instructions" : "NNNNNNESEESWNWW"}
Expected result:
An error should be displayed informing the negative values are not allowed and status code should be 400.
Actual result:
Response shows a 200 status code.
Missing roomSize field should display a 4xx error.

Steps to reproduce:
- Send a request to 'http://localhost:8080/v1/cleaning-sessions' with the following body
{"coords" : [1,3], "patches" : [[1,0],[2,2],[3,3]], "instructions" : "NNNNNNESEESWNWW"}
- Expected result:
400 error should be displayed, error message should inform a missing required field is missing.
- Actual result:
500 error thrown.
Missing body should display a 400 error.

Steps to reproduce:
- Send a request to 'http://localhost:8080/v1/cleaning-sessions' with the following body
{}
- Expected result:
400 error should be displayed, error message should inform a missing body.
- Actual result:
500 error thrown.

## How to run test suite
Requirements
pip install requests
pip install pytest-bdd
pltsci-sdet-assignment container up and running
Running the suite
Once cloned, from the root of this repository run the following: mvn test