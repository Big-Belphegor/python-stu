__author__ = "Alien"
import unittest                                 # python自带的测试模块
from name_function import get_formatted_name    # 导入要测试的模块/函数

class Testname(unittest.TestCase):          # 任意定义一个类，但必须继承unittest.TestCase
    '''测试name_function.py'''

    def test_first_last_name(self):             # 类内只需要创建一个方法，此方法必须以test开头
        formatted_name = get_formatted_name('Alien','Lee')      # 将要测试的函数运行并将结果输出到formatted_name变量中
        self.assertEqual(formatted_name,'Alien Lee ff')         # 利用self.assertEqual判断formatted_name的值是否和预期的值匹配

unittest.main()                                 # 运行本文件中的测试部分代码