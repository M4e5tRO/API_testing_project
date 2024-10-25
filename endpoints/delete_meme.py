import requests
import allure

from .base_endpoint import BaseEndpoint
from ..test_data import headers_list


class DeleteMeme(BaseEndpoint):

    @allure.step('Delete the created meme')
    def delete_meme(self, obj_id, headers=None):
        self.headers = headers if headers else headers_list.auth_headers

        self.response = requests.delete(
            f'{self.url}/{obj_id}',
            headers=self.headers
        )
        return self.response

    @allure.step('Check the response message')
    def check_response_message(self, obj_id):
        assert self.response.text == f'Meme with id {obj_id} successfully deleted', 'Message is incorrect'
