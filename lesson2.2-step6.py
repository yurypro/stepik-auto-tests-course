import math
from selenium import webdriver
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()
try:
    browser.get(link)
    x = browser.find_element_by_id('input_value').text
    y = calc(x)

    browser.find_element_by_id('answer').send_keys(y)
    robotsCheckbox = browser.find_element_by_id('robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotsCheckbox)
    robotsCheckbox.click()
    robotsRule = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotsRule)
    robotsRule.click()
    button = browser.find_element_by_class_name('btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    time.sleep(20)
finally:
    browser.quit()