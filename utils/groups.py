import logging

def getgroups(s):
    endpoint = 'api/user_groups/search'
    try:
        json_response = s.get_request(endpoint)
        # TO-DO : process the json_response
    except Exception as err:
        logging.error(err)

# Lists the groups a user belongs to
def searchusersingroups(s):
    endpoint = 'api/users/groups'
    response = s.get_request(endpoint)
    print(response.text)
