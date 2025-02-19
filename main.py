from selenium import webdriver

# Set options to make browsing easier
options = webdriver.ChromeOptions()
options.add_argument("disable-infobars")
options.add_argument("start-maximized")
options.add_argument('disable-dev-shm-usage')
options.add_argument("no-sandbox")
options.add_experimental_option("excludeSwitches",
    ["enable-automation"])
options.add_argument("disable-blink-features=AutomationControlled")
driver = webdriver.Chrome()
