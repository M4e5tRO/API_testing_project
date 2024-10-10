import requests
import allure

from .endpoint import Endpoint


class GetAllMemes(Endpoint):

    @allure.step('Get ALL memes')
    def get_all_memes(self, headers=None):
      headers = headers if headers else self.headers
      self.response = requests.get(
          self.url,
          headers=headers
      )
      self.json = self.response.json()
      return self.response

    @allure.step('Check the "data" key in the response data')
    def check_data_key(self):
        assert 'data' in self.json, 'The "data" key is NOT created'
