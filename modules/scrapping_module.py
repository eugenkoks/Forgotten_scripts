from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from locators import *


def scrapping_tweet(url):
    driver = webdriver.Chrome(options=headless_options)
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, tweet_page)))
    tweet_id = driver.find_element_by_xpath(tweet_id_locator).get_attribute('id')
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


if __name__ == '__main__':
    if scrapping_tweet('https://twitter.com/KeithAdam10/status/1432822520248479751') == ['/Gargantua_AIO', '/NSB_Bot', '/Ecnarudne1', '/Gargantua_AIO', '/NSB_Bot', '/Ecnarudne1']:
        print('OK')
    else:
        print("BAD")