import requests
import allure

from .endpoint import Endpoint


class PutMeme(Endpoint):

    @allure.step('Update the created data')
    def put_meme(self, obj_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{obj_id}',
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        return self.response

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
