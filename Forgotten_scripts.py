import os
import pickle
import time
from random import random

import eel
import lxml
from selenium import webdriver
from bs4 import BeautifulSoup
import pickle

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Forgotten_script:
    def __init__(self, url, password, login, tag, headless):
        self.url = url
        self.password_str = password
        self.login_str = login
        self.tag = tag
        self.headless = headless
        self.login_div = '/html/body/div/div/div/div[2]/main/div/div'
        self.login_input = '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
        self.password_input = '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
        self.authorize_btn = '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div'
        self.news_page_div = '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div'
        self.wrond_pass_div = '/html/body/div/div/div/div[2]/main/div/div/div[1]/div'
        self.tweet_page = '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/article/div/div/div/div[3]/div[1]/div/div[1]'
        self.tweet_id = '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/article/div/div/div/div[3]/div[1]/div/div[1]'
        self.like = '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[3]/div[5]/div/div[3]/div/div/div'
        self.retweet = '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div[1]/article/div/div/div/div[3]/div[5]/div[2]/div'
        self.retweet_confirm = '/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[3]/div/div/div/div'
        self.subscribe_button = '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div[4]/div/div'
        self.start_page = 'https://twitter.com/login'
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_argument("javascript.enabled")
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.123 Safari/537.36")
        if headless == "on":
            options.add_argument('--headless')
        else:
            options.add_argument('--window-size=800,900')
        if tag == 'on':
            pass
        else:
            pass
        self.driver = webdriver.Chrome(options=options)
        self.driver.wait = WebDriverWait(self.driver, 3)

    def scrapping_tweet(self, url):
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.tweet_page)))
        tweet_id = self.driver.find_element_by_xpath(self.tweet_id).get_attribute('id')
        html = self.driver.page_source
        soup = BeautifulSoup(html, "lxml")
        all_link = soup.find(id=tweet_id).find_all('a')
        links = []
        for link in all_link:
            if link.get('href').split('/')[1] == 'hashtag':
                continue
            else:
                links.append(link.get('href'))
        return links

    def check_url(self, url):
        self.driver.get(url)
        chk_url = self.driver.current_url
        if chk_url != url:
            return False
        else:
            return True

    def login(self, max_try=5):
        while not self.check_url(self.start_page) or max_try == 0:
            self.check_url(self.start_page)
            max_try = max_try - 1
        try:
            login_input_wait = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.login_input)))
            pass_input_wait = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.password_input)))
            auth_btn_wait = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.authorize_btn)))
            login_input_wait.send_keys(self.login_str)
            pass_input_wait.send_keys(self.password_str)
            auth_btn_wait.click()
        except NoSuchElementException:
            pass
        except TimeoutException:
            pass

    def subscribe(self, links):
        for link in links:
            link = "https://twitter.com" + link
            while not self.check_url(link):
                self.check_url(link)
            try:
                while WebDriverWait(self.driver, 3).until(
                        EC.visibility_of_element_located(
                            (By.XPATH, "/html/body/div/div/div/div[1]/div/div[1]/div/div"))):
                    self.driver.refresh()
            except TimeoutException:
                try:
                    subscribe_button_wait = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, self.subscribe_button)))
                    subscribe_button_option = self.driver.find_element_by_xpath(
                        '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div[4]/div/div').get_attribute(
                        "data-testid").split('-')
                    if subscribe_button_option[1] == 'follow':
                        self.driver.find_element_by_xpath(self.subscribe_button).click()
                except TimeoutException:
                    print('Не удалось прожать подписку')

    def like_rt(self, url):
        while not self.check_url(url):
            self.check_url(url)
        try:
            while WebDriverWait(self.driver, 3).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "/html/body/div/div/div/div[1]/div/div[1]/div/div"))):
                self.driver.refresh()
        except TimeoutException:
            try:
                like_btn_wait = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.like)))
                rt_btn_wait = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.retweet)))
                like_btn_wait.click()
                rt_btn_wait.click()
                rt_confirm_btn_wait = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.retweet_confirm)))
                rt_confirm_btn_wait.click()
            except NoSuchElementException:
                print("Лайк не поставлен")


start = Forgotten_script('https://twitter.com/torpedoAIO/status/1411769304048091142', 'qawsedrftgy1973@', '89955086949',
                         'off', 'off')
test = start.scrapping_tweet('https://twitter.com/torpedoAIO/status/1411769304048091142')
start.login()
start.like_rt('https://twitter.com/torpedoAIO/status/1411769304048091142')
start.subscribe(test)
