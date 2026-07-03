import json
import os

def load_books():
    if not os.path.exists("book.json"):
        return[]
    
    with open("book.json", "r") as file:
        if os.path.getsize("book.json") == 0:
            return[]
        
        return json.load(file)

def save_books(books):
    
    with open("book.json", "w") as file:
        json.dump(books, file, indent=4)
        
def print_book(book):
    print("----------------------------")
    print(f"ID: {book['id']}")
    print(f"Title: {book['title']}")
    print(f"Author: {book['author']}")
    print(f"Year: {book['year']}")
    if book['available']:
        status = "Yes"
    else:
        status = "No"
    print(f"Available: {status}")
    print("----------------------------")
    
def add_book():
    books = load_books()
    
    title = input("Enter Title: ")
    author = input("Enter Author Name: ")
    year = int(input("Enter Year: "))
    new_id = len(books) + 1
    
    book = {
        "id": new_id,
        "title": title,
        "author": author,
        "year": year,
        "available": True
    }
    
    books.append(book)
    
    save_books(books)
    print("Book added successfully!")
    
def view_books():
    books = load_books()
    
    if not books:
        print("No books found.")
        return
    
    for book in books:
        print_book(book)
       
        
def borrow_book():
    books = load_books()
    
    if not books:
        print("No books found.")
        return
    
    view_books()
    
    book_id = int(input("Enter book ID to borrow: "))
    if book_id < 1 or book_id > len(books):
        print("Invalied book ID!")
        return
    
    for i,book in enumerate(books):
        if book['id'] == book_id:
            if not book['available']:
                print("Book not available for borrowing.")
                return
            books[i]['available'] = False
            save_books(books)
            
            print(f"You have borrowed '{book['title']}' successfully!")
            return
        
def return_book():
    books = load_books()
    
    if not books:
        print("No books found.")
        return
    
    returned_book = int(input("Enter book ID to return: "))
    if returned_book < 1 or returned_book > len(books):
        print("Invalid book ID!")
        return
    
    for i , book in enumerate(books):
        if book['id'] == returned_book:
            if book['available']:
                print("This book is already avaliable in the library.")
                return
            
            books[i]['available'] = True
            save_books(books)
            
            print(f"You have returned '{book['title']}' successfully!")
            return
        
            
def search_book():
    books = load_books()
    
    if not books:
        print("No books found.")
        return
    
    search_title = input("Enter book title to search: ").lower()
    
    found = False
    
    for book in books:
        if search_title in book['title'].lower():
            print_book(book)
            found = True
    if not found:
        print("No books found with the given title.")
        
def delete_book():
    books = load_books()
    
    if not books:
        print("No books found.")
        return
    
    view_books()
    
    choice = int(input("Enter book ID to delete: "))
    if choice < 1 or choice > len(books):
        print("Invalid book ID!")
        return
    
    for i, book in enumerate(books):
        if book['id'] == choice:
            del books[i]
            save_books(books)
            print(f"Book '{book['title']}' deleted successfully!")
            return
            
            
     
    
    