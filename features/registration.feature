Feature: Registration feature
  Scenario: Validating Registration page scenario
    Given I navigate to the URL qa.way2automation.com
    When I enter name as "<name>"
    Then I enter phonenum as "<phonenum>"
    And I enter email as "<email>"
    And I enter city as "<city>"
    And I enter country as "<country>"
    And I enter username as "<username>"
    And I enter password as "<password>"