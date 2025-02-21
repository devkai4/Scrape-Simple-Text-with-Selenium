from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument('disable-dev-shm-usage')
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",
        ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.get("https://automated.pythonanywhere.com/")
    return driver

def main():
    driver = get_driver()
    element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[1]")
    text = element.text
    driver.quit()
    return text

if __name__ == "__main__":
    print(main())
