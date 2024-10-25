import pytest
import allure

from .base_test import BaseTest
from ..test_data import headers_list


@allure.feature('Get All Memes: Positive cases')
class TestGetAllMemesPositive(BaseTest):

    @allure.story("Check Memes structure")
    @pytest.mark.smoke
    def test_get_all_check_memes_structure(self):
        self.get_all_memes_api.get_all_memes()
        self.get_all_memes_api.check_memes_required_fields()
        self.get_all_memes_api.check_memes_field_type_text()
        self.get_all_memes_api.check_memes_field_type_url()
        self.get_all_memes_api.check_memes_field_type_tags()
        self.get_all_memes_api.check_memes_field_type_info()

    @allure.story("Find the created object by ID")
    @pytest.mark.regression
    def test_get_all_find_object_by_id(self, new_obj):
        self.get_all_memes_api.get_all_memes()
        self.get_all_memes_api.check_response_code_is_200()
        self.get_all_memes_api.find_meme_by_id(obj_id=new_obj)

    @allure.story("Find the created object by User's name")
    @pytest.mark.regression
    def test_get_all_find_object_by_name(self, new_obj):
        self.get_all_memes_api.get_all_memes()
        self.get_all_memes_api.check_response_code_is_200()
        self.get_all_memes_api.find_meme_id_by_updated_by()


@allure.feature('Get All Memes: Negative cases')
class TestGetAllMemesNegative(BaseTest):

    @allure.story('Get All objects without "token"')
    @pytest.mark.regression
    def test_get_all_without_token(self):
        self.get_all_memes_api.get_all_memes(headers=headers_list.def_headers)
        self.get_all_memes_api.check_response_code_is_401()
        self.get_all_memes_api.check_401_page()

    @allure.story('Get All objects with invalid "token"')
    @pytest.mark.regression
    def test_get_all_with_invalid_token(self):
        self.get_all_memes_api.get_all_memes(headers=headers_list.invalid_token)
        self.get_all_memes_api.check_response_code_is_401()
        self.get_all_memes_api.check_401_page()
