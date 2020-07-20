from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects2.html'
browser = webdriver.Chrome()

try:
    page = browser.get(link)
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    total = str(int(num1)+int(num2))
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(total)

    browser.find_element_by_class_name("btn").click()

    time.sleep(20)
finally:
    browser.quit()