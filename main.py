from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


DRIVER_PATH = '/Users/Jasmit/Documents/GitHub/AI_trader/chromedriver-win64/chromedriver.exe'

service = Service(executable_path=DRIVER_PATH)
options = webdriver.ChromeOptions()

#enable headless mode
#options.headless = True
#options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(service=service, options=options)
driver.get('https://bloomberg.com')
#print(driver.page_source)
articles = driver.find_elements(By.XPATH, "//div[@data-type='article']")
print("-------------------------")
print(articles)
for article in articles:
    #title = article.find_element(By.XPATH, ".//h2").text
    content = article.get_attribute('innerHTML')
    print(f"Content: {content}\n")
driver.quit()