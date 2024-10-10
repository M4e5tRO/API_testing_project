import requests


class Authorization:

    base_url = 'http://167.172.172.115:52355'
    auth_url = f'{base_url}/authorize'
    headers = {'Content-Type': 'application/json'}
    response = None
    json = None
    token = None

    def authorize(self, payload, headers=None):
        headers = headers if headers else self.headers

        if self.is_token_valid():
            return self.token

        self.response = requests.post(
            self.auth_url,
            json=payload,
            headers=headers
        )
        self.token = self.response.json().get('token')
        return self.token

    def is_token_valid(self, headers=None, token=None):
        headers = headers if headers else self.headers
        token = token if token else self.token

        if not token:
            return False

        self.response = requests.get(
            f'{self.auth_url}/{token}',
            headers=headers
        )
        return self.response.status_code == 200

    def set_auth_header(self, headers=None, token=None):
        headers = headers if headers else self.headers
        token = token if token else self.token

        headers["Authorization"] = f"{token}"
        return self.headers
