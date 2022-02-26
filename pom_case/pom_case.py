import unittest
from time import sleep

from ddt import ddt, file_data
from selenium import webdriver

from pom_base.key import Key

from selenium.webdriver.common.by import By

from pom_object.pom_object import Object

@ddt
class Case(unittest.TestCase):

    @file_data('../data/pom_data.yaml')
    def test_login(self, usr, pwd):
        driver = webdriver.Chrome()
        lg = Object(driver)
        lg.login(usr, pwd)
        sleep(5)


if __name__ == '__main__':
    unittest.main()
