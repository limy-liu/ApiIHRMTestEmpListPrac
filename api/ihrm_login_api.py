import requests

import app


class IHRMLoginApi:
    """人力资源管理系统登录接口类"""

    def __init__(self):
        self.ihrm_login_url = app.HOST + '/api/sys/login'
        self.headers = app.HEADERS

    def login_api(self, mobile, password):
        """请求ihrm登录方法"""
        data = {"mobile": mobile, "password": password}
        response = requests.post(self.ihrm_login_url, headers=self.headers, json=data)
        return response
