from utils.api import Api


class Users(Api):

    def createuser(self):
        self.endpoint = 'api/users/create'

    def deactivateuser(self):
        self.endpoint = 'api/users/deactivate'

    # Get a list of active users
    def getactiveusers(self):
        self.endpoint = 'api/users/search'
        self._get()
