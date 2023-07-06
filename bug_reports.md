### Bug Report # 1
#### Steps to reproduce:
- Send a request to 'http://localhost:8080/v1/cleaning-sessions' with the following body
{"coords" : [1,3], "patches" : [[1,0],[2,2],[3,3]], "instructions" : "NNNNNNESEESWNWW"}

- Expected result:
400 error should be displayed, error message should inform a missing required field is missing.

- Actual result:
Returns 500 status code
{"timestamp":"2023-07-06T02:37:10.228+0000","path":"/v1/cleaning-sessions","status":400,"error":"Bad Request","message":"Failed to read HTTP message"}%
Missing body should display a 4xx error.

Priority:
P2

Reproducability:
100% of the time.

### Bug Report # 2
#### Steps to reproduce:
- Send a request to 'http://localhost:8080/v1/cleaning-sessions' with the following body
{}

- Expected result:
400 error should be displayed, error message should inform a missing body.

- Actual result:
Returns 500 status code 
{"timestamp":"2023-07-06T02:36:01.663+0000","path":"/v1/cleaning-sessions","status":500,"error":"Internal Server Error","message":null}%

Priority:
P2

Reproducability:
100% of the time.