import requests
import allure

from .base_endpoint import BaseEndpoint
from ..test_data.put_payloads import PutPayloads
from .json_schemas import PutScheme


class PutMeme(BaseEndpoint):

    def __init__(self):
        super().__init__()
        self.put_payloads = PutPayloads()

    def put_meme(self, obj_id, payload=None, headers=None):
        with allure.step(f'Update the meme with id: {obj_id}'):
            self.payload = payload if payload else self.put_payloads.valid_object
            self.headers = headers if headers else self.headers.auth_headers
            self.payload['id'] = obj_id
            self.attach_payload(self.payload)

            self.response = requests.put(
                url=f'{self.URL}/{obj_id}',
                json=self.payload,
                headers=self.headers
            )
            if self.response.status_code == 200:
                self.json = self.response.json()
                self.attach_response(self.json)
                model = PutScheme(**self.json)
                return model
