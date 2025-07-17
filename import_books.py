import requests, database

def import_books_from_api(title='', limit=20):
    books = []
    page = 1
    while len(books) < limit:
        response = requests.get(f'https://frappe.io/api/method/frappe-library?page={page}&title={title}')
        if response.status_code != 200:
            print('Error fetching data:', response.status_code)
            break

        data = response.json().get('message', [])
        if not data:
            print('No more books found.')
            break

        books.extend(data)
        page += 1

    books = books[:limit]

    inserted = 0
    for book in books:
        try:
            # Generates fallback ID
            book_id = book.get('isbn') or book.get('title', '').replace(' ', '_')[:20]

            title = book.get('title', 'Unknown')
            author = book.get('authors', 'Unknown')
            isbn = book.get('isbn', '')
            publisher = book.get('publisher', '')
            pages = int(book.get('num_pages') or 0)

            database.insert_book(
                book_id=book_id,
                title=title,
                author=author,
                isbn=isbn,
                publisher=publisher,
                pages=pages,
                stock=5
            )
            inserted += 1
            print(f"Imported: {title}")
        except Exception as e:
            print('Error inserting book:', e)

    print(f'Successfully inserted {inserted} books into database.')

   

