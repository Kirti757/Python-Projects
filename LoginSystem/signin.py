import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
import os
import subprocess
import sqlite3

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

def signinbtn():
    userid = user_name.get().strip()
    password = user_password.get().strip()

    if not userid or not password:
        messagebox.showerror("Error", "All fields are required!")
        return

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

# Check user credentials
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (userid, password))
    user = cursor.fetchone()

    conn.close()

    if user:
        messagebox.showinfo("Login Successful", f"Welcome, {userid}!")
        user_name.delete(0, tk.END)
        user_password.delete(0, tk.END)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
        user_name.delete(0, tk.END)
        user_password.delete(0, tk.END)


def open_signup():
    root.destroy()  # Close current signup page
    subprocess.run(["python", "signup.py"])  # Opens signin.py

root=tk.Tk()
root.title("Sign-in")
root.geometry("700x400")
root.config(bg="white")

tk.Label(root, text="Sign-in here ..", font="arial 20", bg="white", fg="deep sky blue").place(x=20, y=10)

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

# Signup button
login_button = tk.Button(root, text="Sign-in",font="arial 10 bold",bg="lime green", relief="ridge",width=20, height=2, command=signinbtn)
login_button.place(x=420, y=230)

# Already have an account label
label = tk.Label(root, text="Don't have an account? ", bg="white")
label.place(x=400, y=300)


# Sign-in Label as a Clickable Button
label1 = tk.Label(root, text="Sign-up", bg="white", fg="blue", cursor="hand2")
label1.place(x=535, y=300)
label1.bind("<Button-1>", lambda e: open_signup())

root.mainloop()
if __name__ == "__main__":
    signinbtn()
