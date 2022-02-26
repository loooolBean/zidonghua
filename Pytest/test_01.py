import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


# parmetrize参数化使用
@pytest.mark.parametrize('user, pw, expected',
                         [('18819035643', 'liao13560884795', '验证成功'),
                          ('xuzhu1233', '12345', '验证失败'),
                          ('xuzhu1233', '2345', '验证成功')],
                         ids=['case1', 'case2', 'case3']
                         )
def test_login(user, pw, expected):
    driver = webdriver.Chrome()
    url = 'https://login.dangdang.com/?returnurl=http%3A%2F%2Fbook.dangdang.com%2F20210317_x0d2'
    driver.get(url)
    driver.find_element(By.XPATH, '//div[@class ="l"]/input[@type="text"]').send_keys(user)
    driver.find_element(By.XPATH, '//div[@class ="l"]/input[@type="password"]').send_keys(pw)
    driver.find_element(By.XPATH, '//a[@class="btn"]').click()
    sleep(5)
    assert driver.title == expected


if __name__ == '__main__':
    pytest.main(['-s', 'test_01.py'])
