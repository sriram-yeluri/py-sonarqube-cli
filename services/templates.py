from utils.api import Api
import logging
import sys


class Templates(Api):

    def createtemplate(self):
        self.endpoint: str = 'api/permissions/create_template'
        if not self.template_name:
            logging.error('--templateName flag is missing')
            sys.exit(1)

        data = {'name': f'{self.template_name}', 'projectKeyPattern': 'com.example.abc.*'}
        self.payload = data
        self._post_params()
        if self.json_response:
            logging.info(self.json_response)
