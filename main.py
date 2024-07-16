import add_book
import view_books
import search_books
import remove_book
import lend_book
import return_book
import save_restore

library = []
lent_books = []

# Restore data from file
save_restore.restore_library(library, lent_books)

menu_list = """
1. Add Book
2. View Books
3. Search Books
4. Remove Book
5. Lend Book
6. Return Book
7. Save Library
0. Exit
"""

while True:
    print(menu_list)
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        add_book.add_book(library)
        save_restore.save_library(library, lent_books)
    elif choice == 2:
        view_books.view_books(library)
    elif choice == 3:
        search_books.search_books(library)
    elif choice == 4:
        remove_book.remove_book(library)
        save_restore.save_library(library, lent_books)
    elif choice == 5:
        lend_book.lend_book(library, lent_books)
        save_restore.save_library(library, lent_books)
    elif choice == 6:
        return_book.return_book(library, lent_books)
        save_restore.save_library(library, lent_books)
    elif choice == 7:
        save_restore.save_library(library, lent_books)
    elif choice == 0:
        break
    else:
        print("Invalid choice. Please try again.")
