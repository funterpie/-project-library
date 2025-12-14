# 📚 Taha Library System

**Developed By:** M Taha Sattar  
**Project Type:** Digital Library Management System (Streamlit)  
**Purpose:** To manage library books digitally with user login, borrowing, and admin functionalities.

---

## 📝 Overview

Taha Library System is a digital library app built with **Python** and **Streamlit**, implementing **Object-Oriented Programming (OOP)** principles.  

Users can:  
- Browse and search for books  
- Borrow and return books  
- View their borrowed books  

Admins can:  
- Add new books  
- View all registered users  
- Remove users or books  

All data is **persisted in JSON files**, so the library and user data remain between sessions.

---

## ⚙️ Features

### User Features:
1. View all books in the library  
2. Search books by **Title** or **Author**  
3. Borrow books (updates available copies)  
4. Return borrowed books  
5. View personal borrowed books  

### Admin Features:
1. Add new books with `Title`, `Author`, `Book ID`, and total copies  
2. View all registered users  
3. Remove a user  
4. Remove a book  

### Security:
- Admin login requires a password.  
- Users register with a unique username.  

**Admin Password:** `Taha1502`

---

## 🛠️ Requirements

- Python 3.9+  
- Streamlit (`pip install streamlit`)  

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd <repo-folder>
