from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from selenium.webdriver.common.by import By

class CommonPage(self):
    def __init__(self,driver) :
        self.driver = driver


    def is_element_displayed(self,xpath):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            if element.is_displayed():
                print("element detected")
        except TimeoutException:  
            print ("element was not found")


    def click_on_button(self,xpath):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.click()
        except NoSuchElementException:  
            print ("element was not found")


    def enter_text_to_input(self,text_to_enter,input_xpath):
        self.is_element_displayed(input_xpath)
        self.driver.find_element(By.XPATH, input_xpath).send_keys(text_to_enter)


    def assert_url(self, expected_url):
        current_url = self.driver.current_url()
        self.assertEqual(current_url,expected_url, "the obtained url is not equal to the expected one, please check")
