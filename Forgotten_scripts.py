import os
import pickle
import time
import random

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
        self.like = '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div[1]/article/div/div/div/div[3]/div[5]/div/div[3]/div'
        self.retweet = '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div[1]/article/div/div/div/div[3]/div[5]/div/div[2]/div'
        self.retweet_confirm = '/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[3]/div/div/div/div'
        self.subscribe_button = '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div[3]'
        self.start_page = 'https://twitter.com/login'
        self.headless_options = webdriver.ChromeOptions()
        self.headless_options.add_argument('--ignore-certificate-errors')
        self.headless_options.add_argument('--incognito')
        self.headless_options.add_argument("javascript.enabled")
        self.headless_options.add_argument('--disable-gpu')
        self.headless_options.add_argument('--no-sandbox')
        self.headless_options.add_argument('--disable-dev-shm-usage')
        self.headless_options.add_argument('--headless')
        self.headless_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.123 Safari/537.36")
        self.normal_options = webdriver.ChromeOptions()
        self.normal_options.add_argument('--ignore-certificate-errors')
        self.normal_options.add_argument('--incognito')
        self.normal_options.add_argument('javascript.enabled')
        self.normal_options.add_argument('--disable-gpu')
        self.normal_options.add_argument('--no-sandbox')
        self.normal_options.add_argument('--disable-dev-shm-usage')
        self.normal_options.add_argument('--window-size=800,900')
        self.normal_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.123 Safari/537.36")
        if tag == 'on':
            self.tag = True
        else:
            self.tag = False

    def scrapping_tweet(self, url):
        driver = webdriver.Chrome(options=self.headless_options)
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, self.tweet_page)))
        tweet_id = driver.find_element_by_xpath(self.tweet_id).get_attribute('id')
        html = driver.page_source
        soup = BeautifulSoup(html, "lxml")
        all_link = soup.find(id=tweet_id).find_all('a')
        links = []
        for link in all_link:
            if link.get('href').split('/')[1] == 'hashtag':
                continue
            else:
                links.append(link.get('href'))
        print(links)
        driver.quit()
        return links

    def login(self):
        driver = webdriver.Chrome(options=self.normal_options)
        driver.get(self.start_page)
        time.sleep(random.randint(3, 5))
        try:
            login_input_wait = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.login_input)))
            pass_input_wait = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.password_input)))
            auth_btn_wait = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.authorize_btn)))
            login_input_wait.send_keys(self.login_str)
            pass_input_wait.send_keys(self.password_str)
            auth_btn_wait.click()
        except NoSuchElementException:
            print('NoSuchElementException')
        except TimeoutException:
            print('TimeoutException')
        cookies = driver.get_cookies()
        print("Успешная авторизация")
        driver.quit()
        return cookies

    def like_rt(self, cookies, tag):
        driver = webdriver.Chrome(options=self.normal_options)
        driver.get(self.url)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
        time.sleep(random.randint(3, 5))
        like_btn_wait = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.like)))
        rt_btn_wait = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.retweet)))
        like_btn_wait.click()
        rt_btn_wait.click()
        rt_confirm_btn_wait = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.retweet_confirm)))
        rt_confirm_btn_wait.click()
        driver.quit()
        if tag:
            driver = webdriver.Chrome(options=self.normal_options)
            driver.get(self.url)
            for cookie in cookies:
                driver.add_cookie(cookie)
            driver.refresh()
            time.sleep(random.randint(3, 5))
            driver.find_element_by_xpath("//div[@data-testid='reply'][@role='button']").click()
            time.sleep(3)
            tag_name = 'johpohan'
            driver.find_element_by_xpath("//div[@data-testid='tweetTextarea_0'][@role='textbox']").send_keys(f"@{tag_name} ")
            time.sleep(3)
            driver.find_element_by_xpath("//div[@data-testid='tweetButton'][@role='button']").click()
            print('Тэгнул.')
            time.sleep(3)
            driver.quit()
        else:
            pass

    def subscribe(self, links, cookies):
        driver = webdriver.Chrome(options=self.normal_options)
        for link in links:
            link = "https://twitter.com" + link
            driver.get(link)
            for cookie in cookies:
                driver.add_cookie(cookie)
            driver.refresh()
            time.sleep(random.randint(3, 5))
            subscribe_button_wait = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.subscribe_button)))
            subscribe_button_option = driver.find_element_by_xpath(
                '//div[@data-testid="placementTracking"]/div/div').get_attribute(
                "data-testid").split('-')
            if subscribe_button_option[1] == 'follow':
                driver.find_element_by_xpath(self.subscribe_button).click()
        driver.quit()

    def main(self):
        links = self.scrapping_tweet(self.url)
        cookies = self.login()
        self.like_rt(cookies, self.tag)
        self.subscribe(links, cookies)


eel.init("web")


@eel.expose
def url_print(url, headless, tag, only_lk_rt):
    start = Forgotten_script(url, 'qawsedrftgy1973@', '89955086949', tag, headless)
    start.main()


eel.start("main.html", size=(500, 260), port=0)
