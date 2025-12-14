# file 3: user.py
# manages all the users and connects them to library

import json
import os
from library import Library  # import  Library class
from Book import Book         

class User:
    all_users = []  # acts as DB, also saved in JSON

    def __init__(self, username, is_admin=False, file_path="users_db.json"):
        """
        Initialize a new user.
        Args:
            username (str): Unique username
            is_admin (bool): True if admin, False if regular user
            file_path (str): JSON file path to save/load users
        """
        self.username = username
        self.borrowed_books = []  # store borrowed Book objects
        self.file_path = file_path
        self.is_admin = is_admin

        
        if any(user.username == username for user in User.all_users):
            raise ValueError("Username already exists. Please choose a different username.")

        
        User.all_users.append(self)
    def borrow_book(self, library: Library, book_id):
        """
        Borrow a book from the library.
        """
        success, message = library.borrow_book(book_id)
        if success:
            self.borrowed_books.append(library.books[book_id])
            self.save_users()
        return success, message

    def return_book(self, library: Library, book_id):
        """
        Return a borrowed book to the library.
        """
        success, message = library.return_book(book_id)
        if success:
            self.borrowed_books = [b for b in self.borrowed_books if b.book_id != book_id]
            self.save_users()
        return success, message

    def view_borrowed_books(self):
        """
        Display borrowed books for this user.
        """
        if not self.borrowed_books:
            return "You have not borrowed any books."
        return "\n".join(str(book) for book in self.borrowed_books)

    
    def to_dict(self):
        return {
            "username": self.username,
            "borrowed_books": [book.book_id for book in self.borrowed_books],
            "is_admin": self.is_admin,
        }

# Admin-only 
    @staticmethod
    def admin_login(password):
        """
        Admin login with a predefined security code.
        """
        security_code = "Taha1502"
        if password == security_code:
            return True, "Admin logged in successfully."
        else:
            return False, "Access denied: Wrong password password i awialble in Main.py Readdme.Md."

    # ===== Admin-only Class Methods =====
    @classmethod
    def add_user(cls, username, is_admin=False, file_path="users_db.json"):
        """
         add a new user.
        """
        user = User(username, is_admin=is_admin, file_path=file_path)
        cls.save_users()
        return user

    @classmethod
    def remove_user(cls, username):
        """
         remove a user.
        """
        user = next((u for u in cls.all_users if u.username == username), None)
        if user:
            cls.all_users.remove(user)
            cls.save_users()
            return True, f"User '{username}' removed successfully."
        return False, "User not found."

    @classmethod
    def remove_book(cls, library: Library, book_id):
        """
         remove a book from the library.
        """
        if book_id in library.books:
            del library.books[book_id]
            library.save_books()
            return True, f"Book '{book_id}' removed successfully."
        return False, "Book not found."

    @classmethod
    def all_users_list(cls):
        """
        view all users.
        """
        if not cls.all_users:
            return "No users found."
        return "\n".join([f"{u.username} (Admin: {u.is_admin})" for u in cls.all_users])


    @classmethod
    def save_users(cls):
        """
        Save all users to JSON file.
        """
        data = {user.username: user.to_dict() for user in cls.all_users}
        with open(cls.all_users[0].file_path if cls.all_users else "users_db.json", "w") as f:
            json.dump(data, f, indent=4)

    @classmethod
    def load_users(cls, library: Library, file_path="users_db.json"):
        """
        Load users from JSON file and reconnect borrowed books with the library.
        """
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                data = json.load(f)
                for username, user_data in data.items():
                    
                    if any(u.username == username for u in cls.all_users):
                        continue 
                    user = User(
                        username,
                        is_admin=user_data.get("is_admin", False),
                        file_path=file_path
                    )
                    
                    user.borrowed_books = [
                        library.books[book_id] for book_id in user_data.get("borrowed_books", [])
                        if book_id in library.books
                    ]
