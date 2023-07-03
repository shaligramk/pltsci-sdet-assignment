Platform Science Software Development Engineer in Test assignment
==========================================

## Test Scenarios

Assumptions: All fields in the request are mandatory
Test scenarios are split in 4 groups
1. Happy Path validation.
2. Missing Mandatory fields validation.
3. Invalid Values validation.
4. Invalid API calls. 


## Bugs
In general more descriptive error messages are expected.
The bugs found during execution are listed below:

No negative values should be accepted for roomSize field.

Steps to reproduce:
Send a request to 'http://localhost:8080/v1/cleaning-sessions' with the following body
{"roomSize" : [-3,-3], "coords" : [1,3], "patches" : [[1,0],[2,2],[3,3]], "instructions" : "NNNNNNESEESWNWW"}
Expected result:
An error should be displayed informing the negative values are not allowed and status code should be 400.
Actual result:
Response shows a 200 status code.
Missing roomSize field should display a 400 error.

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

## Execution Report
Over the execution of the test suite, form 14 scenarios executed 3 failed and 11 passed

## How to run test suite
Requirements
Maven latest
pltsci-sdet-assignment container up and running
Running the suite
Once cloned, from the root of this repository run the following: mvn test