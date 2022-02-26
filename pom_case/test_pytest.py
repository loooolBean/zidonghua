import pytest
from time import sleep

from ddt import ddt, file_data
from selenium import webdriver

from pom_base.key import Key

from selenium.webdriver.common.by import By

from pom_object.pom_object import Object
from config.yamlload import loadyaml


class TestCase():

    @pytest.mark.parametrize('data', loadyaml('../data/pom_data.yaml'))
    def test_login(self, data):
        self.driver = webdriver.Chrome()
        self.lg = Object(self.driver)
        self.lg.login(data['usr'], data['pwd'])
        sleep(5)
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(['-s', '/test_pytest.py'])
