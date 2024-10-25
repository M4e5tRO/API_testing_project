import pytest
import allure

from .base_test import BaseTest
from ..test_data import headers_list, payloads_list


@allure.feature('Get Meme: Positive cases')
class TestGetMemePositive(BaseTest):

    @allure.story('Check the created object (POST) via GET method')
    @pytest.mark.smoke
    def test_get_meme(self):
        self.post_meme_api.post_meme()
        post_id = self.post_meme_api.id
        self.get_meme_api.get_meme(obj_id=post_id)
        self.get_meme_api.check_response_code_is_200()
        self.get_meme_api.match_post_get_id(obj_id=post_id)
        self.get_meme_api.check_description(description=self.post_meme_api.description)
        self.get_meme_api.check_policy(policy=self.post_meme_api.policy)
        self.get_meme_api.check_tags(tags=self.post_meme_api.tags)
        self.get_meme_api.check_text(text=self.post_meme_api.text)
        self.get_meme_api.check_updated_by(updated_by=self.post_meme_api.updated_by)
        self.get_meme_api.check_url(url=self.post_meme_api.url)
        self.delete_meme_api.delete_meme(obj_id=post_id)

    @allure.story("Check Meme structure")
    @pytest.mark.smoke
    def test_get_check_meme_structure(self):
        self.post_meme_api.post_meme()
        post_id = self.post_meme_api.id
        self.get_meme_api.get_meme(obj_id=post_id)
        self.get_meme_api.check_meme_field_type_text()
        self.get_meme_api.check_meme_field_type_url()
        self.get_meme_api.check_meme_field_type_tags()
        self.get_meme_api.check_meme_field_type_info()


@allure.feature('Get Meme: Negative cases')
class TestGetMemeNegative(BaseTest):

    @allure.story('Get object without "token"')
    @pytest.mark.regression
    def test_get_without_token(self, new_obj):
        self.get_meme_api.get_meme(obj_id=new_obj, headers=headers_list.def_headers)
        self.get_meme_api.check_response_code_is_401()
        self.get_meme_api.check_401_page()

    @allure.story('Get object with invalid "token"')
    @pytest.mark.regression
    def test_get_with_invalid_token(self, new_obj):
        self.get_meme_api.get_meme(obj_id=new_obj, headers=headers_list.invalid_token)
        self.get_meme_api.check_response_code_is_401()
        self.get_meme_api.check_401_page()

    @allure.story('Get object: Invalid ID')
    @pytest.mark.regression
    def test_get_invalid_id(self):
        self.get_meme_api.get_meme(obj_id=payloads_list.invalid_id)
        self.get_meme_api.check_response_code_is_404()
        self.get_meme_api.check_404_page()

    @allure.story('Get object with negative ID')
    @pytest.mark.regression
    def test_get_with_negative_id(self, new_obj):
        negative_id = -new_obj
        self.get_meme_api.get_meme(obj_id=negative_id)
        self.get_meme_api.check_response_code_is_404()
        self.get_meme_api.check_404_page()
