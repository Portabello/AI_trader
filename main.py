from selenium import webdriver
from selenium.webdriver.chrome.service import Service

DRIVER_PATH = '/Users/Jasmit/Documents/GitHub/AI_trader/chromedriver-win64/chromedriver.exe'

service = Service(executable_path=DRIVER_PATH)
options = webdriver.ChromeOptions()

#enable headless mode
#options.headless = True
#options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(service=service, options=options)
driver.get('https://bloomberg.com')
print(driver.page_source)
driver.quit()