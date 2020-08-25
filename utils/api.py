import requests
import logging


class Api:
    def __init__(self, username, password, baseurl, loglevel):
        self.username: str = username
        self.password: str = password
        self.baseurl: str = baseurl
        self.loglevel: str = loglevel
        logging.basicConfig(format='%(levelname)s %(asctime)s : %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            level=getattr(logging, self.loglevel),
                            filename='sonar-cli.log')

    def get_request(self, endpoint):
        session = requests.session()
        url = f'{self.baseurl}/{endpoint}'
        logging.debug(f'URL = {url}')
        payload = ""
        try:
            response = session.get(url, data=payload, auth=(self.username, self.password))
            logging.debug(response.status_code)
            json_response = response.json()
            return json_response
        except Exception as err:
            logging.error(err)

    def post_request(self):
        response = ''
        return response
