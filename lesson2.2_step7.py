import os
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Firefox()
browser.get(link)
current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)


#Чтобы было понятнее зачем это просто закомментите строку #element.send_keys(file_path) и добавьте 

#print(current_dir) #покажет вам дирректорию, в которой у вас лежит ваш исполняемый код

#print(file_path) #путь до вашего файла который вы хотите загрузить

#Правильно понял ?

#А при нахождении элемента для отправки файла используется функция send_keys, в которую передается аргумент file_path, нахождение файла для передачи