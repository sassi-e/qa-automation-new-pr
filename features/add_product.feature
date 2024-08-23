Feature: fill the cart

    Scenario: add product to cart from overview page
        Given user connected and elements displayed
        When user chooses product from page
        And user clicks on button to add product to cart
        Then button changes
        And product added to cart

    Scenario: add product to cart from product detail page
        Given user connected and elements displayed
        When user chooses product from page and clicks on product
        And user clicks on button to add product to cart
        Then button changes
        And product added to cart

    