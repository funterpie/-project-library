# app_dashboard.py
import streamlit as st
from library import Library
from Book import Book
from user import User

st.set_page_config(page_title="Taha Library System", layout="wide")
library = Library("Taha Library System")
User.load_users(library)

# ------------------ SESSION STATE ------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = None
if "is_admin" not in st.session_state:
    st.session_state.is_admin = False

#  LOGIN / REGISTER 
def login(username, password=None, admin=False):
    if admin:
        success, msg = User.admin_login(password)
        if success:
            st.session_state.logged_in = True
            st.session_state.is_admin = True
            st.success(msg)
        else:
            st.error(msg)
    else:
        user = next((u for u in User.all_users if u.username == username), None)
        if user:
            st.session_state.user = user
            st.session_state.logged_in = True
            st.success(f"Welcome {username} Click Login Button Again")
        else:
            st.error("User not found. Please register first.")

def register(username):
    try:
        User.add_user(username)
        st.success(f"User '{username}' registered successfully! You can now login.")
    except ValueError as e:
        st.error(str(e))

def logout():
    st.session_state.clear()
    st.success("Logged out! Thanks for using Taha Library.")

# Admin Panel
def admin_panel():
    st.sidebar.subheader("Admin Actions")
    option = st.sidebar.radio("Choose Action", ["Add Book", "View Users", "Remove User", "Remove Book"])

    if option == "Add Book":
        st.subheader("Add a New Book")
        title = st.text_input("Book Title")
        author = st.text_input("Author")
        book_id = st.text_input("Book ID")
        copies = st.number_input("Copies", min_value=1, value=1)
        if st.button("Add Book"):
            book = Book(book_id=book_id, title=title, author=author, total_copies=copies)
            success, msg = library.add_book(book)
            if success:
                st.success(msg)
            else:
                st.error(msg)

    elif option == "View Users":
        st.subheader("All Users")
        st.text(User.all_users_list())

    elif option == "Remove User":
        st.subheader("Remove User")
        username_remove = st.text_input("Enter Username to Remove")
        if st.button("Remove User"):
            success, msg = User.remove_user(username_remove)
            if success:
                st.success(msg)
            else:
                st.error(msg)

    elif option == "Remove Book":
        st.subheader("Remove Book")
        book_remove = st.text_input("Enter Book ID to Remove")
        if st.button("Remove Book"):
            success, msg = User.remove_book(library, book_remove)
            if success:
                st.success(msg)
            else:
                st.error(msg)

# ------------------ USER PANEL ------------------
def user_panel():
    st.sidebar.subheader(f"Welcome, {st.session_state.user.username}")
    menu = st.sidebar.radio("Menu", ["All Books", "Search Books", "Borrow Book", "Return Book", "My Borrowed Books"])

    if menu == "All Books":
        st.subheader("Library Books")
        if not library.books:
            st.warning("No books available in library.")
        else:
            for book in library.books.values():
                st.info(f"**{book.title}** by {book.author} | ID: {book.book_id} | Available: {book.available_copies}")

    elif menu == "Search Books":
        st.subheader("Search Books with Title or Author")
        option = st.radio("Search by", ["Title", "Author"], horizontal=True)
        query = st.text_input("Enter search text")
        if st.button("Search"):
            results = library.search_with_title(query) if option == "Title" else library.search_with_author(query)
            if results:
                for book in results:
                    st.success(f"**{book.title}** by {book.author} | ID: {book.book_id} | Available: {book.available_copies}")
            else:
                st.warning("No matching books found.")

    elif menu == "Borrow Book":
        st.subheader("Borrow Book")
        borrow_id = st.text_input("Book ID to Borrow")
        if st.button("Borrow Selected Book"):
            success, msg = st.session_state.user.borrow_book(library, borrow_id)
            if success:
                st.success(msg)
            else:
                st.error(msg)

    elif menu == "Return Book":
        st.subheader("Return Book")
        return_id = st.text_input("Book ID to Return")
        if st.button("Return Selected Book"):
            success, msg = st.session_state.user.return_book(library, return_id)
            if success:
                st.success(msg)
            else:
                st.error(msg)

    elif menu == "My Borrowed Books":
        st.subheader("Your Borrowed Books")
        borrowed_books = st.session_state.user.borrowed_books
        if not borrowed_books:
            st.info("You have not borrowed any books.")
        else:
            for book in borrowed_books:
                st.success(f"**{book.title}** by {book.author} | ID: {book.book_id}")

# ------------------ MAIN APP LOGIC ------------------
st.title("📚 Taha Library Dashboard")

if not st.session_state.logged_in:
    st.subheader("Login or Register")
    login_type = st.radio("Login as", ["User", "Admin"])
    
    if login_type == "Admin":
        password_input = st.text_input("Admin Password", type="password")
        if st.button("Login as Admin"):
            login(username="Admin", password=password_input, admin=True)
    else:
        username_input = st.text_input("Username")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Login as User"):
                login(username_input)
        with col2:
            if st.button("Register"):
                register(username_input)
else:
    st.sidebar.button("Logout", on_click=logout)
    if st.session_state.is_admin:
        admin_panel()
    else:
        user_panel()
