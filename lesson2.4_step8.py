from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/explicit_wait2.html")
    
    # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    btn = browser.find_element(By.ID, "book").click()
    
    def calc(x): 
      return str(math.log(abs(12*math.sin(int(x)))))
      
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    button = browser.find_element(By.ID, "solve")
    button.click()
finally:
    time.sleep(30)
    browser.quit()
   
