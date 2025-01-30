import requests
import allure

from .base_endpoint import BaseEndpoint
from ..test_data.post_payloads import PostPayloads
from .json_schemas import PostScheme


class PostMeme(BaseEndpoint):

    def __init__(self):
        super().__init__()
        self.post_payloads = PostPayloads()

    def post_meme(self, payload=None, headers=None):
        with allure.step('Create a meme'):
            self.payload = payload if payload else self.post_payloads.valid_object
            self.headers = headers if headers else self.headers.auth_headers
            self.attach_payload(self.payload)

            self.response = requests.post(
                url=self.url,
                json=self.payload,
                headers=self.headers
            )
            if self.response.status_code == 200:
                self.json = self.response.json()
                self.attach_response(self.json)
                model = PostScheme(**self.json)
                self.id = model.id
                return model
