import logging


class Config:
    def __init__(self):
        self._defaults()
        self._logging()

    def _defaults(self):
        self.user = None
        self.password = None
        self.url = None
        self.loglevel: str = 'INFO'
        self.template_name = ''

    def _logging(self):
        logging.basicConfig(
            format='%(levelname)s %(asctime)s : [%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p',
            level=getattr(logging, self.loglevel),
            filename='sonarqube-cli.log')

    def set_args(self, args):
        self.user = args.user
        self.password = args.password
        self.url = args.url
        self.loglevel = args.logLevel
        self.template_name = args.templateName

