from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def sum(x, y):
       return str(x + y)
try: 
    link = "https://suninjuly.github.io/selects2.html" #должно работать и с https://suninjuly.github.io/selects1.html
    browser = webdriver.Chrome()
    browser.get(link)
  
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    a = int(num1)+int(num2)
    a = str(a)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(a) # ищем элемент с текстом суммы значений x+y в строковом формате    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    # ждем загрузки страницы
    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()