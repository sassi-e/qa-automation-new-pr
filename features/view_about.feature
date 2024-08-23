Feature: display about page

    Scenario: check about page
        Given user connected
        When user clicks on menu icon
        And user clicks on about button
        Then about page is displayed