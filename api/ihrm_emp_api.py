import requests

import app


class IHRMEmpApi:
    def __init__(self):
        self.emp_list_url = app.HOST + '/api/sys/user'
        self.headers = app.HEADERS

    def emp_list(self, page, size):
        data = {"page": page, "size": size}
        response = requests.get(self.emp_list_url, headers=self.headers, params=data)
        return response
