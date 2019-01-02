'''
1. Enter book details
2. Display all books
3. Search by title
4. Exit
Please enter the choice: 1

Enter title:
Enter price:
Enter pages:

1. Enter book details
2. Display all books
3. Search by title
4. Exit
Please enter the choice: 2

Title: Book1
Price: 400
Pages: 300

Title: Book2
Price: 900
Pages: 400

1. Enter book details
2. Display all books
3. Search by title
4. Exit
Please enter the choice: 3

Enter title : Book1
Title: Book1
Price: 400
Pages: 300

1. Enter book details
2. Display all books
3. Search by title
4. Exit
Please enter the choice: 4
'''
from book import Book
import pickle

try:
  with open('data/book_list.pkl', mode='rb') as fp:
    books = pickle.load(fp)
except Exception:
  books = []

def getAndSave():
  title = input('Enter title : ')
  pages = int(input('Enter pages : '))
  price = float(input('Enter price : '))

  book = Book(title, price, pages)
  books.append(book)

def display():
  for book in books:
    print(book.get_details())

def persistData():
  with open('data/book_list.pkl', mode='wb') as fp:
    pickle.dump(books, fp)

while True:
  print('1. Enter book details\n2. Display all books\n3. Search by title\n4. Exit')
  choice = int(input('Please enter the choice : '))

  if choice == 1:
    getAndSave()
  elif choice == 2:
    display()
  elif choice == 3:
    pass
  else:
    persistData()
    break
