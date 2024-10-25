import requests
import allure

from .base_endpoint import BaseEndpoint
from ..test_data import headers_list, payloads_list


class GetAuthToken(BaseEndpoint):

    @allure.step("Check the token's status")
    def get_auth_token(self, token=None, headers=None):
        self.token = token if token else headers_list.auth_headers['Authorization']
        self.headers = headers if headers else headers_list.def_headers

        self.response = requests.get(
            f'{self.auth_url}/{self.token}',
            headers=self.headers
        )

        return self.response

    @allure.step('Check the authorization response message')
    def check_auth_response_message(self):
        assert self.response.text == f"Token is alive. Username is {payloads_list.valid_credentials['name']}",\
                                     'Message is incorrect'

    def _check_auth_404_error(self):
        expected_html_title = '<title>404 Not Found</title>'
        expected_html_header = '<h1>Not Found</h1>'
        expected_html_message = '<p>Token not found</p>'

        assert self.response.status_code == 404, f'Status code {self.response.status_code} is incorrect'
        assert expected_html_title in self.response.text, 'The title of the error page is incorrect'
        assert expected_html_header in self.response.text, 'The header of the error page is incorrect'
        assert expected_html_message in self.response.text, 'The error message content is incorrect'

    @allure.step("404 Auth Error - Not Found")
    def check_auth_404_page(self):
        self._check_auth_404_error()
