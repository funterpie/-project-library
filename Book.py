#project library
# in the name of allah the most gracious the most merciful
# bismillahir rahmanir rahim

class Book :
    #  stores all info related book
    def __init__(self, title , author , book_id ,total_copies ,  available_copies=None):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.total_copies = total_copies
        self.available_copies = available_copies if available_copies is not None else total_copies
        #here i maked available copis optional becouse intialy new copis will all available
    def borrow_book(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        else:
            return False
    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        else:       
            return False

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "book_id": self.book_id,
            "total_copies": self.total_copies,
            "available_copies": self.available_copies,
        }
    @classmethod
    def from_dict( cls, data):
        return cls(
            title=data["title"],
            author=data["author"],
            book_id=data["book_id"],
            total_copies=data["total_copies"],
            available_copies=data["available_copies"],
        )
    # till here we created two meathod for borowing an dreturn book now er are creating an info meathod whre we can see all info related to book
    # this meathod will return a string containing all the info related to book
    # thats why used __str_ meathod i learned now about 
    #  update firtly i was using simple disc now moved to JSON  thats why i add disc meathod and dicoratetr
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Book ID: {self.book_id}, Total Copies: {self.total_copies}, Available Copies: {self.available_copies}"
    


# now tes is it working or am i idiot haha 
# book_test = Book("48 Laws of Power", "Robert Greene", "B001", 5)
# print(book_test)
# # now other meathod
# book_test.borrow_book()
# print(book_test)
# print(book_test.available_copies)

# # next
# book_test.return_book()
# print(book_test)
# print(book_test.available_copies)

# #  checking if we we borrowe all copis
# for _ in range(6):
#     book_test.borrow_book()
# print(book_test)