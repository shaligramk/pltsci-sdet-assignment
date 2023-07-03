Feature: Hoover Navigation Validation


# Verify Goldenpath/Happy Path (P0 test cases)
  Scenario Outline: Validate patches and coords are properly calculated for different roomSize and same coords and patches
    Given url 'http://localhost:8080/v1/cleaning-sessions'
    And request {"roomSize" : <roomSize>, "coords" : [2,1], "patches" : [[1,0],[2,2],[2,3]], "instructions" : "NNESEESWNWW"}
    When method POST
    Then status 200
    And match $.coords == [1,3]
    And match $.patches == 1
  Examples:
    |roomSize|
    |[5,5]   |
    |[6,6]   |
    |[7,7]   |

# Invalid Values (Error Handling)
  Scenario: Validate error is displayed when patches are outside the roomSize
    Given url 'http://localhost:8080/v1/cleaning-sessions'
    And request {"roomSize" : [3,3], "coords" : [1,2], "patches" : [[1,0],[2,2],[3,3]], "instructions" : "NNNNNNESEESWNWW"}
    When method POST
    Then status 400

  Scenario: Validate error is displayed when start point is outside the roomSize
    Given url 'http://localhost:8080/v1/cleaning-sessions'
    And request {"roomSize" : [3,3], "coords" : [1,3], "patches" : [[1,0],[2,2],[3,3]], "instructions" : "NNNNNNESEESWNWW"}
    When method POST
    Then status 400

  Scenario: Validate no negative values are accepted for roomSize
    Given url 'http://localhost:8080/v1/cleaning-sessions'
    And request {"roomSize" : [-100,-100], "coords" : [1,3], "patches" : [[1,0],[2,2],[3,3]], "instructions" : "NNNNNNESEESWNWW"}
    When method POST
    Then status 400

  Scenario: Validate no negative values are accepted for start point
    Given url 'http://localhost:8080/v1/cleaning-sessions'
    And request {"roomSize" : [3,3], "coords" : [-100,-7], "patches" : [[1,0],[2,2],[3,3]], "instructions" : "NNNNNNESEESWNWW"}
    When method POST
    Then status 400

# Missing API Fields/Parameters
  Scenario: Validate missing roomSize error
    Given url 'http://localhost:8080/v1/cleaning-sessions'
    And request {"coords" : [-1,-3], "patches" : [[1,0],[2,2],[3,3]], "instructions" : "NNNNNNESEESWNWW"}
    When method POST
    Then status 400

  Scenario: Validate missing coords error
    Given url 'http://localhost:8080/v1/cleaning-sessions'
    And request {"roomSize" : [3,3], "patches" : [[1,0],[2,2],[3,3]], "instructions" : "NNNNNNESEESWNWW"}
    When method POST
    Then status 400

  Scenario: Validate missing instructions error
    Given url 'http://localhost:8080/v1/cleaning-sessions'
    And request {"roomSize" : [3,3], "coords" : [-1,-3], "patches" : [[1,0],[2,2],[3,3]]}
    When method POST
    Then status 400

  Scenario: Validate missing patches error
    Given url 'http://localhost:8080/v1/cleaning-sessions'
    And request {"roomSize" : [3,3], "coords" : [-1,-3], "instructions" : "NNNNNNESEESWNWW"}
    When method POST
    Then status 400

# Invalid API Calls to check error messaging/status code
  Scenario: Validate 405 status code is returned for incorrect HTTP method
    Given url 'http://localhost:8080/v1/cleaning-sessions'
    And request {"roomSize" : [3,3], "coords" : [1,2], "patches" : [[1,0],[2,2],[3,3]], "instructions" : "NNNNNNESEESWNWW"}
    When method GET
    Then status 405
    And match $.error == "Method Not Allowed"

  Scenario: Validate error is displayed for wrong path
    Given url 'http://localhost:8080/v1/nba-basketball'
    And request {"roomSize" : [3,3], "coords" : [1,2], "patches" : [[1,0],[2,2],[3,3]], "instructions" : "NNNNNNESEESWNWW"}
    When method POST
    Then status 404
    And match $.error == "Not Found"