import time
import random
import modules.login_module, modules.scrapping_module
import eel
from selenium import webdriver
from bs4 import BeautifulSoup
from modules import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Forgotten_script:
    def __init__(self, url, tag, headless, like, retweet):
        self.url = url
        self.tag = tag
        self.like = like
        self.like = retweet
        self.headless = headless
        if tag == 'on':
            self.tag = True
        else:
            self.tag = False

    def like_rt(self, cookies, tag):
        if self.headless == 'off':
            driver = webdriver.Chrome(options=self.normal_options)
        else:
            driver = webdriver.Chrome(options=self.headless_options)
        driver.get(self.url)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
        time.sleep(random.randint(3, 5))
        if self.like and self.retweet:
            like_btn_wait = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.like)))
            rt_btn_wait = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.retweet)))
            like_btn_wait.click()
            rt_btn_wait.click()
            rt_confirm_btn_wait = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.retweet_confirm)))
            rt_confirm_btn_wait.click()
        elif self.like:
            like_btn_wait = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.like)))
            like_btn_wait.click()
        elif self.retweet:
            rt_btn_wait = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.retweet)))
            rt_btn_wait.click()
            rt_confirm_btn_wait = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.retweet_confirm)))
            rt_confirm_btn_wait.click()
        driver.quit()
        if tag:
            if self.headless == 'off':
                driver = webdriver.Chrome(options=self.normal_options)
            else:
                driver = webdriver.Chrome(options=self.headless_options)
            driver.get(self.url)
            for cookie in cookies:
                driver.add_cookie(cookie)
            driver.refresh()
            time.sleep(random.randint(3, 5))
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
            print('Ретвит, тэг, лайк выполнено')

    def subscribe(self, links, cookies):
        if self.headless == 'off':
            driver = webdriver.Chrome(options=self.normal_options)
        else:
            driver = webdriver.Chrome(options=self.headless_options)
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

    def main(self):
        print('Начало работы')
        accounts = []
        with open("accs.txt") as file:
            for line in file:
                accounts.append(line)

        links = modules.scrapping_module.scrapping_tweet(self.url)

        for account in accounts:
            log_pass = account.split(":")
            cookies = modules.login_module.login(log_pass[0], log_pass[1], self.headless)
            self.like_rt(cookies, self.tag)
            self.subscribe(links, cookies)


eel.init("web")


@eel.expose
def url_print(url, headless, tag, like, retweet):
    start = Forgotten_script(url, tag, headless, like, retweet)
    start.main()


eel.start("main.html", size=(500, 300), port=0)
