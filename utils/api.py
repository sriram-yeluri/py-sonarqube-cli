import requests
import logging


class Api:
    def __init__(self, username, password, baseurl, loglevel):
        self.username: str = username
        self.password: str = password
        self.baseurl: str = baseurl
        self.session = requests.session()
        self.json_response = None
        self.endpoint = None
        self.payload = None
        self.loglevel: str = loglevel
        logging.basicConfig(format='%(levelname)s %(asctime)s : [%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            level=getattr(logging, self.loglevel),
                            filename='sonar-cli.log')

    def _get(self):
        url = f'{self.baseurl}/{self.endpoint}'
        logging.debug(f'URL = {url}')
        try:
            response = self.session.get(url, data=self.payload, auth=(self.username, self.password))
            logging.info(response.status_code)
            self.json_response = response.json()
        except Exception as err:
            logging.error(err)
            print('Check sonar-cli.log')

    def _post(self):
        url = f'{self.baseurl}/{self.endpoint}'
        logging.debug(f'URL = {url}')
        payload = ""
        try:
            response = self.session.post(url, data=payload, auth=(self.username, self.password))
            logging.info(response.status_code)
            self.json_response = response.json()
        except Exception as err:
            logging.error(err)
            print('Check sonar-cli.log')