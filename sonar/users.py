# Get API Calls

# POST API Calls
def createuser(s):
    endpoint = 'api/users/create'
    print('Create User method called')
    print(f'{s.username}\n{s.password}\n{s.baseurl}')


def deactivateuser(s):
    endpoint = 'api/users/deactivate'

# Get a list of active users
def getactiveusers(s):
    endpoint = 'api/users/search'

