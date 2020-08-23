import logging


# List supported programming languages in sonarqube
def getsupportedlanguages(s):
    endpoint = 'api/languages/list'
    supported_technologies = []
    try:
        json_response = s.get_request(endpoint)
        languages = json_response['languages']
        for technology in languages:
            supported_technologies.append(technology['name'])
        print(f'supported_technologies :\n {supported_technologies}')
        # for i in supported_technologies:
        #     print(i)
    except Exception as err:
        logging.error(err)
