from typing import List, Optional
from abc import ABC, abstractmethod

class Book:
    
    
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def check_out(self) -> bool:
        
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_book(self) -> None:
       
        self.is_available = True

    def __str__(self) -> str:
        status = "Available" if self.is_available else "Checked Out"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {status}"


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
        return f"Member: {self.name}, ID: {self.user_id}, Borrowed Books: {len(self.borrowed_books)}"

    def borrow_book(self, book: Book) -> None:
        
        if book.check_out():
            self.borrowed_books.append(book)
            print(f"{self.name} successfully borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is currently not available.")

    def return_book(self, book: Book) -> None:
       
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} successfully returned '{book.title}'.")
        else:
            print(f"{self.name} does not have '{book.title}'.")


class Librarian(User):

    
    def __init__(self, name: str, user_id: str, employee_id: str):
        super().__init__(name, user_id)
        self.employee_id = employee_id

    def get_details(self) -> str:
        return f"Librarian: {self.name}, Employee ID: {self.employee_id}"

    def add_book_to_library(self, library: 'Library', book: Book) -> None:
        """Adds a new book to the specific library."""
        library.add_book(book)
        print(f"Librarian {self.name} added '{book.title}' to the library.")


class Library:
    """Represents the library containing books and members."""
    
    def __init__(self, name: str):
        self.name = name
        self.books: List[Book] = []
        self.members: List[Member] = []

    def add_book(self, book: Book) -> None:
        """Adds a book to the library's collection."""
        self.books.append(book)

    def register_member(self, member: Member) -> None:
        """Registers a new member to the library."""
        self.members.append(member)
        print(f"Member '{member.name}' has been registered to {self.name}.")

    def search_book(self, title: str) -> Optional[Book]:
        """Searches for a book by its title."""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None


if __name__ == "__main__":

    city_library = Library("Hogwarts Library")

    librarian = Librarian("Madam Pince", "U001", "EMP-991")
    book1 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", "9780590353427")
    book2 = Book("The Lord of the Rings: The Fellowship of the Ring", "J.R.R. Tolkien", "9780544003415")

    librarian.add_book_to_library(city_library, book1)
    librarian.add_book_to_library(city_library, book2)

    # 4. Register