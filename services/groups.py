import logging

from utils.api import Api


class Groups(Api):

    def getgroups(self):
        self.endpoint = 'api/user_groups/search'
        try:
            self._get()
            if self.json_response:
                logging.info(self.json_response)
            # TO-DO : process the json_response
        except Exception as err:
            logging.error(err)

    # Lists the groups a user belongs to
    def searchusersingroups(self):
        self.endpoint = 'api/users/groups'
        self._get()
        if not self.json_response:
            logging.info(self.json_response)
