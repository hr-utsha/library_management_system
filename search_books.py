def search_books(library):
    search_term = input("Enter search term (title or ISBN): ").lower()
    results = [book for book in library if search_term in book['title'].lower() or search_term in book['isbn']]
    if results:
        for book in results:
            authors = ', '.join(book['authors'])
            print(f"Title: {book['title']} | Authors: {authors} | ISBN: {book['isbn']} | Year: {book['year']} | Price: {book['price']} | Quantity: {book['quantity']}")
    else:
        print("No books found with the given search term.")
