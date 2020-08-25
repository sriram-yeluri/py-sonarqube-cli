import argparse
import sys

from sonar.groups import Groups
from sonar.languages import Languages
from utils.api import Api


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

    flags = parser.parse_args()
    if len(sys.argv) <= 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    return flags


if __name__ == '__main__':
    args = init_argument_parser()
    api_obj = Api(args.user, args.password, args.url, args.logLevel)

    if args.getgroups:
        Groups.getgroups(api_obj)

    if args.getlanguages:
        Languages.getsupportedlanguages(api_obj)

    sys.exit(0)