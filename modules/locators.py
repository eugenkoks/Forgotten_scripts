from selenium import webdriver

login_div = '/html/body/div/div/div/div[2]/main/div/div'
login_input = '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
password_input = '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
authorize_btn = '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div'
news_page_div = '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div'
wrond_pass_div = '/html/body/div/div/div/div[2]/main/div/div/div[1]/div'
tweet_page = '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/article/div/div/div/div[3]/div[1]/div/div[1]'
tweet_id_locator = '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div/div/div[1]/article/div/div/div/div[3]/div[1]/div/div[1]'
like = '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div[1]/article/div/div/div/div[3]/div[5]/div/div[3]/div'
retweet = '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div[1]/article/div/div/div/div[3]/div[5]/div/div[2]/div'
retweet_confirm = '/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[3]/div/div/div/div'
subscribe_button = '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div[3]'
start_page = 'https://twitter.com/login'

headless_options = webdriver.ChromeOptions()
headless_options.add_argument('--ignore-certificate-errors')
headless_options.add_argument('--incognito')
headless_options.add_argument("javascript.enabled")
headless_options.add_argument('--disable-gpu')
headless_options.add_argument('--no-sandbox')
headless_options.add_argument('--disable-dev-shm-usage')
headless_options.add_argument('--headless')
headless_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.123 Safari/537.36")
normal_options = webdriver.ChromeOptions()
normal_options.add_argument('--ignore-certificate-errors')
normal_options.add_argument('--incognito')
normal_options.add_argument('javascript.enabled')
normal_options.add_argument('--disable-gpu')
normal_options.add_argument('--no-sandbox')
normal_options.add_argument('--disable-dev-shm-usage')
normal_options.add_argument('--window-size=800,900')
normal_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.123 Safari/537.36")