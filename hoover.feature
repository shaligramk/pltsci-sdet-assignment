Feature: Hoover Service

  Scenario: Hoover successfully navigates through the room and cleans patches of dirt
    Given a room size of 5, 5
    And the hoover is initially placed at 1, 2
    And there are patches of dirt at the following locations:
      | dirtCoordX | dirtCoordY |
      | 1          | 0          |
      | 2          | 2          |
      | 2          | 3          |
    And the driving instructions are "NNESEESWNWW"
    When the hoover service is invoked
    Then the final hoover position should be 1, 3
    And the number of cleaned patches should be 1

  Scenario: Hoover placed outside the room boundaries
    Given a room size of 5, 5
    And the hoover is initially placed at 6, 3
    And there are no patches of dirt
    And the driving instructions are "N"
    When the hoover service is invoked
    Then the final hoover position should be 5, 3
    And the number of cleaned patches should be 0

  Scenario: Hoover encounters an invalid instruction
    Given a room size of 5, 5
    And the hoover is initially placed at 2, 2
    And there are no patches of dirt
    And the driving instructions are "NXS"
    When the hoover service is invoked
    Then the final hoover position should be 2, 2
    And the number of cleaned patches should be 0

  Scenario: Hoover encounters an obstacle (wall)
    Given a room size of 5, 5
    And the hoover is initially placed at 0, 0
    And there are no patches of dirt
    And the driving instructions are "SSSS"
    When the hoover service is invoked
    Then the final hoover position should be 0, 0
    And the number of cleaned patches should be 0
