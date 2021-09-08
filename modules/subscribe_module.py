import time
import random

from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from modules.locators import *


def subscribe(links, cookies, headless):
    if headless == 'off':
        driver = webdriver.Chrome(options=normal_options)
    else:
        driver = webdriver.Chrome(options=headless_options)
    for link in links:
        link = "https://twitter.com" + link
        driver.get(link)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
        time.sleep(random.randint(3, 5))
        subscribe_button_option = driver.find_element_by_xpath(
            '//div[@data-testid="placementTracking"]/div/div').get_attribute(
            "data-testid").split('-')
        if subscribe_button_option[1] == 'follow':
            subscribe_button_wait = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="placementTracking"]/div/div')))
            subscribe_button_wait.click()
        print(f'Подписка на {link} выполнена')
    driver.quit()
