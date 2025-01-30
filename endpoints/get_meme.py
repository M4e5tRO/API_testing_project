import requests
import allure

from .base_endpoint import BaseEndpoint
from .json_schemas import GetMemeScheme


class GetMeme(BaseEndpoint):

    def get_meme(self, obj_id, headers=None):
        with allure.step(f'Get the meme with id: {obj_id}'):
            self.headers = headers if headers else self.headers.auth_headers

            self.response = requests.get(
                url=f'{self.url}/{obj_id}',
                headers=self.headers
            )
            if self.response.status_code == 200:
                self.json = self.response.json()
                self.attach_response(self.json)
                self.model = GetMemeScheme(**self.response.json())
                return self.model
