from common_page import *
from pageLocators.product_page_locators import *

class ProductPage(self):
    def __init__(self,driver) :
        self.driver = driver

    def is_product_displayed(self):
        CommonPage.is_element_displayed(ProductPageLocators.page_title)
        CommonPage.is_element_displayed(ProductPageLocators.inventory_list)

    def scroll_to_product(self,product_name):
        self.product_xpath= f"//div/a/div[contains(text(), '{product_name}')]"
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(By.XPATH,self.product_xpath))
        self.product=self.driver.find_element(By.XPATH,self.product_xpath)
        self.add_to_cart_button = self.product.find_element(By.XPATH, "./following-sibling::div/button")
        WebDriverWait(self.driver, 15).until(EC.element_to_be_visible((By.XPATH,self.add_to_cart_button)))
        return self.add_to_cart_button

    def click_on_add_product_to_cart(self,product):
        product_button=self.scroll_to_product(product)
        CommonPage.click_on_button(product_button)