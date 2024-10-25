import requests
import allure

from .base_endpoint import BaseEndpoint
from .json_schemas import GetMemeScheme, InfoScheme
from ..test_data import headers_list


class GetMeme(BaseEndpoint):

    @allure.step('Read the created meme')
    def get_meme(self, obj_id, headers=None):
        self.headers = headers if headers else headers_list.auth_headers

        self.response = requests.get(
            f'{self.url}/{obj_id}',
            headers=self.headers
        )
        if self.response.status_code == 200:
            self.json = GetMemeScheme(**self.response.json())
            self.id = self.json.id
            self.info = self.json.info
            self.description = self.info.description
            self.policy = self.info.policy
            self.tags = self.json.tags
            self.text = self.json.text
            self.updated_by = self.json.updated_by
            self.url = self.json.url
        return self.response

    @allure.step('Match the "id" in POST & GET')
    def match_post_get_id(self, obj_id):
        get_id = self.json.id
        assert int(obj_id) == int(get_id), f'The POST ID: "{obj_id}" does NOT matched with the GET ID: "{get_id}"'

    @allure.step('Checking "text" data type in the meme')
    def check_meme_field_type_text(self):
        assert isinstance(self.text, str), f"Meme ID: {self.id} - ‘text’ should be a string"

    @allure.step('Checking "url" data type in the meme')
    def check_meme_field_type_url(self):
        assert isinstance(self.url, str), f"Meme ID: {self.id} - ‘url’ should be a string"

    @allure.step('Checking "tags" data type in the meme')
    def check_meme_field_type_tags(self):
        assert isinstance(self.tags, list), f"Meme ID: {self.id} - ‘tags’ should be an array"

    @allure.step('Checking "info" data type in the meme')
    def check_meme_field_type_info(self):
        assert isinstance(self.info, InfoScheme), f"Meme ID: {self.id} - ‘info’ should be an object"
