import requests
import allure

from .base_endpoint import BaseEndpoint
from ..test_data import payloads_list, headers_list
from .json_schemas import PutScheme


class PutMeme(BaseEndpoint):

    @allure.step('Update the created data')
    def put_meme(self, obj_id, payload=None, headers=None):
        self.payload = payload if payload else payloads_list.put_valid_object
        self.headers = headers if headers else headers_list.auth_headers
        self.payload['id'] = obj_id

        self.response = requests.put(
            f'{self.url}/{obj_id}',
            json=self.payload,
            headers=self.headers
        )
        if self.response.status_code == 200:
            self.json = PutScheme(**self.response.json())
            self.id = self.json.id
            self.description = self.json.info.description
            self.policy = self.json.info.policy
            self.tags = self.json.tags
            self.text = self.json.text
            self.updated_by = self.json.updated_by
            self.url = self.json.url
        return self.response

    @allure.step('Match the "id" in the response & payload')
    def check_id(self, payload_id):
        resp_id = int(self.id)
        payload_id = int(payload_id)
        assert resp_id == payload_id, f'The payload: "{payload_id}" does NOT matched with the response: "{resp_id}"'

    @allure.step('Check the updated text')
    def check_updated_text(self, updated_text):
        assert updated_text in self.json['text'], f'The "{updated_text}" is NOT added / is partially added'

    @allure.step('Check the updated url')
    def check_updated_url(self, updated_url):
        assert updated_url in self.json['url'], f'The "{updated_url}" is NOT added / is partially added'

    @allure.step('Check the updated description')
    def check_updated_description(self, updated_description):
        assert updated_description in self.json['info']['description'], (f'The "{updated_description}" is NOT added'
                                                                         f' / is partially added')

    @allure.step('Check if new tags are added')
    def check_new_tags(self, expected_tags):
        existing_tags = set(self.json.get('tags', []))
        new_tags = set(expected_tags)
        missing_tags = new_tags - existing_tags

        assert not missing_tags, f"Tags {missing_tags} are NOT added to the meme"
