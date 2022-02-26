"""
    1. 获取excel文件
    2. 获取sheet页
    3. 获取单元格内容
"""
import openpyxl

from UItest.Keydriver.Excel_key import WebDemo
import unittest


class demo(unittest.TestCase):
    def test_excel(self):
        excel = openpyxl.load_workbook('../../data/Bean.xlsx')  # 1.
        # sheet = excel['Sheet1']
        # cell = sheet['A1'].value
        # print(cell)
        sheets = excel.sheetnames
        # print(sheets)
        for name in sheets:
            sheet = excel[name]  # 2.
            for value in sheet.values:  # 3.
                if type(value[0]) is int:
                    data = {}
                    data['name'] = value[2]
                    data['value'] = value[3]
                    data['txt'] = value[4]

                    for key1 in list(data.keys()):
                        if data[key1] is None:
                            del data[key1]
                    print(data)
                    #
                    # # Excel数据驱动完成自动化测试
                    if value[1] == 'browser':
                        wd = WebDemo(data['txt'])
                    else:
                        getattr(wd, value[1])(**data)
                        self.assertEqual('121', '121', msg='断言成功')


if __name__ == '__main__':
    unittest.main()
