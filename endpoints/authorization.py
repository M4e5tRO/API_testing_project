import requests
import allure

from .base_endpoint import BaseEndpoint
from .json_schemas import AuthScheme


class Authorization(BaseEndpoint):


    def authorize(self, payload=None, headers=None):
        with allure.step('Authorize the user'):
            self.payload = payload if payload else self.auth_payloads.valid_credentials
            self.headers = headers if headers else self.headers.def_headers
            self.attach_payload(self.payload)

            self.response = requests.post(
                url=self.auth_url,
                json=self.payload,
                headers=self.headers
            )
            if self.response.status_code == 200:
                self.json = self.response.json()
                self.attach_response(self.json)
                self.model = AuthScheme(**self.json)
                self.token = self.model.token
                self.user = self.model.user
                return self.model

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
