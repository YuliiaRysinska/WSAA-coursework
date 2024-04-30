# program read a file from a repository, replace all the instances of the text "Andrew" with your name. 
# program should then commit those changes and push the file back to the repository (You will need authorisation to do this).

import requests
import json

#filename = "repos-public.json"
filename = "wsaa_code.json"


url = 'https://api.github.com/repos/andrewbeattycourseware/wsaa-course-material/contents/code'
# try to change name in url
#new_url = url.replace("andrebeatty", replace_with="yuliia")


response = requests.get(url)
print (response.status_code)
repoJSON = response.json()
#print (response.json())

with  open(filename, 'w') as fp:
    json.dump(repoJSON, fp, indent=4)
    