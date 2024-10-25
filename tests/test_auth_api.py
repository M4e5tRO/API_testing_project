import pytest
import allure

from .base_test import BaseTest
from ..test_data import payloads_list


@allure.feature('Authorization: Positive cases')
class TestAuthorizationPositive(BaseTest):

    @allure.story('Valid name: string')
    @pytest.mark.smoke
    def test_auth_valid_name_string(self):
        self.auth_api.authorize(payload=payloads_list.auth_valid_name_string)
        self.auth_api.check_response_code_is_200()
        self.auth_api.check_token()
        self.auth_api.check_name(self.auth_api.payload['name'])


@allure.feature('Authorization: Negative cases')
class TestAuthorizationNegative(BaseTest):

    @allure.story('Invalid name: empty string')
    @pytest.mark.regression
    def test_auth_invalid_name_empty(self):
        self.auth_api.authorize(payload=payloads_list.auth_invalid_name_empty)
        self.auth_api.check_response_code_is_400()
        self.auth_api.check_400_page()

    @allure.story('Invalid name: only spaces string')
    @pytest.mark.regression
    def test_auth_invalid_name_only_spaces(self):
        self.auth_api.authorize(payload=payloads_list.auth_invalid_name_only_spaces)
        self.auth_api.check_response_code_is_400()
        self.auth_api.check_400_page()

    @allure.story('Additional key-value pair')
    @pytest.mark.regression
    def test_auth_additional_key_value(self):
        self.auth_api.authorize(payload=payloads_list.auth_additional_key_value)
        self.auth_api.check_response_code_is_400()
        self.auth_api.check_400_page()

    @allure.story('No "name" key')
    @pytest.mark.regression
    def test_auth_no_name_key(self):
        self.auth_api.authorize(payload=payloads_list.auth_no_name_key)
        self.auth_api.check_response_code_is_400()
        self.auth_api.check_400_page()

    @allure.story('Invalid name: single quotes')
    @pytest.mark.regression
    def test_auth_invalid_name_single_quotes(self):
        self.auth_api.authorize(payload=payloads_list.auth_invalid_name_single_quotes)
        self.auth_api.check_response_code_is_400()
        self.auth_api.check_400_page()

    @allure.story('Invalid name: integer')
    @pytest.mark.regression
    def test_auth_invalid_name_integer(self):
        self.auth_api.authorize(payload=payloads_list.auth_invalid_name_integer)
        self.auth_api.check_response_code_is_400()
        self.auth_api.check_400_page()

    @allure.story('Invalid name: float')
    @pytest.mark.regression
    def test_auth_invalid_name_float(self):
        self.auth_api.authorize(payload=payloads_list.auth_invalid_name_float)
        self.auth_api.check_response_code_is_400()
        self.auth_api.check_400_page()

    @allure.story('Invalid name: boolean')
    @pytest.mark.regression
    def test_auth_invalid_name_boolean(self):
        self.auth_api.authorize(payload=payloads_list.auth_invalid_name_boolean)
        self.auth_api.check_response_code_is_400()
        self.auth_api.check_400_page()

    @allure.story('Invalid name: None')
    @pytest.mark.regression
    def test_auth_invalid_name_none(self):
        self.auth_api.authorize(payload=payloads_list.auth_invalid_name_none)
        self.auth_api.check_response_code_is_400()
        self.auth_api.check_400_page()

    @allure.story('Invalid name: empty array')
    @pytest.mark.regression
    def test_auth_invalid_name_empty_array(self):
        self.auth_api.authorize(payload=payloads_list.auth_invalid_name_empty_array)
        self.auth_api.check_response_code_is_400()
        self.auth_api.check_400_page()

    @allure.story('Invalid name: array')
    @pytest.mark.regression
    def test_auth_invalid_name_array(self):
        self.auth_api.authorize(payload=payloads_list.auth_invalid_name_array)
        self.auth_api.check_response_code_is_400()
        self.auth_api.check_400_page()

    @allure.story('Invalid name: empty object')
    @pytest.mark.regression
    def test_auth_invalid_name_empty_object(self):
        self.auth_api.authorize(payload=payloads_list.auth_invalid_name_empty_object)
        self.auth_api.check_response_code_is_400()
        self.auth_api.check_400_page()

    @allure.story('Invalid name: object')
    @pytest.mark.regression
    def test_auth_invalid_name_object(self):
        self.auth_api.authorize(payload=payloads_list.auth_invalid_name_object)
        self.auth_api.check_response_code_is_400()
        self.auth_api.check_400_page()
