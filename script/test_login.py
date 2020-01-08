import unittest
import logging
import app
import utils
from api.ihrm_login_api import IHRMLoginApi
from parameterized import parameterized


class TestLogin(unittest.TestCase):
    """ihrm登录测试用例类"""

    @classmethod
    def setUpClass(cls):
        cls.ihrm_login_api = IHRMLoginApi()

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @parameterized.expand(utils.read_login_data)
    def test_login(self, mobile, password, message, http_code, code, success):
        response = self.ihrm_login_api.login_api(mobile, password)
        jsonData = response.json()
        logging.info('登录返回的json数据为：{}'.format(jsonData))

        # 获取token令牌
        token = jsonData.get('data')
        app.HEADERS['Authorization'] = 'Bearer ' + token

        # 断言
        utils.assert_common(self, response, http_code, code, success, message)


if __name__ == '__main__':
    unittest.main()
