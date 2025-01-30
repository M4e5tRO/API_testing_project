import allure

from ..test_data.headers_list import Headers
from ..test_data.auth_payloads import AuthPayloads
from ..test_data.base_payloads import BasePayloads
from ..utils.helper import Helper


class BaseEndpoint(Helper):

    model = None
    payload = None
    response = None
    token = None
    json = None

    def __init__(self):
        self.base_url = 'http://167.172.172.115:52355'
        self.auth_url = f'{self.base_url}/authorize'
        self.url = f'{self.base_url}/meme'
        self.headers = Headers()
        self.auth_payloads = AuthPayloads()
        self.base_payloads = BasePayloads()

    @allure.step('Check the response status code - 200 OK')
    def check_response_code_is_200(self):
        assert self.response.status_code == 200, (f'Status Code:{self.response.status_code},\n\n'
                                                  f'JSON: {self.response.json()}')

    @allure.step('Check the response status code - 400 Bad Request')
    def check_response_code_is_400(self):
        assert self.response.status_code == 400, (f'Status Code:{self.response.status_code},\n\n'
                                                  f'JSON: {self.response.json()}')

    @allure.step('Check the response status code - 401 Unauthorized')
    def check_response_code_is_401(self):
        assert self.response.status_code == 401, (f'Status Code:{self.response.status_code},\n\n'
                                                  f'JSON: {self.response.json()}')

    @allure.step('Check the response status code - 403 Forbidden')
    def check_response_code_is_403(self):
        assert self.response.status_code == 403, (f'Status Code:{self.response.status_code},\n\n'
                                                  f'JSON: {self.response.json()}')

    @allure.step('Check the response status code - 404 Not Found')
    def check_response_code_is_404(self):
        assert self.response.status_code == 404, (f'Status Code:{self.response.status_code},\n\n'
                                                  f'JSON: {self.response.json()}')

    @allure.step("Check if Payload is a subset of the Response JSON")
    def if_payload_is_a_subset_of_response(self):
        yield self.is_subset(self.payload, self.json)
        print(f'The values of the keys: [{self.payload.keys()}] are verified')

    @allure.step('Verify a value of the "updated_by" key in the response')
    def check_value_of_updated_by(self):
        payload_auth_name=self.auth_payloads.valid_credentials['name']
        allure.attach('Payload', f'"name": "{payload_auth_name}"', allure.attachment_type.TEXT)
        resp_updated_by = self.json['updated_by']
        allure.attach('Response', f'"updated_by": "{resp_updated_by}"', allure.attachment_type.TEXT)
        assert payload_auth_name == resp_updated_by, (
            f'The payload: "{payload_auth_name}" does NOT matched with the response: "{resp_updated_by}"'
        )

    @allure.step("Check the HTML page - 400 Bad Request")
    def check_400_page(self):
        html = self.response.text
        self.attach_html(html)
        assert self.base_payloads.title_400 in html, 'The title of the error page is incorrect'
        assert self.base_payloads.header_400 in html, 'The header of the error page is incorrect'
        assert self.base_payloads.message_400 in html, 'The error message content is incorrect'

    @allure.step("Check the HTML page - 401 Unauthorized")
    def check_401_page(self):
        html = self.response.text
        self.attach_html(html)
        assert self.base_payloads.title_401 in html, 'The title of the error page is incorrect'
        assert self.base_payloads.header_401 in html, 'The header of the error page is incorrect'
        assert self.base_payloads.message_401 in html, 'The error message content is incorrect'

    @allure.step("Check the HTML page - 403 Forbidden")
    def check_403_page(self):
        html = self.response.text
        self.attach_html(html)
        assert self.base_payloads.title_403 in html, 'The title of the error page is incorrect'
        assert self.base_payloads.header_403 in html, 'The header of the error page is incorrect'
        assert self.base_payloads.message_403 in html, 'The error message content is incorrect'

    @allure.step("Check the HTML page - 404 Not Found")
    def check_404_page(self):
        html = self.response.text
        self.attach_html(html)
        assert self.base_payloads.title_404 in html, 'The title of the error page is incorrect'
        assert self.base_payloads.header_404 in html, 'The header of the error page is incorrect'
        assert self.base_payloads.message_404 in html, 'The error message content is incorrect'
