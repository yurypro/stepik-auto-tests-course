import time
from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    browser.find_element_by_class_name('btn').click()
    alert = browser.switch_to.alert
    alert.accept()

    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_class_name('btn').click()
    time.sleep(20)
finally:
    browser.quit()