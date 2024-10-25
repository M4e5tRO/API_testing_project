import pytest
import allure

from .base_test import BaseTest


@allure.feature('Token')
class TestToken(BaseTest):

    @allure.story('Check valid token')
    @pytest.mark.smoke
    def test_valid_auth_token(self):
        self.get_auth_token_api.get_auth_token()
        self.get_auth_token_api.check_response_code_is_200()
        self.get_auth_token_api.check_auth_response_message()

    @allure.story('Check invalid token')
    @pytest.mark.regression
    def test_invalid_auth_token(self):
        self.get_auth_token_api.get_auth_token(token="invalid_token")
        self.get_auth_token_api.check_response_code_is_404()
        self.get_auth_token_api.check_auth_404_page()
