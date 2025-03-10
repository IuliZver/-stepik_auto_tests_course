from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    import math

    def calc(x): 
      return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("window.scrollBy(0, 150)", "")
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    option1 = browser.find_element(By.ID, "robotCheckbox").click()
    option2 = browser.find_element(By.ID, "robotsRule").click()
    button.click()
    # ждем загрузки страницы
    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()