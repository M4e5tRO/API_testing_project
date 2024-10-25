import requests
import allure

from .base_endpoint import BaseEndpoint
from .json_schemas import AuthScheme
from ..test_data import payloads_list, headers_list


class Authorization(BaseEndpoint):

    @allure.step("User's Authorization")
    def authorize(self, payload=None, headers=None):
        self.payload = payload if payload else payloads_list.valid_credentials
        self.headers = headers if headers else headers_list.def_headers

        self.response = requests.post(
            self.auth_url,
            json=self.payload,
            headers=self.headers
        )
        if self.response.status_code == 200:
            self.json = AuthScheme(**self.response.json())
            self.token = self.json.token
            self.user = self.json.user

        return self.response

    @allure.step("Check token")
    def check_token(self):
        if not self.token:
            allure.attach('Token Check', 'The "token" is NOT created', allure.attachment_type.TEXT)
            raise ValueError('The "token" is NOT created')
        else:
            allure.attach('Token Check', f'The token is valid: {self.token}', allure.attachment_type.TEXT)

    @allure.step("Check name")
    def check_name(self, name):
        assert self.user == name, f'The payload: "{name}" does NOT matched with the response: "{self.user}"'
