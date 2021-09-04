import time
import random

from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from locators import *


def like(url, headless, cookies):
    if headless == 'off':
        driver = webdriver.Chrome(options=normal_options)
    else:
        driver = webdriver.Chrome(options=headless_options)
    driver.get(url)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    time.sleep(random.randint(3, 5))
