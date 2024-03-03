# 9. Make a basic server in it and test it
from flask import Flask, url_for, request, redirect, abort
app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    return "hello"

#Modify the Flask Server to deal with the required URL mappings 
#10. Create a mapping and function for each of the possible API calls
@app.route('/books', methods=['GET'])
def getall():
    return "get all"

@app.route('/books/<int:id>', methods=['GET'])
def findbyid(id):
    return "find by id"
#create
@app.route('/books', methods=['POST'])
def create():
# read json from the body
    jsonstring = request.json
    return f"create {jsonstring}"
# update
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    jsonstring = request.json
    return f"update {id} {jsonstring}"
#delete
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    return f"delete {id}"

if __name__ == "__main__":
    app.run(debug=True)
#11. Using either postman or CURL test each of your endpoints
