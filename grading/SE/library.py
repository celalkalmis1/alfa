from typing import List, Optional
from abc import ABC, abstractmethod

class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def check_out(self) -> bool:
        # If the book is available, mark it as borrowed
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_book(self) -> None:
        # Mark the book as available again
        self.is_available = True


class User(ABC):
    def __init__(self, name: str, user_id: str):
        self.name = name
        self.user_id = user_id

    @abstractmethod
    def get_details(self) -> str:
        pass


class Member(User):
    def __init__(self, name: str, user_id: str):
        super().__init__(name, user_id)
        self.borrowed_books: List[Book] = []

    def get_details(self) -> str:
        return f"Member: {self.name}, ID: {self.user_id}"

    def borrow_book(self, book: Book) -> None:
        # Member borrows the book
        if book.check_out():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is not available.")

    def return_book(self, book: Book) -> None:
        # Member returns the book
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")


class Librarian(User):
    def __init__(self, name: str, user_id: str, employee_id: str):
        super().__init__(name, user_id)
        self.employee_id = employee_id

    def get_details(self) -> str:
        return f"Librarian: {self.name}, Employee ID: {self.employee_id}"

    def add_book_to_library(self, library: 'Library', book: Book) -> None:
        # Librarian adds a book to the library system
        library.add_book(book)
        print(f"Librarian {self.name} added '{book.title}'.")


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books: List[Book] = []
        self.members: List[Member] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def register_member(self, member: Member) -> None:
        self.members.append(member)
        print(f"Member '{member.name}' registered to {self.name}.")

    def search_book(self, title: str) -> Optional[Book]:
        # Search book by title
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None


# --- TEST SECTION (MAIN) ---
if __name__ == "__main__":
    # Setup Library and Librarian
    school_library = Library("School Library")
    librarian = Librarian("Madam Pince", "U01", "EMP-01")

    # Create a book and add to library
    book1 = Book("Python 101", "John Doe", "123456")
    librarian.add_book_to_library(school_library, book1)

    # Register a member
    student = Member("Harry", "M01")
    school_library.register_member(student)

    # Member searches and borrows the book
    found_book = school_library.search_book("Python 101")
    if found_book:
        student.borrow_book(found_book)

    # Member returns the book (This is what you asked to add)
    student.return_book(book1)