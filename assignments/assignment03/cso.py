
import requests
import json

#get specific data
urlBegining = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd = "/JSON-stat/2.0/en"
def getAll(dataset):
    url = urlBegining + dataset + urlEnd
    response = requests.get(url)
    return response.json()

# create this json file in VSC
if __name__ =="__main__":
    with open("cso_data.json", "wt") as fp:
        print(json.dumps(getAll("FIQ02")), file=fp)
