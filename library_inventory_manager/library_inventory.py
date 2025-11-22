import json
import os

# Book class
class Book:
    def __init__(self, title, author, isbn, status="Available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def issue(self):
        if self.status == "Available":
            self.status = "Issued"
            print("Book issued successfully.")
        else:
            print("Book is already issued.")

    def return_book(self):
        if self.status == "Issued":
            self.status = "Available"
            print("Book returned successfully.")
        else:
            print("Book was not issued.")

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {self.status}"

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }

# File name for storing data
CATALOGUE_FILE = "library_catalogue.json"

# Function to load data
def load_catalogue():
    try:
        if os.path.exists(CATALOGUE_FILE):
            with open(CATALOGUE_FILE, "r") as f:
                data = json.load(f)
                return [Book(**item) for item in data]
        else:
            print("No previous data found. Starting with an empty catalogue.")
            return []
    except (IOError, json.JSONDecodeError) as e:
        print("Error while loading file:", e)
        return []
    finally:
        pass

# Function to save data
def save_catalogue(catalogue):
    try:
        with open(CATALOGUE_FILE, "w") as f:
            json.dump([book.to_dict() for book in catalogue], f, indent=4)
    except IOError as e:
        print("Error while saving file:", e)
    finally:
        pass

# Add new book
def add_book(catalogue):
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    isbn = input("Enter ISBN: ")

    for book in catalogue:
        if book.isbn == isbn:
            print("Book with this ISBN already exists.")
            return

    new_book = Book(title, author, isbn)
    catalogue.append(new_book)
    print("Book added successfully.")

# Search book
def search_book(catalogue):
    keyword = input("Enter title keyword to search: ").lower()
    results = [book for book in catalogue if keyword in book.title.lower()]

    if results:
        print("\nSearch Results:")
        for book in results:
            print(book)
    else:
        print("No matching book found.")

# Issue book
def issue_book(catalogue):
    isbn = input("Enter ISBN to issue: ")
    for book in catalogue:
        if book.isbn == isbn:
            book.issue()
            return
    print("Book not found.")

# Return book
def return_book(catalogue):
    isbn = input("Enter ISBN to return: ")
    for book in catalogue:
        if book.isbn == isbn:
            book.return_book()
            return
    print("Book not found.")

# Display all books
def display_all_books(catalogue):
    if not catalogue:
        print("No books in the catalogue.")
    else:
        print("\nLibrary Catalogue:")
        for book in catalogue:
            print(book)

# Menu-driven system
def main():
    catalogue = load_catalogue()

    while True:
        print("\nLibrary Inventory Manager")
        print("1. Add New Book")
        print("2. Search Book by Title")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Display All Books")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_book(catalogue)
        elif choice == "2":
            search_book(catalogue)
        elif choice == "3":
            issue_book(catalogue)
        elif choice == "4":
            return_book(catalogue)
        elif choice == "5":
            display_all_books(catalogue)
        elif choice == "6":
            save_catalogue(catalogue)
            print("Catalogue saved. Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

        # Save data after each operation
        save_catalogue(catalogue)


if __name__ == "__main__":
    main()
