import pytest
import allure

from .base_test import BaseTest
from ..test_data import payloads_list, headers_list


@allure.feature('Update Meme: Positive cases')
class TestUpdateMemePositive(BaseTest):

    @allure.story('Update the created object')
    @pytest.mark.smoke
    def test_put_meme(self, new_obj):
        self.put_meme_api.put_meme(obj_id=new_obj)
        self.put_meme_api.check_response_code_is_200()
        put_payload = self.put_meme_api.payload
        self.put_meme_api.check_description(description=put_payload['info']['description'])
        self.put_meme_api.check_policy(policy=put_payload['info']['policy'])
        self.put_meme_api.check_tags(tags=put_payload['tags'])
        self.put_meme_api.check_text(text=put_payload['text'])
        self.put_meme_api.check_updated_by(updated_by=payloads_list.valid_credentials['name'])
        self.put_meme_api.check_url(url=put_payload['url'])


@allure.feature('Update Meme: Negative cases')
class TestUpdateMemeNegative(BaseTest):

    @allure.story('Update Meme without "token"')
    @pytest.mark.regression
    def test_put_without_token(self, new_obj):
        self.put_meme_api.put_meme(obj_id=new_obj, headers=headers_list.def_headers)
        self.put_meme_api.check_response_code_is_401()
        self.put_meme_api.check_401_page()

    @allure.story('Send ONLY ONE updated key/value pair (like PATCH method)')
    @pytest.mark.regression
    def test_put_send_like_path_method(self, new_obj):
        self.put_meme_api.put_meme(obj_id=new_obj, payload=payloads_list.put_send_like_path_method)
        self.put_meme_api.check_response_code_is_400()
        self.put_meme_api.check_400_page()

    @allure.story('Update object: Invalid ID')
    @pytest.mark.regression
    def test_put_object_invalid_id(self):
        self.put_meme_api.put_meme(obj_id=payloads_list.invalid_id)
        self.put_meme_api.check_response_code_is_404()
        self.put_meme_api.check_404_page()

    @allure.story('Update object: NO "text" key')
    @pytest.mark.regression
    def test_put_object_no_text(self, new_obj):
        self.put_meme_api.put_meme(obj_id=new_obj, payload=payloads_list.put_object_no_text)
        self.put_meme_api.check_response_code_is_400()
        self.put_meme_api.check_400_page()

    @allure.story('Update object: NO "url" key')
    @pytest.mark.regression
    def test_put_object_no_url(self, new_obj):
        self.put_meme_api.put_meme(obj_id=new_obj, payload=payloads_list.put_object_no_url)
        self.put_meme_api.check_response_code_is_400()
        self.put_meme_api.check_400_page()

    @allure.story('Update object: NO "tags" key')
    @pytest.mark.regression
    def test_put_object_no_tags(self, new_obj):
        self.put_meme_api.put_meme(obj_id=new_obj, payload=payloads_list.put_object_no_tags)
        self.put_meme_api.check_response_code_is_400()
        self.put_meme_api.check_400_page()

    @allure.story('Update object: NO "info" key')
    @pytest.mark.regression
    def test_put_object_no_info(self, new_obj):
        self.put_meme_api.put_meme(obj_id=new_obj, payload=payloads_list.put_object_no_info)
        self.put_meme_api.check_response_code_is_400()
        self.put_meme_api.check_400_page()

    @allure.story('Update object with any additional key/value pair')
    @pytest.mark.regression
    def test_put_add_any_key_value_pair(self, new_obj):
        self.put_meme_api.put_meme(obj_id=new_obj, payload=payloads_list.put_add_any_key_value_pair)
        self.put_meme_api.check_response_code_is_400()
        self.put_meme_api.check_400_page()

    @allure.story('Invalid type: "text" is object')
    @pytest.mark.regression
    def test_put_invalid_type_text_is_object(self, new_obj):
        self.put_meme_api.put_meme(obj_id=new_obj, payload=payloads_list.put_invalid_type_text_is_object)
        self.put_meme_api.check_response_code_is_400()
        self.put_meme_api.check_400_page()

    @allure.story('Invalid type: "url" is array')
    @pytest.mark.regression
    def test_put_invalid_type_url_is_array(self, new_obj):
        self.put_meme_api.put_meme(obj_id=new_obj, payload=payloads_list.put_invalid_type_url_is_array)
        self.put_meme_api.check_response_code_is_400()
        self.put_meme_api.check_400_page()

    @allure.story('Invalid type: "tags" is None')
    @pytest.mark.regression
    def test_put_invalid_type_tags_is_none(self, new_obj):
        self.put_meme_api.put_meme(obj_id=new_obj, payload=payloads_list.put_invalid_type_tags_is_none)
        self.put_meme_api.check_response_code_is_400()
        self.put_meme_api.check_400_page()

    @allure.story('Invalid type: "info" is string')
    @pytest.mark.regression
    def test_put_invalid_type_info_is_string(self, new_obj):
        self.put_meme_api.put_meme(obj_id=new_obj, payload=payloads_list.put_invalid_type_info_is_string)
        self.put_meme_api.check_response_code_is_400()
        self.put_meme_api.check_400_page()

    @allure.story('Update object on behalf of another user')
    @pytest.mark.regression
    def test_put_on_behalf_of_another_user(self):
        self.get_all_memes_api.get_all_memes()
        self.get_all_memes_api.find_meme_id_by_updated_by()
        self.put_meme_api.put_meme(obj_id=self.get_all_memes_api.meme_different_user_id)
        self.put_meme_api.check_response_code_is_403()
        self.put_meme_api.check_403_page()
