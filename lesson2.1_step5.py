from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    import math

    def calc(x): 
      return str(math.log(abs(12*math.sin(int(x)))))
  
    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CLASS_NAME, "form-control")
    input1.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
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