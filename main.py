from customtkinter import *
from PIL import Image
from tkinter import messagebox

def login():
    if UsernameEntry.get() == '' or PasswordEntry.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    elif UsernameEntry.get() == 'library' and PasswordEntry.get() == '1234':
        messagebox.showinfo('Success', 'Login Successful!')
        root.destroy()
        import library
    else:
        messagebox.showerror('Error', 'Invalid Credentials')

root = CTk()
root.geometry('940x478')
root.resizable(0,0)
root.title('Library Login')
image = CTkImage(Image.open('cover-photo.jpg'), size=(940,478))
ImageLabel = CTkLabel(root, image=image, text='')
ImageLabel.place(x=0, y=0)

headingLabel = CTkLabel(root, text='Library Management System', bg_color='#FAFAFA', text_color='dark blue', font=('Goudy Old Style', 20, 'bold'))
headingLabel.place(x=20, y=100)

UsernameEntry = CTkEntry(root, placeholder_text="Enter username", width=180)
UsernameEntry.place(x=50, y=150)

PasswordEntry = CTkEntry(root, placeholder_text="Enter password", width=180, show='*')
PasswordEntry.place(x=50, y=190)

loginButton = CTkButton(root, text='Login', width=180, command=login)
loginButton.place(x=50, y=250)

root.mainloop()
