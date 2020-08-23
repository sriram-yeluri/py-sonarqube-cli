import requests

def getgroups(s):

    endpoint = 'api/user_groups/search'
    url = f'{s.baseurl}/{endpoint}'
    payload = ""
    headers = {'authorization': 'Basic YWRtaW46YWRtaW4='}
    response = requests.request("GET", url, data=payload, headers=headers)
    print(response.text)

