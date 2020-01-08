# 封装断言函数
import json

from app import BASE_DIR


def assert_common(self, response, http_code, code, success, message):
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(code, response.json().get('code'))
    self.assertEqual(success, response.json().get('success'))
    self.assertIn(message, response.json().get('message'))


# 读取json数据封装函数方法
def read_login_data():
    path = BASE_DIR + '/data/login_data.json'
    with open(path, "r", encoding='utf-8') as f:
        jsonData = json.load(f)
        data_list = list()
        data_list.append((jsonData.get('mobile'),
                          jsonData.get('password'),
                          jsonData.get('message'),
                          jsonData.get('code'),
                          jsonData.get('http_code'),
                          jsonData.get('success')))
    print(data_list)
    return data_list


def read_emp_data():
    path = BASE_DIR + '/data/emp_data.json'
    with open(path, 'r', encoding='utf-8') as f:
        jsonData = json.load(f)
        data_list = list()
        for i in jsonData:
            data_list.append((i.get('page'),
                              i.get('size'),
                              i.get('http_code'),
                              i.get('code'),
                              i.get('success'),
                              i.get('message')))
    print(data_list)
    return data_list


if __name__ == '__main__':
    read_emp_data()
