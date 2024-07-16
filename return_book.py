def return_book(library, lent_books):
    search_term = input("Enter search term to return (title or ISBN): ").lower()
    results = [book for book in lent_books if search_term in book['title'].lower() or search_term in book['isbn']]
    if results:
        for index, book in enumerate(results):
            print(f"{index + 1} | Title: {book['title']} | ISBN: {book['isbn']} | Borrower: {book['borrower']}")
        choice = int(input("Enter the number of the book to return: ")) - 1
        if 0 <= choice < len(results):
            lent_book = results[choice]
            for book in library:
                if book['title'] == lent_book['title'] and book['isbn'] == lent_book['isbn']:
                    book['quantity'] += 1
            lent_books.remove(lent_book)
            print("Book returned successfully.")
        else:
            print("Invalid selection.")
    else:
        print("No lent books found with the given search term.")
