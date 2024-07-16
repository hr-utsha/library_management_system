def lend_book(library, lent_books):
    search_term = input("Enter search term to lend (title or ISBN): ").lower()
    results = [book for book in library if search_term in book['title'].lower() or search_term in book['isbn']]
    if results:
        for index, book in enumerate(results):
            print(f"{index + 1} | Title: {book['title']} | ISBN: {book['isbn']} | Quantity: {book['quantity']}")
        choice = int(input("Enter the number of the book to lend: ")) - 1
        if 0 <= choice < len(results):
            book = results[choice]
            if book['quantity'] > 0:
                borrower = input("Enter the name of the borrower: ")
                book['quantity'] -= 1
                lent_books.append({
                    "title": book['title'],
                    "isbn": book['isbn'],
                    "borrower": borrower
                })
                print("Book lent successfully.")
            else:
                print("Not enough books available to lend.")
        else:
            print("Invalid selection.")
    else:
        print("No books found with the given search term.")
