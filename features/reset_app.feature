Feature: reset app 

    Scenario: reset page
        Given user logged in
        And user cart is not empty
        When user clicks on menu icon
        And user clicks on reset app button
        Then cart is empty
