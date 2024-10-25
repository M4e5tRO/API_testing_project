import requests
import allure

from .base_endpoint import BaseEndpoint
from ..test_data import headers_list


class GetAllMemes(BaseEndpoint):

    def __init__(self):
        super().__init__()
        self.meme_found = None
        self.meme_different_user_id = None

    @allure.step('Get ALL memes')
    def get_all_memes(self, headers=None):
        self.headers = headers if headers else headers_list.auth_headers

        self.response = requests.get(
            self.url,
            headers=self.headers
        )
        if self.response.status_code == 200:
            self.json = self.response.json()
            self.all_memes = self.json['data']
        return self.response

    @allure.step('Find meme by ID')
    def find_meme_by_id(self, obj_id):
        self.meme_found = next((meme for meme in self.all_memes if meme["id"] == obj_id), None)
        assert self.meme_found is not None, f"Meme with ID: {obj_id} not found"

    @allure.step('Find meme ID by updated_by different from logged user')
    def find_meme_id_by_updated_by(self):
        meme_different_user = next((meme for meme in self.all_memes if meme["updated_by"] != self.user), None)
        assert meme_different_user is not None, f"No meme found with updated_by different from {self.user}"
        self.meme_different_user_id = meme_different_user['id']
        return self.meme_different_user_id

    @allure.step('Checking for required fields in each meme')
    def check_memes_required_fields(self):
        required_fields = ['text', 'url', 'tags', 'info']
        for meme in self.all_memes:
            for field in required_fields:
                assert field in meme, f"Error: field ‘{field}’ is missing in the meme"

    @allure.step('Checking "text" data type')
    def check_memes_field_type_text(self):
        for meme in self.all_memes:
            assert isinstance(meme['text'], str), f"Meme ID: {meme['id']} - ‘text’ should be a string"

    @allure.step('Checking "url" data type')
    def check_memes_field_type_url(self):
        for meme in self.all_memes:
            assert isinstance(meme['url'], str), f"Meme ID: {meme['id']} - ‘url’ should be a string"

    @allure.step('Checking "tags" data type')
    def check_memes_field_type_tags(self):
        for meme in self.all_memes:
            assert isinstance(meme['tags'], list), f"Meme ID: {meme['id']} - ‘tags’ should be an array"

    @allure.step('Checking "tags" data type')
    def check_memes_field_type_info(self):
        for meme in self.all_memes:
            assert isinstance(meme['info'], dict), f"Meme ID: {meme['id']} - ‘info’ should be an object"
