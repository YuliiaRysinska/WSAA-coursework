# 1. 1. install pyGithub: pip install PyGithub
#2. Test that your pyGithub works

# ok this is not exactly like I asked you to to in the labs
import requests
import json
from config import config as cfg

filename = "repos-private.json"

#url = 'https://api.github.com/repos/andrewbeattycourseware/datarepresentation/contents/code'
url = 'https://api.github.com/repos/andrewbeattycourseware/aprivateone'

# the more basic way of setting authorization
#headers = {'Authorization': 'token ' + apikey}
#response = requests.get(url, headers= headers)

apikey = cfg["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"]
response = requests.get(url, auth = ('token', apikey))

print (response.status_code)
#print (response.json())

with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)