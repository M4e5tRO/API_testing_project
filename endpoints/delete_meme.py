import requests
import allure

from .base_endpoint import BaseEndpoint


class DeleteMeme(BaseEndpoint):

    def delete_meme(self, obj_id, headers=None):
        with allure.step(f'Delete the created meme with id: {obj_id}'):
            self.headers = headers if headers else self.headers.auth_headers

            self.response = requests.delete(
                url=f'{self.URL}/{obj_id}',
                headers=self.headers
            )
            return self.response

    @allure.step('Check the response message')
    def check_response_message(self, obj_id):
        allure.attach('Message', f'Message: "{self.response.text}"', allure.attachment_type.TEXT)
        assert self.response.text == f'Meme with id {obj_id} successfully deleted', 'Message is incorrect'
