import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException

def init_browser():
	path_to_chromedriver = './chromedriver'
	browser = webdriver.Chrome(executable_path=path_to_chromedriver)
	browser.wait = WebDriverWait(browser, 5)
	return browser

def lookup(browser, query):
	browser.get('https://google.com')
	try:
		box = browser.wait.until(EC.presence_of_element_located((By.NAME, "q")))
		button = browser.wait.until(EC.element_to_be_clickable((By.NAME, "btnK")))
		box.send_keys(query)
		try:
			button.click()
		except ElementNotVisibleException:
			button = browser.wait.until(EC.visibility_of_element_located((By.NAME, "btnG")))
			button.click()
	except TimeoutException:
		print("Box or Button not found in google.com")

if __name__ == "__main__":
	browser = init_browser()
	lookup(browser, "website.com")
	time.sleep(5)
	browser.quit()