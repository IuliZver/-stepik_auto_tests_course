from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")

        input1 = browser.find_element(By.CLASS_NAME, "first:required")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CLASS_NAME, "second:required")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, "third:required")
        input3.send_keys("test@mail.com")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        browser.quit()

    def test_abs2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")
        input1 = browser.find_element(By.CLASS_NAME, "first:required")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CLASS_NAME, "second:required")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, "third:required")
        input3.send_keys("test@mail.com")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)
        browser.quit()

if __name__ == "__main__":
    unittest.main()