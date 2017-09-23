from pyvirtualdisplay import Display
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException

def init_browser():
	browser = webdriver.Chrome()
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

def go_site(browser):
	try:
		first_link = browser.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"rso\"]/div/div/div[1]/div/div/h3/a")))
		first_link.click()
	except TimeoutException:
		print("Cannot find first link")

if __name__ == "__main__":
	display = Display(visible=1, size=(800, 600))
	display.start()
	browser = init_browser()
	lookup(browser, "https://depannage.alexisgaillac.fr")
	go_site(browser)
	time.sleep(10)
	browser.quit()
	print("Successfuly completed")
