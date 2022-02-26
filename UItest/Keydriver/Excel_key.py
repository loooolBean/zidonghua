from time import sleep

from selenium import webdriver


def browsers(type_):
    try:
        driver = getattr(webdriver, type_)()    # 获取对象webdriver里的type_属性，如果有，就运行
    except:
        driver = webdriver.Chrome()
    return driver


class WebDemo:
    def __init__(self, type_):
        self.driver = browsers(type_)

    def open_url(self, **kwargs):
        self.driver.get(kwargs['txt'])

    def locator(self, **kwargs):
        return self.driver.find_element(kwargs['name'], kwargs['value'])

    def input(self, **kwargs):
        self.locator(**kwargs).send_keys(kwargs['txt'])

    def click(self, **kwargs):
        self.locator(**kwargs).click()

    def wait(self, **kwargs):
        sleep(kwargs['txt'])

    def quit(self,**kwargs):
        self.driver.quit()
