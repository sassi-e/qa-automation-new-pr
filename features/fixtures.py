from selenium import webdriver

global chromeDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--whitelisted-ips")
chrome_options.add_argument("--verbose")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--incognito")
chrome_options.accept_insecure_certs = True

chrome_options.add_experimental_option("prefs", {
            "download.default_directory": "/home/seluser/Downloads",
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })

def browser_chrome(context, timeout=30, **kwargs):
    if hasattr(context, 'browser') == False:
        context.browser = webdriver.Remote(command_executor='http://selenium-hub:4444/wd/hub',
                                desired_capabilities=chrome_options.to_capabilities())
        context.browser.maximize_window()
        context.browser.delete_all_cookies()

    global config
    config = context.config