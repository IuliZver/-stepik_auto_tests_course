import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys("test@mail.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path) 
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(30)
    browser.quit()



#Чтобы было понятнее зачем это просто закомментите строку #element.send_keys(file_path) и добавьте 

#print(current_dir) #покажет вам дирректорию, в которой у вас лежит ваш исполняемый код

#print(file_path) #путь до вашего файла который вы хотите загрузить

#Правильно понял ?

#А при нахождении элемента для отправки файла используется функция send_keys, в которую передается аргумент file_path, нахождение файла для передачи