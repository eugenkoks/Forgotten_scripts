import time
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from modules.locators import *
from modules.login_module import login


def like_rt_tag(url, headless, cookies, like_int, retweet_int, tag_int):
    if headless == 'off':
        driver = webdriver.Chrome(options=normal_options)
    else:
        driver = webdriver.Chrome(options=headless_options)
    driver.get(url)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    time.sleep(random.randint(3, 5))
    if like_int == 'on' and retweet_int == 'on' and tag_int == 'on':
        like_btn_wait = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, like)))
        rt_btn_wait = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, retweet)))
        like_btn_wait.click()
        rt_btn_wait.click()
        rt_confirm_btn_wait = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, retweet_confirm)))
        rt_confirm_btn_wait.click()
        driver.find_element_by_xpath("//div[@data-testid='reply'][@role='button']").click()
        time.sleep(3)
        tag_name = 'johpohan'
        driver.find_element_by_xpath("//div[@data-testid='tweetTextarea_0'][@role='textbox']").send_keys(
            f"@{tag_name} ")
        time.sleep(3)
        driver.find_element_by_xpath("//div[@data-testid='tweetButton'][@role='button']").click()
        print('Тэгнул.')
        time.sleep(3)
        driver.quit()
    elif like_int == 'on':
        like_btn_wait = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, like)))
        like_btn_wait.click()
        driver.quit()
    elif retweet_int == 'on':
        rt_btn_wait = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, retweet)))
        rt_btn_wait.click()
        rt_confirm_btn_wait = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, retweet_confirm)))
        rt_confirm_btn_wait.click()
        driver.quit()
    elif tag_int == 'on':
        driver.find_element_by_xpath("//div[@data-testid='reply'][@role='button']").click()
        time.sleep(3)
        tag_name = 'johpohan'
        driver.find_element_by_xpath("//div[@data-testid='tweetTextarea_0'][@role='textbox']").send_keys(
            f"@{tag_name} ")
        time.sleep(3)
        driver.find_element_by_xpath("//div[@data-testid='tweetButton'][@role='button']").click()
        print('Тэгнул.')
        time.sleep(3)
        driver.quit()


if __name__ == '__main__':
    cookies_int = login('89952993278', 'Padre19732846', 'off')
    like_rt_tag('https://twitter.com/KeithAdam10/status/1432822520248479751', 'off', cookies_int, 'on', 'on', 'on')