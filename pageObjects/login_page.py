from common_page import *
from pageLocators.login_page_locators import *

class LoginPage(self):
    def __init__(self,driver) :
        self.driver = driver


    def load_page(self):
        self.URL="https://www.saucedemo.com/"
        self.driver.get(self.URL)
        CommonPage.is_element_displayed(LoginPageLocators.login_button)
    
    def enter_username(self,username):
        CommonPage.enter_text_to_input(username, LoginPageLocators.username_input)

    def enter_password(self,password):
        CommonPage.enter_text_to_input(password ,LoginPageLocators.password_input)

    def click_login(self):
        CommonPage.click_on_button(LoginPageLocators.login_button)
    
    def is_user_connected(self):
        self.expected_url="https://www.saucedemo.com/inventory.html"
        CommonPage.assert_url(self.expected_url)

    def is_user_connection_refused(self):
        self.expected_url="https://www.saucedemo.com/"
        CommonPage.assert_url(self.expected_url)