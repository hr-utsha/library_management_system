def remove_book(library):
    search_term = input("Enter search term to remove (title or ISBN): ").lower()
    results = [book for book in library if search_term in book['title'].lower() or search_term in book['isbn']]
    if results:
        for index, book in enumerate(results):
            print(f"{index + 1} | Title: {book['title']} | ISBN: {book['isbn']}")
        choice = int(input("Enter the number of the book to remove: ")) - 1
        if 0 <= choice < len(results):
            library.remove(results[choice])
            print("Book removed successfully.")
        else:
            print("Invalid selection.")
    else:
        print("No books found with the given search term.")
