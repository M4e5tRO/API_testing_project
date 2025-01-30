import requests
import allure

from .base_endpoint import BaseEndpoint


class GetAuthToken(BaseEndpoint):

    def get_auth_token(self, token=None, headers=None):
        with allure.step("Check the token's status"):
            self.token = token if token else self.headers.auth_headers['Authorization']
            self.headers = headers if headers else self.headers.def_headers

            self.response = requests.get(
                url=f'{self.auth_url}/{self.token}',
                headers=self.headers
            )

            return self.response

    @allure.step('Check the authorization response message')
    def check_auth_response_message(self):
        assert self.response.text == self.auth_payloads.auth_message, 'Message is incorrect'

    @allure.step("404 Auth Error - Not Found")
    def check_auth_404_page(self):
        assert self.response.status_code == 404, f'Status code {self.response.status_code} is incorrect'
        html = self.response.text
        self.attach_html(html)
        assert self.auth_payloads.title_404_auth in html, 'The title of the error page is incorrect'
        assert self.auth_payloads.header_404_auth in html, 'The header of the error page is incorrect'
        assert self.auth_payloads.message_404_auth in html, 'The error message content is incorrect'
