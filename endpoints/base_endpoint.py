import allure

from ..test_data import headers_list


class BaseEndpoint:

    id = None
    description = None
    policy = None
    info = None
    tags = None
    text = None
    updated_by = None
    all_memes = None
    payload = None
    headers = None
    response = None
    json = None
    token = None
    user = None

    def __init__(self):
        self.base_url = 'http://167.172.172.115:52355'
        self.auth_url = f'{self.base_url}/authorize'
        self.url = f'{self.base_url}/meme'
        self.def_headers = headers_list.def_headers
        self.auth_headers = headers_list.auth_headers

    @allure.step('Check the response code - 200 OK')
    def check_response_code_is_200(self):
        assert self.response.status_code == 200, f'The Response status code is {self.response.status_code}'

    @allure.step('Check the response code - 400 Bad Request')
    def check_response_code_is_400(self):
        assert self.response.status_code == 400, f'The Response status code is {self.response.status_code}'

    @allure.step('Check the response code - 401 Unauthorized')
    def check_response_code_is_401(self):
        assert self.response.status_code == 401, f'The Response status code is {self.response.status_code}'

    @allure.step('Check the response code - 403 Forbidden')
    def check_response_code_is_403(self):
        assert self.response.status_code == 403, f'The Response status code is {self.response.status_code}'

    @allure.step('Check the response code - 404 Not Found')
    def check_response_code_is_404(self):
        assert self.response.status_code == 404, f'The Response status code is {self.response.status_code}'

    @allure.step('Match optional Key-Value pair in the response & payload')
    def check_json(self, key, value):
        assert self.json[key] == value

    @allure.step('Match the "description" in the response & payload')
    def check_description(self, description):
        assert self.description == description, (f'The payload: "{description}" does NOT matched with the response:'
                                                 f' "{self.description}"')

    @allure.step('Match the "policy" in the response & payload')
    def check_policy(self, policy):
        assert self.policy == policy, f'The payload: "{policy}" does NOT matched with the response: "{self.policy}"'

    @allure.step('Match TAGs in the response & payload')
    def check_tags(self, tags):
        set_resp_tags = set(self.json.tags)
        set_tags = set(tags)
        assert set_resp_tags == set_tags, (f'The payload: "{set_tags}" do NOT matched with the response: '
                                           f'"{set_resp_tags}"')

    @allure.step('Match the "text" in the response & payload')
    def check_text(self, text):
        assert self.text == text, f'The payload: "{text}" does NOT matched with the response: "{self.text}"'

    @allure.step('Match the "updated_by" in the response & payload')
    def check_updated_by(self, updated_by):
        assert self.updated_by == updated_by, (f'The payload: "{updated_by}" does NOT matched with the response:'
                                               f' "{self.updated_by}"')

    @allure.step('Match the "url" in the response & payload')
    def check_url(self, url):
        assert self.url == url, f'The payload: "{url}" does NOT matched with the response: "{self.url}"'

    def _check_common_400_error(self):
        expected_html_title = '<title>400 Bad Request</title>'
        expected_html_header = '<h1>Bad Request</h1>'
        expected_html_message = '<p>Invalid parameters</p>'

        assert expected_html_title in self.response.text, 'The title of the error page is incorrect'
        assert expected_html_header in self.response.text, 'The header of the error page is incorrect'
        assert expected_html_message in self.response.text, 'The error message content is incorrect'

    @allure.step("400 Error - Bad Request")
    def check_400_page(self):
        self._check_common_400_error()

    def _check_common_401_error(self):
        expected_html_title = '<title>401 Unauthorized</title>'
        expected_html_header = '<h1>Unauthorized</h1>'
        expected_html_message = '<p>Not authorized</p>'

        assert expected_html_title in self.response.text, 'The title of the error page is incorrect'
        assert expected_html_header in self.response.text, 'The header of the error page is incorrect'
        assert expected_html_message in self.response.text, 'The error message content is incorrect'

    @allure.step("401 Error - Unauthorized")
    def check_401_page(self):
        self._check_common_401_error()

    def _check_common_403_error(self):
        expected_html_title = '<title>403 Forbidden</title>'
        expected_html_header = '<h1>Forbidden</h1>'
        expected_html_message = '<p>You are not the meme owner</p>'

        assert expected_html_title in self.response.text, 'The title of the error page is incorrect'
        assert expected_html_header in self.response.text, 'The header of the error page is incorrect'
        assert expected_html_message in self.response.text, 'The error message content is incorrect'

    @allure.step("403 Error - Forbidden")
    def check_403_page(self):
        self._check_common_403_error()

    def _check_common_404_error(self):
        expected_html_title = '<title>404 Not Found</title>'
        expected_html_header = '<h1>Not Found</h1>'
        expected_html_message = ('<p>The requested URL was not found on the server. If you entered the URL manually'
                                 ' please check your spelling and try again.</p>')

        assert expected_html_title in self.response.text, 'The title of the error page is incorrect'
        assert expected_html_header in self.response.text, 'The header of the error page is incorrect'
        assert expected_html_message in self.response.text, 'The error message content is incorrect'

    @allure.step("404 Error - Not Found")
    def check_404_page(self):
        self._check_common_404_error()
