import argparse

from utils import sonar, users, groups


def init_argument_parser(argument_list=None):
    parser = argparse.ArgumentParser()

    parser.add_argument('--verbose', action='store_true', help='Increase verbosity')

    parser.add_argument('-u', '--user', action='store', default='admin',
                        required=False, help='Login ID of User')

    parser.add_argument('-p', '--password', action='store', default='admin',
                        required=False, help='Login Password')

    parser.add_argument('-url', '--url', action='store', default='http://localhost:9000',
                        required=False, help='Sonarqube URL')

    parser.add_argument('--createuser', action='store_true', default=False, help='Create sonarqube user')

    parser.add_argument('--getgroups', action='store_true', default=False, help='Get sonarqube groups')
    return parser.parse_args()


if __name__ == '__main__':
    args = init_argument_parser()
    s = sonar.Sonar(args.user, args.password, args.url)

    if args.getgroups:
        groups.getgroups(s)

