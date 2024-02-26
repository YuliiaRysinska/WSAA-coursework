# Create a pdf.
# Go to html2pdf.com and create an account for yourself and copy the API key.
#2. Write a script that will convert the Wikipedia website into a pdf
import requests
import urllib.parse
#3. put the api into a config file
from config import config as cfg

targetUrl = "https://en.wikipedia.org"

apiKey = cfg["htmltopdfkey"]
apiurl = "https://dash.html2pdf.app/api-keys"

params = {'url': targetUrl,'apiKey': apiKey}
parsedparams = urllib.parse.urlencode(params)
requestUrl = apiurl +"?" + parsedparams

response = requests.get(requestUrl)
print (response.status_code)

result =response.content
with open("document.pdf", "wb") as handler:
    handler.write(result)
