from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time
link = "https://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    
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



