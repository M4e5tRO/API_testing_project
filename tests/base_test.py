import os

from ..test_data.headers_list import Headers
from ..test_data.auth_payloads import AuthPayloads
from ..endpoints.authorization import Authorization
from ..endpoints.get_auth_token import GetAuthToken
from ..endpoints.get_all_memes import GetAllMemes
from ..endpoints.get_meme import GetMeme
from ..endpoints.post_meme import PostMeme
from ..test_data.post_payloads import PostPayloads
from ..endpoints.put_meme import PutMeme
from ..test_data.put_payloads import PutPayloads
from ..endpoints.delete_meme import DeleteMeme


class BaseTest:


    def setup_method(self):
        self.headers = Headers()
        self.auth_payloads = AuthPayloads()
        self.auth_headers = self.get_token()
        self.auth_api = Authorization()
        self.get_auth_token_api = GetAuthToken()
        self.get_all_memes_api = GetAllMemes()
        self.get_meme_api = GetMeme()
        self.post_meme_api = PostMeme()
        self.post_payloads = PostPayloads()
        self.put_meme_api = PutMeme()
        self.put_payloads = PutPayloads()
        self.delete_meme_api = DeleteMeme()


    def get_token(self):

        token = os.getenv('AUTH_TOKEN')
        token = self.check_token(token)

        if not token:
            token = self.authorize_and_get_token()
            print("New token generated:", token)
        else:
            print("Using existing token:", token)

        self.headers.auth_headers["Authorization"] = f"{token}"
        return self.headers.auth_headers


    @staticmethod
    def check_token(token):
        if token:
            get_auth_token_api = GetAuthToken()
            response = get_auth_token_api.get_auth_token(token=token)

            if response.status_code != 200:
                return None
        return token


    def authorize_and_get_token(self):
        headers = self.headers.def_headers
        payloads = self.auth_payloads.valid_credentials
        auth_api = Authorization()
        auth_api.authorize(headers=headers, payload=payloads)

        if auth_api.response.status_code == 200:
            token = auth_api.token
            os.environ['AUTH_TOKEN'] = token
            return token
        else:
            raise Exception('Authorization failed')
