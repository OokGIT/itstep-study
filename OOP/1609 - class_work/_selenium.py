from selenium import webdriver
# import base64
# from selenium.webdriver.common.keys import Keys
# import os

my_pass = open('_my_pass', 'r').readline()
print(my_pass)

driver = webdriver.Chrome(executable_path="./chromedriver")

# Токен выдается в CRM с привязкой к IP.
# Если IP "левый", то после логина может вылезти капча.
driver.get('https://online.feeria.ua/cl_refer?oauth_token=2c1c982f45164fddba72cb407b3b9317')

element = driver.find_element_by_id('login')
element.send_keys('aeroua')
element = driver.find_element_by_id('passwd')
element.send_keys(my_pass)
button = driver.find_element_by_class_name('button')
button.click()

