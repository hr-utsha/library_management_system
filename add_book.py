def add_book(library):
    title = input("Enter title: ")
    authors = input("Enter authors (comma-separated): ").split(',')
    isbn = input("Enter ISBN: ")
    year = input("Enter publishing year: ")
    while True:
        try:
            price = float(input("Enter price: "))
            break
        except ValueError:
            print("Invalid input. Price should be a number.")
    quantity = int(input("Enter quantity: "))

    book = {
        "title": title,
        "authors": authors,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity
    }
    library.append(book)
    print("Book added successfully.")
