# Library-Managament-System
# 📚 Library Management System (Desktop GUI App)

A desktop-based Library Management System built using `customtkinter` for the GUI, `MySQL` for the backend database, and `Pillow` for image handling. It provides book management features with an intuitive user interface and optional integration with the [Frappe API](https://frappe.io/api/method/frappe-library).

---

## 💡 Features

- 🔐 **Login System** with email and password
- 🧾 **Add, View, Delete Books**
- 🔎 **Search by Title or Author**
- 🌐 **Import Books** from an online API
- 📦 **MySQL Database** integration
- 🖼️ Background image support for a better UI
- 🪟 Clean tabbed interface with `customtkinter`

---

## 📁 Folder Structure
Library-Management-System/
│
├── database.py # MySQL connection and book operations
├── import_books.py # Fetch books from Frappe API
├── library.py # Main GUI application
├── login.py # Login window
├── bg.jpg # Background image (optional)
├── README.md # Project documentation
└── requirements.txt # Python dependencies

