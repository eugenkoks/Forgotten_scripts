from Forgotten_scripts import *


def login(login_str, password_str, headless):
    if headless == 'off':
        driver = webdriver.Chrome(options=normal_options)
    else:
        driver = webdriver.Chrome(options=headless_options)
    driver.get(self.start_page)
    time.sleep(random.randint(3, 5))
    try:
        login_input_wait = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.login_input)))
        pass_input_wait = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.password_input)))
        login_input_wait.send_keys(login_str)
        pass_input_wait.send_keys(password_str)
        pass_input_wait.send_keys(Keys.RETURN)
    except StaleElementReferenceException:
        pass
    except NoSuchElementException:
        print('NoSuchElementException')
    except TimeoutException:
        print('TimeoutException')
    cookies = driver.get_cookies()
    print("Успешная авторизация")
    driver.quit()
    return cookies
