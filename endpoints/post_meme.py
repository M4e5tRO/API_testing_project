import requests
import allure

from .base_endpoint import BaseEndpoint
from ..test_data import payloads_list, headers_list
from .json_schemas import PostScheme


class PostMeme(BaseEndpoint):

    @allure.step('Create a meme')
    def post_meme(self, payload=None, headers=None):
        self.payload = payload if payload else payloads_list.post_valid_object
        self.headers = headers if headers else headers_list.auth_headers

        self.response = requests.post(
            self.url,
            json=self.payload,
            headers=self.headers
        )
        if self.response.status_code == 200:
            self.json = PostScheme(**self.response.json())
            self.id = self.json.id
            self.description = self.json.info.description
            self.policy = self.json.info.policy
            self.tags = self.json.tags
            self.text = self.json.text
            self.updated_by = self.json.updated_by
            self.url = self.json.url
        return self.response

    @allure.step('Check the "id" key in the response data')
    def check_id_key(self):
        assert 'id' in self.json, 'The "id" key is NOT created'
