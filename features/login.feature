Feature: Login user

    Scenario: login user
        Given login page displayed
        When user enter <username> and <password>
        And user clicks on login button
        Then <page> displayed
    
    |      username  |    password  | page      |
    | standard_user  | secret_sauce | overview  |
    | locked_out_user| secret_sauce | login     |
    | problem_user   | secret_sauce | overview  |
    | performance_glitch_user  | secret_sauce | overview  |
    | error_user     | secret_sauce | overview  |
    | visual_user    | secret_sauce | overview  |
    |  test          | test         |  login    |
    | test           |              |  login    |