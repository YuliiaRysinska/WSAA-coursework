# 1.How would you get all books: 
#curl http://andrewbeatty1.pythonanywhere.com/books

# 2 How would you get the book with id 17
#curl http://andrewbeatty1.pythonanywhere.com/books/17

# 3. For the same website how would you use curl to create book, NOTE the id of the book you made. You can test if your book is there using the find by id.
#curl -H "Content-Type:application/json" -X POST -d "{\"Title\":\"xxx\",\"Author\":\"xxx\",\"Price\":3000}" http://andrewbeatty1.pythonanywhere.com/books

# 4  update a book

# curl -H "Content-Type:application/json" -X PUT -d "{\"Price\":2000}" http://andrewbeatty1.pythonanywhere.com/books/???

# 5  delete the book you just made
# curl -X DELETE http://andrewbeatty1.pythonanywhere.com/books/??

# 6. Try doing the same with postman

# 7.Try using curl on to get the bitcoin JSON and other site
