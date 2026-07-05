from tools import add_book, view_books, borrow_book, return_book, delete_book,search_book,count_books
import os

while True:
    print("Library Management System")
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Delete Book")
    print("6. Search Books")
    print("7. Count Books")
    print("8. Exit")


    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        add_book()
    elif choice == '2':
        view_books()
    elif choice == '3':
        borrow_book()
    elif choice == '4':
        return_book()
    elif choice == '5':
        delete_book()
    elif choice == '6':
        search_book()
    elif choice == '7':
        count_books()
    elif choice == '8':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice! Please try again.")
    
    input("\nPress Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')