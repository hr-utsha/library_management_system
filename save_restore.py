import csv

def save_library(library, lent_books):
    with open("library_data.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "Title", "Authors", "ISBN", "Year", "Price", "Quantity", "Borrower"])
        for book in library:
            writer.writerow(["Library", book['title'], ','.join(book['authors']), book['isbn'], book['year'], book['price'], book['quantity'], ""])
        for book in lent_books:
            writer.writerow(["Lent", book['title'], "", book['isbn'], "", "", "", book['borrower']])

def restore_library(library, lent_books):
    try:
        with open("library_data.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if row[0] == "Library":
                    book = {
                        "title": row[1],
                        "authors": row[2].split(','),
                        "isbn": row[3],
                        "year": row[4],
                        "price": float(row[5]),
                        "quantity": int(row[6])
                    }
                    library.append(book)
                elif row[0] == "Lent":
                    lent_book = {
                        "title": row[1],
                        "isbn": row[3],
                        "borrower": row[7]
                    }
                    lent_books.append(lent_book)
    except FileNotFoundError:
        print("No saved library data found. Starting with an empty library.")
