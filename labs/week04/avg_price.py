#Write a program in another file that works out the average book price from all the books on the server
from my_api_vsc import readBooks

books = readBooks()

total = 0
count = 0
for book in books:  
    total +=book["Price"]
    count += 1
      
print('Average price of', count, 'books is', total/count)