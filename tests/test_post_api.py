import pytest
import allure

from .base_test import BaseTest
from ..test_data import payloads_list, headers_list


@allure.feature('Create Meme: Positive cases')
class TestCreateMemePositive(BaseTest):

    @allure.story('Create valid object')
    @pytest.mark.smoke
    def test_post_meme(self):
        self.post_meme_api.post_meme()
        self.post_meme_api.check_response_code_is_200()
        post_payload = self.post_meme_api.payload
        self.post_meme_api.check_description(description=post_payload['info']['description'])
        self.post_meme_api.check_policy(policy=post_payload['info']['policy'])
        self.post_meme_api.check_tags(tags=post_payload['tags'])
        self.post_meme_api.check_text(text=post_payload['text'])
        self.post_meme_api.check_updated_by(updated_by=payloads_list.valid_credentials['name'])
        self.post_meme_api.check_url(url=post_payload['url'])
        self.delete_meme_api.delete_meme(obj_id=self.post_meme_api.id)


@allure.feature('Create Meme: Negative cases')
class TestCreateMemeNegative(BaseTest):

    @allure.story('Create object without "token"')
    @pytest.mark.regression
    def test_post_without_token(self):
        self.post_meme_api.post_meme(headers=headers_list.def_headers)
        self.post_meme_api.check_response_code_is_401()
        self.post_meme_api.check_401_page()

    @allure.story('Create object with invalid "token"')
    @pytest.mark.regression
    def test_create_with_invalid_token(self):
        self.post_meme_api.post_meme(headers=headers_list.invalid_token)
        self.post_meme_api.check_response_code_is_401()
        self.post_meme_api.check_401_page()

    @allure.story('Create invalid object: NO "text" key')
    @pytest.mark.regression
    def test_post_invalid_object_no_text(self):
        self.post_meme_api.post_meme(payload=payloads_list.post_invalid_object_no_text)
        self.post_meme_api.check_response_code_is_400()
        self.post_meme_api.check_400_page()

    @allure.story('Create invalid object: NO "url" key')
    @pytest.mark.regression
    def test_post_invalid_object_no_url(self):
        self.post_meme_api.post_meme(payload=payloads_list.post_invalid_object_no_url)
        self.post_meme_api.check_response_code_is_400()
        self.post_meme_api.check_400_page()

    @allure.story('Create invalid object: NO "tags" key')
    @pytest.mark.regression
    def test_post_invalid_object_no_tags(self):
        self.post_meme_api.post_meme(payload=payloads_list.post_invalid_object_no_tags)
        self.post_meme_api.check_response_code_is_400()
        self.post_meme_api.check_400_page()

    @allure.story('Create invalid object: NO "info" key')
    @pytest.mark.regression
    def test_post_invalid_object_no_info(self):
        self.post_meme_api.post_meme(payload=payloads_list.post_invalid_object_no_info)
        self.post_meme_api.check_response_code_is_400()
        self.post_meme_api.check_400_page()

    @allure.story('Create object with any additional key/value pair')
    @pytest.mark.regression
    def test_post_add_any_key_value_pair(self):
        self.post_meme_api.post_meme(payload=payloads_list.post_add_any_key_value_pair)
        self.post_meme_api.check_response_code_is_400()
        self.post_meme_api.check_400_page()

    @allure.story('Invalid type: "text" is number')
    @pytest.mark.regression
    def test_post_invalid_type_text_is_number(self):
        self.post_meme_api.post_meme(payload=payloads_list.post_invalid_object_text_is_number)
        self.post_meme_api.check_response_code_is_400()
        self.post_meme_api.check_400_page()

    @allure.story('Invalid type: "url" is boolean')
    @pytest.mark.regression
    def test_post_invalid_type_url_is_boolean(self):
        self.post_meme_api.post_meme(payload=payloads_list.post_invalid_object_url_is_boolean)
        self.post_meme_api.check_response_code_is_400()
        self.post_meme_api.check_400_page()

    @allure.story('Invalid type: "tags" is object')
    @pytest.mark.regression
    def test_post_invalid_type_tags_is_object(self):
        self.post_meme_api.post_meme(payload=payloads_list.post_invalid_object_tags_is_object)
        self.post_meme_api.check_response_code_is_400()
        self.post_meme_api.check_400_page()

    @allure.story('Invalid type: "info" is array')
    @pytest.mark.regression
    def test_post_invalid_type_info_is_array(self):
        self.post_meme_api.post_meme(payload=payloads_list.post_invalid_object_info_is_array)
        self.post_meme_api.check_response_code_is_400()
        self.post_meme_api.check_400_page()
