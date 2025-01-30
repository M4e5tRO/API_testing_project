import requests
import allure

from .base_endpoint import BaseEndpoint


class GetAllMemes(BaseEndpoint):

    def get_all_memes(self, headers=None):
        with allure.step('Get all memes'):
            self.headers = headers if headers else self.headers.auth_headers

            self.response = requests.get(
                url=self.url,
                headers=self.headers
            )
            if self.response.status_code == 200:
                self.json = self.response.json()
                self.attach_response(self.json)
                self.all_memes = self.json['data']
                return self.response

    @allure.step('Find meme by ID')
    def find_meme_by_id(self, obj_id):
        meme_found = next((meme for meme in self.all_memes if meme["id"] == obj_id), None)
        assert meme_found is not None, f"Meme with ID: {obj_id} not found"

    @allure.step('Find meme ID by updated_by different from logged user')
    def find_meme_id_by_updated_by(self):
        meme_different_user = next((meme for meme in self.all_memes if meme["updated_by"] != self.auth_payloads.valid_credentials["name"]),None)
        assert meme_different_user is not None, f"No meme found with updated_by different from {self.auth_payloads.valid_credentials["name"]}"
        self.meme_different_user_id = meme_different_user['id']
        return self.meme_different_user_id
