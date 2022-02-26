"""

    利用yaml数据驱动
"""
import unittest

from ddt import ddt, file_data

from UItest.Keydriver.UnitTest_key import Key
from selenium import webdriver


@ddt
class UnitDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.key = Key()

    @file_data('../../data/Test_data.yaml')
    def test_serarch01(self, url, txt, expect):
        self.key.open_url(url)
        self.key.input('id', 'kw', txt)
        self.key.click('id', 'su')
        self.key.wait(5)
        self.key.quit()
        self.assertEqual('121', '121', msg=expect)


if __name__ == '__main__':
    unittest.main()
