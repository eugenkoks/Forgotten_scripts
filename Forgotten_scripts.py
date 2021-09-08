import modules.login_module
import modules.scrapping_module
import modules.like_rt_tag_module
import modules.subscribe_module
import eel


class Forgotten_script:
    def __init__(self, url, tag, headless, like, retweet):
        self.url = url
        self.tag = tag
        self.like = like
        self.retweet = retweet
        self.headless = headless
        if tag == 'on':
            self.tag = True
        else:
            self.tag = False

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
            modules.like_rt_tag_module.like_rt_tag(self.url, self.headless, cookies, self.like, self.retweet, self.tag)
            modules.subscribe_module.subscribe(links, cookies, self.headless)


eel.init("web")


@eel.expose
def url_print(url, headless, tag, like, retweet):
    start = Forgotten_script(url, tag, headless, like, retweet)
    start.main()


eel.start("main.html", size=(500, 300), port=0)
