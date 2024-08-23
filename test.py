from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })
driver = webdriver.Remote(command_executor='http://selenium-hub:4444/wd/hub', options=chrome_options)

driver.get("https://www.googole.com")
print("hello google")

driver.quit()