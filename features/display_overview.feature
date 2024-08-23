Feature: display overview page

    Scenario: go back from product details to overview
        Given product details are displayed
        When user clicks on back to products button 
        Then overview page is displayed

    Scenario: go back from cart details to overview
        Given cart list is displayed 
        When user click on continue shopping button
        Then overview page is displayed