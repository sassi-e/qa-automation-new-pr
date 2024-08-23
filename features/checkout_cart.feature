Feature: checkout cart 

    Scenario: confirm items' list
        Given user checked cart
        When user clicks on checkout
        And user enter his information to form
        And user clicks on continue
        And checkout overview displayed
        And user clicks on finish
        Then order passed successfully
