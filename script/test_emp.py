import unittest
import logging
import utils
from api.ihrm_emp_api import IHRMEmpApi
from parameterized import parameterized


class TestEmp(unittest.TestCase):
    """员工测试用例类"""

    @classmethod
    def setUpClass(cls):
        cls.ihrm_emp_api = IHRMEmpApi()

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @parameterized.expand(utils.read_emp_data)
    def test_emp_list(self, page, size, http_code, code, success, message):
        # for i in range(1, 3):
        #     response = self.ihrm_emp_api.emp_list(i, 10)
        #     jsonData = response.json()
        #     logging.info("获取员工列表接口返回的数据为：{}".format(jsonData))
        #     utils.assert_common(self, response, 200, 10000, True, '操作成功')
        #
        #     # 断言第一页默认条数是否是10
        #     list1 = jsonData.get('data').get('rows')
        #     logging.info('第{}页返回的数据条数为：{}'.format(i, len(list1)))
        #     self.assertEqual(10, len(list1))

        response = self.ihrm_emp_api.emp_list(page, size)
        jsonData = response.json()
        logging.info("获取员工列表接口返回的数据为：{}".format(jsonData))
        utils.assert_common(self, response, http_code, code, success, message)

        while size != 0:
            # 断言默认条数是否是10
            list1 = jsonData.get('data').get('rows')
            logging.info('第{}页返回的数据条数为：{}'.format(page, len(list1)))
            self.assertEqual(size, len(list1))
            break

        # 断言第一页手机号13800000002的username是否是aj123
        while page == 1 and size == 10:
            list2 = jsonData.get('data').get('rows')
            for i in list2:
                mobile = i.get('mobile')
                username = i.get('username')
                if mobile == '13800000002':
                    logging.info("mobile：{}".format(mobile))
                    id1 = i.get('id')
                    logging.info("打印id：{}".format(i.get('id')))
                    if username == "aj123":
                        logging.info("username：{}".format(username))
                        logging.info("打印id：{}".format(i.get('id')))
                        id2 = i.get('id')
            self.assertEqual(id1, id2)
            break


if __name__ == '__main__':
    unittest.main()





