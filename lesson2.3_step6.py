from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
link = "https://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "button.trollface").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    def calc(x): 
      return str(math.log(abs(12*math.sin(int(x)))))
      
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(30)
    browser.quit()
    
#Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти. Это делается с помощью команды switch_to.window:

#browser.switch_to.window(window_name)
#Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок. Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:

#new_window = browser.window_handles[1]
#Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:

#first_window = browser.window_handles[0]
#После переключения на новую вкладку поиск и взаимодействие с элементами будут происходить уже на новой странице.



