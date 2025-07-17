from tkinter import ttk, messagebox
from customtkinter import *
import database
import import_books

# GUI  
app = CTk()
app.geometry('1000x600')
app.title('Library Management System')

# TabView Setup
tabview = CTkTabview(app, width=950, height=580)
tabview.place(x=20, y=10)

add_tab = tabview.add("Add Book")
manage_tab = tabview.add("Manage Books")

# Entry Fields  
def create_entry(tab, label_text, x, y):
    CTkLabel(tab, text=label_text).place(x=x, y=y)
    entry = CTkEntry(tab, width=180)
    entry.place(x=x+100, y=y)
    return entry

bookIdEntry     = create_entry(add_tab, 'Book ID', 20, 20)
titleEntry      = create_entry(add_tab, 'Title', 20, 60)
authorEntry     = create_entry(add_tab, 'Author', 20, 100)
isbnEntry       = create_entry(add_tab, 'ISBN', 20, 140)
publisherEntry  = create_entry(add_tab, 'Publisher', 20, 180)
pagesEntry      = create_entry(add_tab, 'Pages', 20, 220)
stockEntry      = create_entry(add_tab, 'Stock', 20, 260)

# Functions 
def clear_entries():
    for entry in [bookIdEntry, titleEntry, authorEntry, isbnEntry, publisherEntry, pagesEntry, stockEntry]:
        entry.delete(0, END)

def refresh_books():
    books = database.fetch_books()
    tree.delete(*tree.get_children())
    for book in books:
        tree.insert('', END, values=book)

def add_book():
    if bookIdEntry.get() == '' or titleEntry.get() == '' or stockEntry.get() == '':
        messagebox.showerror('Error', 'Please fill all required fields')
        return
    try:
        database.insert_book(
            bookIdEntry.get(), titleEntry.get(), authorEntry.get(), isbnEntry.get(),
            publisherEntry.get(), int(pagesEntry.get()), int(stockEntry.get())
        )
        refresh_books()
        clear_entries()
        messagebox.showinfo('Success', 'Book Added!')
    except Exception as e:
        messagebox.showerror('Error', str(e))

def delete_book():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error', 'Please select a book to delete')
        return
    book_id = tree.item(selected_item[0])['values'][0]
    database.delete_book(book_id)
    refresh_books()
    messagebox.showinfo('Success', 'Book Deleted!')

def search_book():
    if SearchEntry.get() == '':
        messagebox.showerror('Error', 'Enter keyword to search')
        return
    field = searchBox.get()
    books = database.search_books_by(field, SearchEntry.get())
    tree.delete(*tree.get_children())
    for book in books:
        tree.insert('', END, values=book)

def import_books_gui():
    try:
        count = int(importEntry.get())
        keyword = keywordEntry.get()
        import_books.import_books_from_api(keyword, count)
        refresh_books()
        messagebox.showinfo('Success', 'Books Imported')
    except Exception as e:
        messagebox.showerror('Error', str(e))

# Buttons 
CTkButton(add_tab, text='Add Book', command=add_book).place(x=20, y=310)
CTkButton(add_tab, text='Delete Book', command=delete_book).place(x=150, y=310)

# Treeview
columns = ("Book ID", "Title", "Author", "ISBN", "Publisher", "Pages", "Stock")
tree = ttk.Treeview(manage_tab, columns=columns, show='headings', height=18)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120, anchor='center')

tree.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

scroll_y = ttk.Scrollbar(manage_tab, orient='vertical', command=tree.yview)
scroll_y.grid(row=0, column=3, sticky='ns')

scroll_x = ttk.Scrollbar(manage_tab, orient='horizontal', command=tree.xview)
scroll_x.grid(row=1, column=0, columnspan=3, sticky='ew')

tree.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

# Treeview Style
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", font=('Arial', 12, 'bold'), foreground='black', background='#cccccc')
style.configure("Treeview", font=('Arial', 11), rowheight=28, background="#f9f9f9",
                fieldbackground="#f9f9f9", foreground="black")
style.map("Treeview", background=[('selected', '#347083')])

# Search & Import 
searchBox = CTkComboBox(manage_tab, values=['title', 'author'], state='readonly', width=120)
searchBox.set('title')
searchBox.place(x=20, y=420)

SearchEntry = CTkEntry(manage_tab, width=200)
SearchEntry.place(x=160, y=420)

CTkButton(manage_tab, text='Search', command=search_book).place(x=380, y=420)
CTkButton(manage_tab, text='Show All', command=refresh_books).place(x=480, y=420)

CTkLabel(manage_tab, text='Import Count').place(x=20, y=470)
importEntry = CTkEntry(manage_tab, width=100)
importEntry.place(x=130, y=470)

CTkLabel(manage_tab, text='Keyword').place(x=250, y=470)
keywordEntry = CTkEntry(manage_tab, width=150)
keywordEntry.place(x=330, y=470)

CTkButton(manage_tab, text='Import Books', command=import_books_gui).place(x=500, y=470)

# Run app 
refresh_books()
app.mainloop()
