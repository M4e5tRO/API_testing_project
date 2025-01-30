import pytest
import allure

from .base_test import BaseTest


@allure.feature('Authorization: Positive cases')
class TestAuthorizationPositive(BaseTest):

    @allure.story('Valid name: string')
    @pytest.mark.smoke
    def test_auth_valid_name_string(self):
        self.auth_api.authorize(payload=self.auth_payloads.auth_valid_name_string)
        self.auth_api.check_response_code_is_200()
        self.auth_api.check_token()
        self.auth_api.check_name(self.auth_api.payload['name'])


@allure.feature('Authorization: Negative cases')
class TestAuthorizationNegative(BaseTest):

    @allure.story('Invalid name: empty string')
    @pytest.mark.regression
    def test_auth_invalid_name_empty(self):
        self.auth_api.authorize(payload=self.auth_payloads.auth_invalid_name_empty)
        self.auth_api.check_response_code_is_400()
        self.auth_api.check_400_page()

    @allure.story('No "name" key')
    @pytest.mark.regression
    def test_auth_no_name_key(self):
        self.auth_api.authorize(payload=self.auth_payloads.auth_no_name_key)
        self.auth_api.check_response_code_is_400()
        self.auth_api.check_400_page()

    @allure.story('Invalid name: integer')
    @pytest.mark.regression
    def test_auth_invalid_name_integer(self):
        self.auth_api.authorize(payload=self.auth_payloads.auth_invalid_name_integer)
        self.auth_api.check_response_code_is_400()
        self.auth_api.check_400_page()

    @allure.story('Invalid name: float')
    @pytest.mark.regression
    def test_auth_invalid_name_float(self):
        self.auth_api.authorize(payload=self.auth_payloads.auth_invalid_name_float)
        self.auth_api.check_response_code_is_400()
        self.auth_api.check_400_page()

    @allure.story('Invalid name: boolean')
    @pytest.mark.regression
    def test_auth_invalid_name_boolean(self):
        self.auth_api.authorize(payload=self.auth_payloads.auth_invalid_name_boolean)
        self.auth_api.check_response_code_is_400()
        self.auth_api.check_400_page()

    @allure.story('Invalid name: None')
    @pytest.mark.regression
    def test_auth_invalid_name_none(self):
        self.auth_api.authorize(payload=self.auth_payloads.auth_invalid_name_none)
        self.auth_api.check_response_code_is_400()
        self.auth_api.check_400_page()

    @allure.story('Invalid name: empty array')
    @pytest.mark.regression
    def test_auth_invalid_name_empty_array(self):
        self.auth_api.authorize(payload=self.auth_payloads.auth_invalid_name_empty_array)
        self.auth_api.check_response_code_is_400()
        self.auth_api.check_400_page()

    @allure.story('Invalid name: array')
    @pytest.mark.regression
    def test_auth_invalid_name_array(self):
        self.auth_api.authorize(payload=self.auth_payloads.auth_invalid_name_array)
        self.auth_api.check_response_code_is_400()
        self.auth_api.check_400_page()

    @allure.story('Invalid name: empty object')
    @pytest.mark.regression
    def test_auth_invalid_name_empty_object(self):
        self.auth_api.authorize(payload=self.auth_payloads.auth_invalid_name_empty_object)
        self.auth_api.check_response_code_is_400()
        self.auth_api.check_400_page()

    @allure.story('Invalid name: object')
    @pytest.mark.regression
    def test_auth_invalid_name_object(self):
        self.auth_api.authorize(payload=self.auth_payloads.auth_invalid_name_object)
        self.auth_api.check_response_code_is_400()
        self.auth_api.check_400_page()
