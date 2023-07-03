### Bug Report # 1
#### Steps to reproduce:
Send a request to 'http://localhost:8080/v1/cleaning-sessions' with the following body
{"roomSize" : [-100,-100], "coords" : [1,3], "patches" : [[1,0],[2,2],[3,3]], "instructions" : "NNNNNNESEESWNWW"}

Expected result:
An error should be displayed informing the negative values are not allowed and status code should be 400.

Actual result:
Response shows a 200 status code.
Missing roomSize field should display a 4xx error.

Priority:
P2

Reproducability:
100% of the time.

### Bug Report # 2
#### Steps to reproduce:
- Send a request to 'http://localhost:8080/v1/cleaning-sessions' with the following body
{"coords" : [1,3], "patches" : [[1,0],[2,2],[3,3]], "instructions" : "NNNNNNESEESWNWW"}

- Expected result:
400 error should be displayed, error message should inform a missing required field is missing.

- Actual result:
Returns 500 status code 
Missing body should display a 4xx error.

Priority:
P2

Reproducability:
100% of the time.

### Bug Report # 3 
#### Steps to reproduce:
- Send a request to 'http://localhost:8080/v1/cleaning-sessions' with the following body
{}

- Expected result:
400 error should be displayed, error message should inform a missing body.

- Actual result:
Returns 500 status code 

Priority:
P2

Reproducability:
100% of the time.