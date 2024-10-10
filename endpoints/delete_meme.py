import requests
import allure

from .endpoint import Endpoint


class DeleteMeme(Endpoint):

    @allure.step('Delete the created meme')
    def delete_meme(self, obj_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            f'{self.url}/{obj_id}',
            headers=headers
        )
        return self.response

    @allure.step('Check the response message')
    def check_response_message(self, obj_id):
        assert self.response.text == f'Meme with id {obj_id} successfully deleted', 'Message is incorrect'
