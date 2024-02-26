# 1.create private repository + Get your own API key for your GitHub account
# 2.Use curl to check that it works: curl -i -H "Authorization: token curl -i -H "AuthorizationL token "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" https://api.github.com/user/repos

import requests
import json
filename = "repos_private.json"

url = "https://api.github.com/repos/YuliiaRysinska/aprivateone"

apikey = "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"

response = requests.get(url, auth=('token',apikey))
repoJSON = response.json()
#print (response.status_code)
#print (response.json())

with  open(filename, 'w') as fp:
   json.dump(repoJSON, fp, indent=4)

