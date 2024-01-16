from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


DRIVER_PATH = '/Users/Jasmit/Documents/GitHub/AI_trader/chromedriver-win64/chromedriver.exe'

service = Service(executable_path=DRIVER_PATH)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#enable headless mode
#options.headless = True
#options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(service=service, options=options)
driver.get('https://bloomberg.com')
articles = driver.find_elements(By.XPATH, "//div[@data-type='article']")
print("-------------------------")
print(articles)

link_list = []
headline_list = []

for article in articles:
	content = article.get_attribute('innerHTML')
	soup = BeautifulSoup(content, 'html.parser')
	link = soup.find('a')	
	href_link = "https://bloomberg.com"+link.get('href')
	headline_text = soup.select_one('div[data-component="headline"]').get_text(strip=True)

	#headline = article.find_element(By.XPATH, ".//div[@data-component='headline']")
	#headline_html = headline.get_attribute("outerHTML")
	#soup_1 = BeautifulSoup(headline_html, 'html.parser')
	#headline_text = soup.get_text(strip=True)
	link_list.append(href_link)
	headline_list.append(headline_text)
	print(f"link: {href_link}\n headline: {headline_text}\n")
#driver.quit()

output_file_path = "/Users/Jasmit/Documents/GitHub/AI_trader/logs/bloomberg_frontpage.txt"

with open(output_file_path, 'w', encoding='utf-8') as file:
    for headline, link in zip(headline_list, link_list):
        file.write(f"{headline}\n{link}\n\n")