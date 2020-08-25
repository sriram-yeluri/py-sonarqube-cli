import logging

from utils.api import Api


class Languages(Api):

    # List supported programming languages in sonarqube
    def getsupportedlanguages(self):
        self.endpoint = 'api/languages/list'
        supported_technologies = []
        try:
            # self.json_response = self._get()
            self._get()
            if self.json_response is not None:
                languages = self.json_response['languages']
                for technology in languages:
                    supported_technologies.append(technology['name'])
                print(f'supported_technologies :\n {supported_technologies}')
            # for i in supported_technologies:
            #     print(i)
        except Exception as err:
            logging.error(err)
            print('Check sonar-cli.log')
