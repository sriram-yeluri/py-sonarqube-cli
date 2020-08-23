# Sonarqube CLI
This is a python implementation of sonarqube-cli.

# How to use the sonarqube-cli

```sh
python3 sonarqube-cli.py -h
usage: sonarqube-cli.py [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                        [-u USER] [-p PASSWORD] [-url URL] [--createuser]
                        [--getgroups] [--getlanguages]

optional arguments:
  -h, --help            show this help message and exit
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --log {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        Set the logging level
  -u USER, --user USER  Login ID of User
  -p PASSWORD, --password PASSWORD
                        Login Password
  -url URL, --url URL   Sonarqube URL
  --createuser          Create sonarqube user
  --getgroups           Get sonarqube groups
  --getlanguages        Get sonarqube supported languages
```

### References
[Sonarqube Web API](http://localhost:9000/web_api)