from selenium import webdriver
from pathlib import Path
import time

file_path = Path.cwd() /'test.txt'
print(file_path)

link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
try:
    browser.get(link)
    browser.find_element_by_name("firstname").send_keys('Ivan')
    browser.find_element_by_name("lastname").send_keys('Ivanov')
    browser.find_element_by_name('email').send_keys('ivan.ivanov@mail.ru')
    browser.find_element_by_name('file').send_keys(file_path.as_posix())
    browser.find_element_by_class_name('btn').click()
    time.sleep(20)
finally:
    browser.quit()