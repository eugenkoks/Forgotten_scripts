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
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

accounts = []
with open("accs.txt") as file:
    for line in file:
        accounts.append(line)


    class Task_body:

    def __init__(self, url, headless, tag):
        self.url = url
        self.headless = headless
        self.tag = tag
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        options.add_argument("javascript.enabled")
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.123 Safari/537.36")
        if headless == 'on':
            options.add_argument("--headless")
        else:
            options.add_argument("--window-size=800,900")
        self.driver = webdriver.Chrome(options=options)

    def scrapping(self):
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                             '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/article/div/div/div/div[3]/div[1]/div/div[1]')))
        tweet_id = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/article/div/div/div/div[3]/div[1]/div/div[1]').get_attribute(
            'id')
        html = self.driver.page_source
        soup = BeautifulSoup(html, "lxml")
        all_link = soup.find(id=tweet_id).find_all("a")
        links = []
        for i in all_link:
            if i.get('href').split('/')[1] == "hashtag":
                pass
            else:
                links.append(i.get('href'))
        print(links)
        return links

    def login(self, login_int, pass_int):
        self.driver.get('https://twitter.com/login')
        if self.driver.current_url == "https://twitter.com/i/flow/login":
            self.driver.get('https://twitter.com/login')
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/h1/span')))
        self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input').send_keys(
            login_int)
        self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input').send_keys(
            pass_int)
        # time.sleep(2)
        self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div').click()
        time.sleep(2)
        pickle.dump(self.driver.get_cookies(), open(f"{login_int}.pkl", "wb"))
        cookies = pickle.load(open(f"{login_int}.pkl", "rb"))
        return cookies

    def subscribe(self, links, cookies):
        for link in links:
            self.driver.get(f"https://twitter.com{link}")
            # for cookie in cookies:
            #     self.driver.add_cookie(cookie)
            #     time.sleep(2)
            self.driver.refresh()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                 '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div[3]')))
            subscribe_button = self.driver.find_element_by_xpath(
                '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div[4]/div/div').get_attribute(
                "data-testid").split('-')
            if subscribe_button[1] == 'follow':
                self.driver.find_element_by_xpath(
                    '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[1]/div/div[3]/div/div').click()
                if subscribe_button[1] == "unfollow":
                    print("Подписка оформлена")
                else:
                    print('Подписка не оформлена')

        time.sleep(1)

    def like_rt_tag(self, cookies):
        self.driver.get(self.url)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        try:
            self.driver.find_element_by_xpath(
                '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div[1]/article/div/div/div/div[3]/div[5]/div[3]/div').click()
            self.driver.find_element_by_xpath(
                '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div[1]/article/div/div/div/div[3]/div[5]/div[2]/div').click()
            time.sleep(0.5)
            self.driver.find_element_by_xpath(
                '/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[3]/div/div/div/div').click()
        except NoSuchElementException:
            print("Лайк не поставлен")
        pass


eel.init("web")


@eel.expose
def url_print(url, headless, tag):
    pr = Task_body(url, headless, tag)
    links = pr.scrapping()
    for account in accounts:
        pr.driver.delete_all_cookies()
        pr.driver.refresh()
        log_pass = account.split(":")
        cookie = pr.login(log_pass[0], log_pass[1])
        pr.subscribe(links, cookie)
        # pr.like_rt_tag(cookie)
    pr.driver.quit()


eel.start("main.html", size=(500, 220), port=0)
