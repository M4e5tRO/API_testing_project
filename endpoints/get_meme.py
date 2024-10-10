import requests
import allure

from .endpoint import Endpoint


class GetMeme(Endpoint):

    @allure.step('Read the created meme')
    def get_meme(self, obj_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
          f'{self.url}/{obj_id}',
          headers=headers
        )
        self.json = self.response.json()
        return self.response
