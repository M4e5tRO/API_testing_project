import allure

from .authorization import Authorization
from ..tests.test_api import AUTH_DATA


class Endpoint(Authorization):

    obj_id = None

    def __init__(self):
        self.token = self.authorize(AUTH_DATA[0])
        self.headers = self.set_auth_header()
        self.url = f'{self.base_url}/meme'

    @allure.step('Check the response code - 200 OK')
    def check_response_code_is_200(self):
        assert self.response.status_code == 200, f'Status code {self.response.status_code} is incorrect'

    @allure.step('Match the created "id" key with the response data')
    def match_id_key(self, created_id):
        assert 'id' in self.json, 'The "id" key is NOT created'
        assert int(created_id) == int(self.json['id']), ('The "id" key in the response data is NOT matched with created'
                                                         ' "id"')

    @allure.step('Check the "updated_by" key in the response data')
    def check_updated_by_key(self):
        assert 'updated_by' in self.json, 'The "updated_by" key is NOT created'
