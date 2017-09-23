from selenium import webdriver
import time

path_to_chromedriver = './chromedriver'
browser = webdriver.Chrome(executable_path=path_to_chromedriver)

url = 'https://google.com'
browser.get(url)

time.sleep(5)
browser.quit()