def view_books(library):
    if not library:
        print("No books available.")
    else:
        for index, book in enumerate(library):
            authors = ', '.join(book['authors'])
            print(f"{index + 1} | Title: {book['title']} | Authors: {authors} | ISBN: {book['isbn']} | Year: {book['year']} | Price: {book['price']} | Quantity: {book['quantity']}")
