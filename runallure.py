import os

import pytest

if __name__ == '__main__':
    # 执行测试用例获得测试数据 数据的目录
    pytest.main(['-s', './pom_case/test_pytest.py', '--alluredir', './allure-results'])
    # 生成测试报告 找到测试数据 生成测试报告的目录
    # ./allure-results是测试数据目录 ./reports是测试报告目录
    os.system('allure generate ./allure-results -o ./reports')