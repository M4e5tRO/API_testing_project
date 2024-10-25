import os

from ..endpoints.authorization import Authorization
from ..endpoints.get_auth_token import GetAuthToken
from ..endpoints.get_all_memes import GetAllMemes
from ..endpoints.get_meme import GetMeme
from ..endpoints.post_meme import PostMeme
from ..endpoints.put_meme import PutMeme
from ..endpoints.delete_meme import DeleteMeme
from ..test_data import headers_list, payloads_list


class BaseTest:

    auth_headers = headers_list.auth_headers
    auth_api = None
    get_auth_token_api = None
    get_all_memes_api = None
    get_meme_api = None
    post_meme_api = None
    put_meme_api = None
    delete_meme_api = None

    def setup_method(self):
        self.auth_headers = self.get_token()
        self.auth_api = Authorization()
        self.get_auth_token_api = GetAuthToken()
        self.get_all_memes_api = GetAllMemes()
        self.get_meme_api = GetMeme()
        self.post_meme_api = PostMeme()
        self.put_meme_api = PutMeme()
        self.delete_meme_api = DeleteMeme()

    def get_token(self):

        token = os.getenv('AUTH_TOKEN')
        token = self.check_token(token)

        if not token:
            token = self.authorize_and_get_token()
            print("New token generated:", token)
        else:
            print("Using existing token:", token)

        headers_list.auth_headers["Authorization"] = f"{token}"
        return headers_list.auth_headers

    @staticmethod
    def check_token(token):
        if token:
            get_auth_token_api = GetAuthToken()
            response = get_auth_token_api.get_auth_token(token=token)

            if response.status_code != 200:
                return None
        return token

    @staticmethod
    def authorize_and_get_token():
        headers = headers_list.def_headers
        payloads = payloads_list.valid_credentials
        auth_api = Authorization()
        auth_api.authorize(headers=headers, payload=payloads)

        if auth_api.response.status_code == 200:
            token = auth_api.token
            os.environ['AUTH_TOKEN'] = token
            return token
        else:
            raise Exception('Authorization failed')
