from selenium import webdriver
import time

options = webdriver.chrome.options.Options()
driver = webdriver.Chrome()
driver.get('https://www.google.co.jp')
search_bar = driver.find_element_by_name("q")
search_bar.send_keys("python")
search_bar.submit()
    
time.sleep(3)

driver.close()