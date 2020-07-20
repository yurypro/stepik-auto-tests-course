import math
from selenium import webdriver
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
try:
    browser.get(link)
    chest = browser.find_element_by_id('treasure')
    x = chest.get_attribute('valuex')
    y = calc(x)

    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_class_name('btn').click()
    time.sleep(20)
finally:
    browser.quit()