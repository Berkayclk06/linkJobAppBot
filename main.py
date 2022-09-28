import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

chrome_driver_path = "C:/Development/chromedriver.exe"

linkedin_url = "https://www.linkedin.com/jobs/search/?currentJobId=3273291208&distance=25&f_AL=true&f_E=1%2C2&f_WT=2%2C1%2C3&geoId=100025096&keywords=python%20developer"

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get(linkedin_url)
driver.maximize_window()

sing_in = driver.find_element("class name", "nav__button-secondary")
sing_in.click()
time.sleep(3)

username_input = driver.find_element("id", "username")
password_input = driver.find_element("id", "password")
username_input.send_keys(os.environ["MY_EMAIL"])
password_input.send_keys(os.environ["MY_PASS"])

signin_btn = driver.find_element("class name", "btn__primary--large")
signin_btn.click()

time.sleep(2)
easyapp_btn = driver.find_element("class name", "jobs-apply-button")
easyapp_btn.click()

time.sleep(5)
driver.find_element("css selector", 'button[aria-label="Continue to next step"]').click()

driver.find_element("css selector", 'button[aria-label="Review your application"]').click()



