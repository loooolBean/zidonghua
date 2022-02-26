from time import sleep

from selenium import webdriver


#
# def open_browser(type_):
#     try:
#         driver = getattr(webdriver, type_)()
#     except Exception as e:
#         print(e)
#         driver = webdriver.Chrome()
#     return driver


class Key:

    # 构造函数
    # 这里建议直接传driver，不写browser方式，因为会报错
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, txt):
        self.driver.get(txt)

    def locator(self, loc):
        return self.driver.find_element(*loc)

    def input(self, loc, txt):
        self.locator(loc).send_keys(txt)

    def click(self, loc):
        self.locator(loc).click()

    def wait(self, txt):
        sleep(txt)

    def quit(self):
        self.driver.quit()
