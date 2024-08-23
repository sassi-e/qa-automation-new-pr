Feature: remove product from cart

    Scenario: remove product in the products page
        Given the products are displayed
        And user added product to cart
        When user clicks on remove product
        Then button changes
        And product removed from cart

    Scenario: remove product in cart page
        Given the products are displayed
        And user added product to cart
        When user clicks on cart icon
        And the chosen products are displayed
        And user clicks on remove item
        Then product removed from cart list