import time
import random

from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from modules.locators import *


def login(login_str, password_str, headless):
    if headless == 'off':
        driver = webdriver.Chrome(options=normal_options)
    else:
        driver = webdriver.Chrome(options=headless_options)
    driver.get(start_page)
    time.sleep(random.randint(3, 5))
    try:
        login_input_wait = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, login_input)))
        pass_input_wait = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, password_input)))
        login_input_wait.send_keys(login_str)
        pass_input_wait.send_keys(password_str)
        pass_input_wait.send_keys(Keys.RETURN)
    except StaleElementReferenceException:
        print('StaleElementReferenceException')
    except NoSuchElementException:
        print('NoSuchElementException')
    except TimeoutException:
        print('TimeoutException')
    cookies = driver.get_cookies()
    print("Успешная авторизация")
    driver.quit()
    return cookies


if __name__ == '__main__':
    login('89952993278', 'Padre19732846', 'off')
