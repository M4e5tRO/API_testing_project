import pytest
import allure

from .base_test import BaseTest


@allure.feature('Delete Meme: Positive cases')
class TestDeleteMemePositive(BaseTest):

    @allure.story('Delete the created object')
    @pytest.mark.smoke
    def test_delete_meme(self):
        self.post_meme_api.post_meme()
        post_id = self.post_meme_api.id
        self.delete_meme_api.delete_meme(obj_id=post_id)
        self.delete_meme_api.check_response_code_is_200()
        self.delete_meme_api.check_response_message(obj_id=post_id)
        self.get_meme_api.get_meme(obj_id=post_id)
        self.get_meme_api.check_response_code_is_404()
        self.get_meme_api.check_404_page()


@allure.feature('Delete Meme: Negative cases')
class TestDeleteMemeNegative(BaseTest):

    @allure.story('Delete object without "token"')
    @pytest.mark.regression
    def test_delete_without_token(self, new_obj):
        self.delete_meme_api.delete_meme(obj_id=new_obj, headers=self.headers.def_headers)
        self.delete_meme_api.check_response_code_is_401()
        self.delete_meme_api.check_401_page()

    @allure.story('Delete object with invalid "token"')
    @pytest.mark.regression
    def test_delete_with_invalid_token(self, new_obj):
        self.delete_meme_api.delete_meme(obj_id=new_obj, headers=self.headers.invalid_token)
        self.delete_meme_api.check_response_code_is_401()
        self.delete_meme_api.check_401_page()

    @allure.story('Delete object twice')
    @pytest.mark.regression
    def test_delete_twice(self, new_obj):
        self.delete_meme_api.delete_meme(obj_id=new_obj)
        self.delete_meme_api.delete_meme(obj_id=new_obj, headers=self.headers.auth_headers)
        self.delete_meme_api.check_response_code_is_404()
        self.delete_meme_api.check_404_page()

    @allure.story('Delete object with an invalid ID')
    @pytest.mark.regression
    def test_delete_with_invalid_id(self, new_obj):
        self.delete_meme_api.delete_meme(obj_id=self.auth_payloads.invalid_id)
        self.delete_meme_api.check_response_code_is_404()
        self.delete_meme_api.check_404_page()

    @allure.story('Delete object with negative ID')
    @pytest.mark.regression
    def test_delete_with_negative_id(self, new_obj):
        negative_id = -new_obj
        self.delete_meme_api.delete_meme(obj_id=negative_id)
        self.delete_meme_api.check_response_code_is_404()
        self.delete_meme_api.check_404_page()

    @allure.story('Delete object on behalf of another user')
    @pytest.mark.regression
    def test_delete_on_behalf_of_another_user(self):
        self.get_all_memes_api.get_all_memes()
        self.get_all_memes_api.find_meme_id_by_updated_by()
        self.delete_meme_api.delete_meme(obj_id=self.get_all_memes_api.meme_different_user_id)
        self.delete_meme_api.check_response_code_is_403()
        self.delete_meme_api.check_403_page()
