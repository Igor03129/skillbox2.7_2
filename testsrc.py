from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.chrome.options import Options

chrome_options = Options()


driver.get("https://www.skillbox.ru")
email_form = driver.find_element("Skillbox")