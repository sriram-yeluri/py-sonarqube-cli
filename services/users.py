from utils.api import Api
import logging


class Users(Api):

    def createuser(self, login: str, f_name: str, l_name: str, password: str, email: str):
        self.endpoint = 'api/users/create'
        # To-Do : Add validation for arguments
        data = {'login': login, 'name': f'{f_name}{l_name}', 'password': password, 'email': email}
        self.payload = data
        self._post_params()
        if self.json_response:
            logging.info(self.json_response)

    def deactivateuser(self, login: str):
        self.endpoint = 'api/users/deactivate'
        data = {'login': login}
        self.payload = data
        self._post_params()
        if self.json_response:
            logging.info(self.json_response)

    # Get a list of active users
    def getactiveusers(self):
        self.endpoint = 'api/users/search'
        self._get()
