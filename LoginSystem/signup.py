import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import subprocess
import os
import sqlite3


users = {}  # Dictionary to store username-password in pairs

def create_database():
    conn = sqlite3.connect("users.db")  # Connect to SQLite database
    cursor = conn.cursor()

# Create table if it doesn't exist
    cursor.execute("""
    create table if not exists users (
        id integer primary key autoincrement,
        username text unique not null,
        password text not null
    )
    """)

    conn.commit()
    conn.close()

create_database()

def signupbtn():
    userid = user_name.get().strip()
    password = user_password.get().strip()
    confirm_pwd = confirm_password.get().strip()
    SpecialSym =['$', '@', '#', '%']
    if not userid or not password or not confirm_pwd:
        messagebox.showerror("Error", "All fields are required!")
        return
    
    if len(password)<6 or len(password)>10 or not any(char in SpecialSym for char in password):
        messagebox.showerror("Error", "Password must be at least 6 or 10 characters long!\n Must contain at least one of the symbols $@#%")
        user_password.delete(0, tk.END)
        confirm_password.delete(0, tk.END)
        return
    
    if password != confirm_pwd:
        messagebox.showerror("Error", "Passwords do not match!")
        user_password.delete(0, tk.END)
        confirm_password.delete(0, tk.END)
        return

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

# Check if user already exists
    cursor.execute("SELECT * FROM users WHERE username=?", (userid,))
    if cursor.fetchone():
        messagebox.showerror("Error", "Username already taken! Try another.")
        user_name.delete(0, tk.END)
        conn.close()
        return

# Insert new user into database
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (userid, password))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Signup successful! You can now sign in.")
    
    user_name.delete(0, tk.END)
    user_password.delete(0, tk.END)
    confirm_password.delete(0, tk.END)


def open_signin():
    root.destroy()  # Close current signup page
    subprocess.run(["python", "signin.py"])  # Opens signin.py

root = tk.Tk()
root.title("Sign-up")
root.geometry("700x400")
root.config(bg="white")   

tk.Label(root, text="Sign-up", font="arial 20", bg="white", fg="deep sky blue").place(x=20, y=10)

# Load and display image
image = Image.open("loginicon.jpg")
resize_image = image.resize((270, 270)) 
image = ImageTk.PhotoImage(resize_image)

img_display = tk.Label(root, image=image, bg="white")
img_display.place(x=10, y=70)

# Username entry
tk.Label(root, text="Username :", font="arial 10", bg="white").place(x=340, y=100) 
user_name = tk.Entry(root, font=("Arial", 14), width=20, relief="flat", bg="white", fg="black")
user_name.place(x=460, y=90)
tk.Frame(root, width=200, height=1, bg="black").place(x=460, y=120)

# Password entry
tk.Label(root, text="Password :", font="arial 10", bg="white").place(x=340, y=160)
user_password = tk.Entry(root, font=("Arial", 14), width=25, relief="flat", bg="white", fg="black", show="*")
user_password.place(x=460, y=150)
tk.Frame(root, width=200, height=1, bg="black").place(x=460, y=180)

# Confirm Password entry
tk.Label(root, text="Confirm-Password :", font="arial 10", bg="white").place(x=320, y=220)
confirm_password = tk.Entry(root, font=("Arial", 14), width=25, relief="flat", bg="white", fg="black", show="*")
confirm_password.place(x=460, y=210)
tk.Frame(root, width=200, height=1, bg="black").place(x=460, y=240)

# Signup button
login_button = tk.Button(root, text="Sign-up", font="arial 10 bold",width=15, height=2, relief="ridge",bg="limegreen",command=signupbtn)
login_button.place(x=420, y=265)

# Already have an account label
label = tk.Label(root, text="Already have an account ? ", bg="white")
label.place(x=400, y=320)

# Sign-in Label as a Clickable Button
label1 = tk.Label(root, text="Sign-in", bg="white", fg="blue", cursor="hand2")
label1.place(x=542, y=320)
label1.bind("<Button-1>", lambda e: open_signin())  

root.mainloop()
