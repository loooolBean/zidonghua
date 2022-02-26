from ddt import ddt, file_data
from selenium import webdriver

from pom_base.key import Key

from selenium.webdriver.common.by import By


class Object(Key):
    url = 'https://login.dangdang.com/?returnurl=http%3A%2F%2Fwww.dangdang.com%2F'
    user = (By.XPATH, '//div[@class ="l"]/input[@type="text"]')
    password = (By.XPATH, '//div[@class ="l"]/input[@type="password"]')
    btn = (By.XPATH, '//a[@class="btn"]')

    def login(self, usr, pwd):
        self.open_url(self.url)
        self.wait(2)
        self.input(self.user, usr)
        self.input(self.password, pwd)
        self.click(self.btn)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    lp = Object(driver)
    usr1 = '18819035643'
    pwd1 = 'liao13560884795'
    lp.login(usr1, pwd1)
