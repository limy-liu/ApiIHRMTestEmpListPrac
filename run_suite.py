import unittest

# 实例化测试套件对象
import time

from app import BASE_DIR
from script.test_emp import TestEmp
from script.test_login import TestLogin
from tools.HTMLTestRunner_sq import HTMLTestRunner

suite = unittest.TestSuite()
# 向测试套件添加测试用例
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestEmp))

# report_path = BASE_DIR + '/report/ihrm{}.html'.format(time.strftime('%Y%m%d-%H%M%S'))
report_path = BASE_DIR + '/report/ihrm.html'
with open(report_path, 'wb') as f:
    runner = HTMLTestRunner(stream=f,
                            verbosity=2,
                            title='IHRM接口自动化测试报告',
                            description='V1.0.0')
    runner.run(suite)