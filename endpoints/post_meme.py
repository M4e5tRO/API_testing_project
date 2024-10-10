import requests
import allure

from .endpoint import Endpoint


class PostMeme(Endpoint):

    @allure.step('Create a meme')
    def post_meme(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=payload,
            headers=headers
        )
        self.json = self.response.json()
        self.obj_id = self.json.get('id')
        return self.response

    @allure.step('Check the "id" key in the response data')
    def check_id_key(self):
        assert 'id' in self.json, 'The "id" key is NOT created'
