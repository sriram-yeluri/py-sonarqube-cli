import argparse
import sys

from services.groups import Groups
from services.languages import Languages
from services.templates import Templates
from utils.config import Config


def init_argument_parser(argument_list=None):
    parser = argparse.ArgumentParser()

    parser.add_argument("-l", "--log", dest="logLevel", choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        help="Set the logging level", default='INFO')

    parser.add_argument('-u', '--user', action='store', default='admin',
                        required=False, help='Login ID of User')

    parser.add_argument('-p', '--password', action='store', default='admin',
                        required=False, help='Login Password')

    parser.add_argument('-url', '--url', action='store', default='http://localhost:9000',
                        required=False, help='Sonarqube URL')

    parser.add_argument('--createuser', action='store_true', default=False, help='Create sonarqube user')

    parser.add_argument('--getgroups', action='store_true', default=False, help='Get sonarqube groups')

    parser.add_argument('--getlanguages', action='store_true', default=False, help='Get sonarqube supported languages')

    parser.add_argument('-templateName', '--templateName', action='store', default=None,
                        required=False, help='Permission Template Name')

    parser.add_argument('--createTemplate', action='store_true', default=False, help='Create Permission Template')

    flags = parser.parse_args()
    if len(sys.argv) <= 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    return flags


def main():
    args = init_argument_parser()
    config = Config()
    config.set_args(args)

    if args.getgroups:
        Groups(config).getgroups()
    if args.getlanguages:
        Languages(config).getsupportedlanguages()
    if args.createTemplate:
        Templates(config).createtemplate()


if __name__ == '__main__':
    main()
    sys.exit(0)
