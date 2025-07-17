import pymysql
from tkinter import messagebox

def connect_database():
    global mycursor, conn
    try:
        conn = pymysql.connect(host='localhost', user='root', password='root@123')
        mycursor = conn.cursor()
    except:
        messagebox.showerror('Error', 'Please open MySQL before running again')
        return

    mycursor.execute('CREATE DATABASE IF NOT EXISTS library')
    mycursor.execute('USE library')
    mycursor.execute('''CREATE TABLE IF NOT EXISTS books (
                        book_id VARCHAR(20),
                        title VARCHAR(255),
                        author VARCHAR(255),
                        isbn VARCHAR(20),
                        publisher VARCHAR(255),
                        pages INT,
                        stock INT)''')
    mycursor.execute('''CREATE TABLE IF NOT EXISTS members (
                        member_id VARCHAR(20),
                        name VARCHAR(50),
                        phone VARCHAR(15),
                        email VARCHAR(100),
                        total_debt DECIMAL(10,2))''')
    mycursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                        trans_id INT AUTO_INCREMENT PRIMARY KEY,
                        book_id VARCHAR(20),
                        member_id VARCHAR(20),
                        issue_date DATE,
                        return_date DATE,
                        fee DECIMAL(10,2))''')

def insert_book(book_id, title, author, isbn, publisher, pages, stock):
    mycursor.execute('INSERT INTO books VALUES (%s, %s, %s, %s, %s, %s, %s)', (book_id, title, author, isbn, publisher, pages, stock))
    conn.commit()

def fetch_books():
    mycursor.execute('SELECT * FROM books')
    return mycursor.fetchall()

def search_books_by(field, value):
    mycursor.execute(f'SELECT * FROM books WHERE {field} LIKE %s', ('%' + value + '%',))
    return mycursor.fetchall()

def update_book(book_id, title, author, isbn, publisher, pages, stock):
    mycursor.execute('''UPDATE books SET title=%s, author=%s, isbn=%s, publisher=%s, pages=%s, stock=%s WHERE book_id=%s''',
                     (title, author, isbn, publisher, pages, stock, book_id))
    conn.commit()

def delete_book(book_id):
    mycursor.execute('DELETE FROM books WHERE book_id=%s', (book_id,))
    conn.commit()

def insert_member(member_id, name, phone, email):
    mycursor.execute('INSERT INTO members VALUES (%s, %s, %s, %s, %s)', (member_id, name, phone, email, 0.00))
    conn.commit()

def fetch_members():
    mycursor.execute('SELECT * FROM members')
    return mycursor.fetchall()

def update_member_debt(member_id, new_debt):
    mycursor.execute('UPDATE members SET total_debt=%s WHERE member_id=%s', (new_debt, member_id))
    conn.commit()

def get_member_debt(member_id):
    mycursor.execute('SELECT total_debt FROM members WHERE member_id=%s', (member_id,))
    return mycursor.fetchone()[0]

def insert_transaction(book_id, member_id, issue_date, return_date, fee):
    mycursor.execute('INSERT INTO transactions(book_id, member_id, issue_date, return_date, fee) VALUES (%s, %s, %s, %s, %s)',
                     (book_id, member_id, issue_date, return_date, fee))
    conn.commit()

def update_stock(book_id, change):
    mycursor.execute('UPDATE books SET stock = stock + %s WHERE book_id = %s', (change, book_id))
    conn.commit()

connect_database()
