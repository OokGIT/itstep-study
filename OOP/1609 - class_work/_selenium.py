from selenium import webdriver
# import base64
# from selenium.webdriver.common.keys import Keys
# import os

my_pass = open('_my_pass', 'r').readline()
phone_number = '0800604439'
login_url = 'https://online.feeria.ua/cl_refer?oauth_token=2c1c982f45164fddba72cb407b3b9317'
# agent_url = 'https://online.feeria.ua/edit_agency?oauth_token=2c1c982f45164fddba72cb407b3b9317&'

driver = webdriver.Chrome(executable_path="./chromedriver")

# Логинимся...
# Токен выдается в CRM с привязкой к IP.
# Если IP "левый", то после логина может вылезти капча.
driver.get(login_url)
element = driver.find_element_by_id('login')
element.send_keys('aeroua')
element = driver.find_element_by_id('passwd')
element.send_keys(my_pass)
button = driver.find_element_by_class_name('button')
button.click()

# Заходим в нужную вкладку..
agency_button = driver.find_element_by_xpath('//*[@id="cl_refer"]/div[2]/div/div[5]/a')
agency_button.click()

# Заполняем необходимое поле и сохраняем профайл агентства
phone_3 = driver.find_element_by_xpath('//*[@id="edit_agency"]/div[3]/fieldset[1]/table/tbody/tr[9]/td[2]/input')
phone_3.send_keys(phone_number)
button = driver.find_element_by_xpath('//*[@id="edit_agency"]/div[3]/input[4]')
button.click()
