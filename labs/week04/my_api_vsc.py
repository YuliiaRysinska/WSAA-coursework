# 1. Write the code to get the books
import requests
URL = "http://andrewbeatty1.pythonanywhere.com/books"

# 2. Write the function for "find all" and test it
def readBooks():
    response = requests.get(URL)
# we could do checking for correct response code here
    return response.json()

# 3. Write the function for "find by id" and test it 
def readBookById(id):
    geturl = URL + "/" + str(id)
    response = requests.get(geturl)
# we could do checking for correct response code here
    return response.json()

# 4. write the code to create and test it
def createBook(book):
    book= {
        'Author':'yuliasha',
        'Title': 'buuuuu',
        'Price': 666
    }
    response = requests.post(URL, json=book)
# should check we have the correct status code
    return response.json()

# 5. write update function
def updateBook(id, bookdiff):
    updateurl = URL + "/" + str(id)
    response = requests.put(updateurl, json=bookdiff)
    return response.json()

# 6. write delete function
def deleteBook(id):
    deleteurl = URL + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()

# end function + update
if __name__ == "__main__":
 # updating book   
    bookdiff= {
        'Price': 222
}
    # print(readBooks())
    # print(readBookById(505))
    # print(createBook({}))
    # print(updateBook(548, bookdiff))
    print(deleteBook(548))
    
    