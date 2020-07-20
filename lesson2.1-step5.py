import math
from selenium import webdriver
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
try:
    browser.get(link)
    x = browser.find_element_by_id('input_value').text
    y = calc(x)

    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_class_name('btn').click()
    time.sleep(20)
finally:
    browser.quit()