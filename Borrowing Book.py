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

def print_info():
    for book in book_list:
        book.book_details()


def print_user():
    for user in user_list:
        user.user_details()

def add_user():
    name = input("Enter the new users name: ").title()
    address = input("Enter the new users address: ")
    User(name, address)
    print(f"{name} at {address} has been added to the user list")

def add_book():
    title = input("Enter the new books title: ").title()
    author = input("Who is the books author: ").title()
    dewey = input("Enter the books Dewey code: ").upper()
    isbn = input("Enter the books ISBN number: ")
    Book(title, author, dewey, isbn)
    print(f"{title} has been added to the book list")
    print()

def find_user():
    user_to_find = input("Enter the name of user: ").title()
    for user in user_list:
        if user.name == user_to_find:
            print(f"Hi {user_to_find}")
            return user
    print("Sorry, no user was found with that name")
    return None

def find_book():
    book_to_find = input("Enter name of book:  ")
    for book in book_list:
        if book.title == book_to_find:
            print(f"The book {book_to_find} is in our database")
        return book
    print("Sorry no book was found in that name")
    find_book()

def lend_book():
    user = find_user()
    print()
    if user:
        book = find_book()
        if book.avalible:
            confirm = input("Type 'Y' if you want to borrow this book: ")
            if confirm == "Y" or confirm == "y":
                print(f"The book {book.title} is now on loan to {user.name}")
            book.avalible = False
            book.borrower = user.name
            user.borrowed_books.append(book.title)
        else:
            print(f"Sorry {book.title} is already out on loan")

def return_book():
    user = find_user()
    print()
    if user:
        book = find_book()
        if book.title in user.borrowed_books:
            confirm = input(" Press 'Y' is you want to return this book: ")
            if confirm == "Y" or confirm == "y":
                print(f"{book.title} has been returned")
            book.avalible = True
            book.borrower = user.name
            user.borrowed_books.remove(book.title)
        else:
            print(f"Sorry {book.title} is already out on loan")

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

new_action = True
while new_action:
    print("##### Menu #####")
    print("1. Lend a book")
    print("2. Return a book")
    print("3. Add a user")
    print("4. Add a book")
    print("5. Exit")

    choice = input("What would you like to do \n"
                   " - Enter a number: ")

    if choice == "1":
        lend_book()
    elif choice == "2":
        return_book()
    elif choice == "3":
        add_user()
    elif choice == "4":
        add_book()
    elif choice == "5":
        print("Goodbye")
        new_action = False
    else:
        print("*** Sorry that is not a valid option *** ")
