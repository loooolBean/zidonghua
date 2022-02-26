from time import sleep

from selenium import webdriver


def open_browser(type_):
    try:
        driver = getattr(webdriver, type_)()
    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
    return driver


class Key:
    driver = webdriver.Chrome()

    # 构造函数
    # def __init__(self, type_):
    #     self.driver = open_browser(type_)

    def open_url(self, txt):
        self.driver.get(txt)

    def locator(self, name, value):
        return self.driver.find_element(name, value)

    def input(self, name, value, txt):
        self.locator(name, value).send_keys(txt)

    def click(self, name, value):
        self.locator(name, value).click()

    def wait(self, txt):
        sleep(txt)

    def quit(self):
        self.driver.quit()
