import json
import os
from Book import Book
#imported BOok file and clas to get all datra 


class Library:

    #stores all ifo related library
    def __init__(self, name, file_path= "library_db.json"):
        self.name =  name
        self.books = {}
        self.file_path = file_path
        self.load_books()
        # db upgraded to json from disc
    def save_books(self):
        data = {book_id: book.to_dict() for book_id, book in self.books.items()}
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)
    def load_books(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                for book_id, book_data in data.items():
                    self.books[book_id] = Book.from_dict(book_data)           

    def add_book(self, book):
        if book.book_id in self.books:
            return False ,f"book with book id you provided {book.book_id} already exssts in our data base"
        
        else:
            self.books[book.book_id] = book
            self.save_books()
            return True , f"book with book id {book.book_id} added successfully"

    #search book with help of title
    def search_with_title(self, title):
        test = []
        for book in self.books.values():
            if book.title.lower() == title.lower():
                test.append(book)
        return test if test else None

    # search book with author name
    def search_with_author(self, author):
        test = []
        for book in self.books.values():
            if book.author.lower() == author.lower():
                test.append(book)
        return test if test else None

    def borrow_book(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            if book.borrow_book():
                self.save_books()
                return True , f"You have successfully borrowed the book: {book.title}"
            else:
                return False , "Sorry, this book is currently not available."
        else:
            return False , "Book ID not found in the library."

    def return_book(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            if book.return_book():
                self.save_books()
                return True , f"You have successfully returned the book: {book.title}"
            else:
                return False , "trouble returning the book. Please check the details."
        else:
            return False , "Book ID not found in the dB."

    def display_books(self):
        if not self.books:
            return "No books available in the library."
        return "\n".join(str(book) for book in self.books.values())
    def  availablity_status(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            return f"Available copies of '{book.title}': {book.available_copies}"
        else:
            return "Book ID not found in the library."