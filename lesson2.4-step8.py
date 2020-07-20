import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()

try:
    browser.get(link)
    btn_book =  browser.find_element_by_id('book')
    
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    btn_book.click()
    

    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_id('solve').click()
    time.sleep(20)
finally:
    browser.quit()