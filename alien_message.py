import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--ignore-ssl-errors")
    browser = webdriver.Chrome(options=chrome_options)
    login_page = "https://stepik.org/catalog?auth=login"
    browser.get(login_page)  
    
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "login"))).send_keys("idontbelieveinmiracles@mail.ru")
    browser.find_element(By.NAME, "password").send_keys("Sugarbaby25!")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    wait_after_login(browser)  # Добавляем ожидание после авторизации
    
    yield browser
    print("\nquit browser..")
    browser.quit()

def wait_after_login(browser):
    """Ожидание после авторизации, чтобы убедиться, что страница загрузилась."""
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.navbar__profile-toggler")))
        print("Login successful and page loaded")
    except Exception as e:
        print(f"Failed to wait after login: {e}")
        pytest.fail("Failed to wait after login")
@pytest.mark.parametrize('link', [
"https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1","https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])       
class TestMessage:
    links = []
    
    def test_guest_should_see_alien_message(self, browser, link):
        browser.implicitly_wait(30)
        browser.get(link)
        browser.implicitly_wait(10)
        # Ввод правильного ответа
        try:
            answer = str(math.log(int(time.time())))
            textarea = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.ember-text-area")))
            textarea.clear()
            textarea.send_keys(answer)
            print("Answer entered")
        except Exception as e:
            print(f"Failed to enter answer: {e}")
            pytest.fail("Failed to enter answer")

        # Отправка ответа
        try:
            button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
            button.click()
            print("Answer submitted")
        except Exception as e:
            print(f"Failed to submit answer: {e}")
            pytest.fail("Failed to submit answer")

        # Проверка фидбека
        try:
            hint = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "p.smart-hints__hint"))).text
            assert 'Correct!' in hint
            print("Feedback checked successfully")
        except AssertionError:
            self.links.append(link)
            print(f"Feedback is incorrect for link: {link}")
        except Exception as e:
            print(f"Failed to check feedback: {e}")
            pytest.fail("Failed to check feedback")

if __name__ == "__main__":
    pytest.main()
