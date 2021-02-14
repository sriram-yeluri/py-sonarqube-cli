import requests
import logging


class Api:
    def __init__(self, config):
        self.auth = (config.user, config.password)
        self.baseurl: str = config.url
        self.template_name = config.template_name

        self.session = requests.session()
        self.json_response = None
        self.endpoint = None
        self.payload = None
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    def _get(self):
        url = f'{self.baseurl}/{self.endpoint}'
        logging.info(f'URL = {url}')
        try:
            response = self.session.get(url, data=self.payload, auth=self.auth)
            logging.info(response.status_code)
            self.json_response = response.json()
        except Exception as err:
            logging.error(err)

    def _post_params(self):
        url = f'{self.baseurl}/{self.endpoint}'
        logging.info(f'URL = {url}')
        try:
            response = self.session.post(url, params=self.payload, auth=self.auth, headers=self.headers)
            logging.info(response.status_code)
            self.json_response = response.json()
        except Exception as err:
            logging.error(err)

    def _post_json(self):
        url = f'{self.baseurl}/{self.endpoint}'
        logging.info(f'URL = {url}')
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        try:
            response = self.session.post(url, json=self.payload, auth=self.auth, headers=headers)
            logging.info(response.status_code)
            self.json_response = response.json()
        except Exception as err:
            logging.error(err)
