class Book:
    def __init__(self, title, author, dewey, isbn):
        self.title = title
        self.author = author
        self.dewey = dewey
        self.isbn = isbn
        self.avalible = True
        self.borrower = None
        book_list.append(self)

    def book_details(self):
        print(self.title)
        print(self.author)
        print(self.dewey)
        print(self.isbn)
        print(self.avalible)
        print(self.borrower)
        print("##################")


def print_info():
    for book in book_list:
        book.book_details()


class User:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.fees = 0.0
        self.borrowed_books = []
        user_list.append(self)

    def user_details(self):
        print("Name:", self.name)
        print("Address:", self.address)
        print("Fee: $", self.fees)
        print("##################")

def print_user():
    for user in user_list:
        user.user_details()

def add_user():
    name = input("Enter the new users name: ").title()
    address = input("Enter the new users address: ")
    User(name, address)
    print(name, address, "has been added to the user list")

def add_book():
    title = input("Enter the new books title: ").title()
    author = input("Who is the books author: ").title()
    dewey = input("Enter the books Dewey code: ").upper()
    isbn = input("Enter the books ISBN number: ")
    Book(title, author, dewey, isbn)
    print(f"{title} has been added to the book list")

def find_user():
    user_to_find = input("Enter the name of user: ").title()
    for user in user_list:
        if user.name == user_to_find:
            print(f"Hi {user_to_find}")
            return user
    print("Sorry, no user was found with that name")
    return None

def find_book():
    book_to_find = input("WHat book would you like to ")

# main routine
book_list = []
user_list = []
Book("Lord of the Rings", "J.R.R Tolkien", "TOL", "9780261103252")
Book("The Hunger Games", "Suzanne Collins", "COL", "9781407132082")
Book("A Tale Of Two Cities", "Charles Dickens", "DIC", "978185326247")
Book("Harry Potter", "J.K.Rowling", "ROW", "9780439321624")

User("John", "12 Example Street")
User("Susan", "1011 Binary Road")
User("Paul", "25 Appletree Drive")
User("Mary", "8 Moon Cres")

#print_user()
#print_info()
#add_user()
#print_user()
#add_book()
#print_info()
find_user()