import logging
import requests


class Peloton:
    def __init__(self, username: str, password: str):
        self.logger = logging.getLogger(__name__)
        self.base_url = 'https://api.onepeloton.com'
        self.token = None
        self.session = requests.Session()

        try:
            self.logger.info(f'Peloton username is "{username}"')
            self.username = username
            self.password = password
        except KeyError:
            self.logger.critical(f'Peloton username or password not configured')
            exit(1)

    def login(self):
        url = self.base_url + '/auth/login'

        headers = {
            'Content-Type': 'application/json'
        }

        payload = {
            "username_or_email": self.username,
            "password": self.password
        }

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code != 200:
            self.logger.error(response.text)
            exit(1)
        else:
            self.token = response.json()
            self.session.headers.update({'Cookie': f'peloton_session_id={self.token["session_id"]}'})

        return response

    def workouts(self):
        url = self.base_url + f'/api/user/{self.token["user_id"]}/workouts'

        response = self.session.get(url)

        if response.status_code != 200:
            self.logger.error(response.headers)
            self.logger.error(response.text)
            exit(1)
        else:
            return response.json()

    def subscriptions(self):
        url = self.base_url + '/api/v2/user/subscriptions'

        response = self.session.get(url)

        self.logger.info(response.status_code)

        if response.status_code != 200:
            self.logger.error(response.headers)
            self.logger.error(response.text)
            exit(1)
        else:
            return response.json()
