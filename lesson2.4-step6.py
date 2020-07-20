from selenium import webdriver

link = 'http://suninjuly.github.io/cats.html'
browser = webdriver.Chrome()

try:
    browser.find_element_by_id("button")
finally:
    browser.quit()