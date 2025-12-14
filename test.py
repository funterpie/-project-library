from Book import Book
from library import Library
from user import User

# Create Library
lib = Library("Taha Digital Library")

# Add Books
b1 = Book("48 Laws of Power", "Robert Greene", "B001", 5)
b2 = Book("Atomic Habits", "James Clear", "B002", 3)
lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)

# Create Users
u1 = User("Alice")
u2 = User("Bob")

# Borrow and Return
print(u1.borrow_book(lib, "B001"))
print(u2.borrow_book(lib, "B001"))  
print(u1.view_borrowed_books())     
print(u2.view_borrowed_books())         
print(lib.availablity_status("B001"))


# Return book
print(u1.return_book(lib, "B001"))
print(u1.view_borrowed_books())

# Display library books
print(lib.display_books())
