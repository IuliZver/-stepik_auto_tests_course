import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


"""@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()"""
def test_guest_should_see_login_link(browser):
    link = f"https://stepik.org/catalog?auth=login"
    browser.get(link)
    browser.implicitly_wait(10)
    input1 = browser.find_element(By.NAME, "login")
    input1.send_keys("idontbelieveinmiracles@mail.ru")
    input2 = browser.find_element(By.NAME, "password")
    input2.send_keys("Sugarbaby25!")
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()
 
 