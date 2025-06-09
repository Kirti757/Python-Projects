import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3


def create_database():

    conn=sqlite3.connect("users.db")
    cursor=conn.cursor()
    cursor.execute("""
        create table if not exists users(
            id integer primary key autoincrement,
            username text unique not null,
            password text not null
            )
        """)
    conn.commit()
    conn.close()
    
create_database()

# ----------------------- App Root ------------------------
root = tk.Tk()
root.title("Login System")
root.geometry("700x400")
root.config(bg="white")

# --------------------- Frames ----------------------------
signup_frame = tk.Frame(root, bg="white")
signin_frame = tk.Frame(root, bg="white")

for frame in (signup_frame, signin_frame):
    frame.place(x=0, y=0, width=700, height=400)

def show_frame(frame):
    frame.tkraise()

# ---------------------- Signup UI ------------------------
def signup_ui():
    tk.Label(signup_frame, text="Sign-up", font="arial 20", bg="white", fg="deep sky blue").place(x=20, y=10)
    image = Image.open("loginicon.jpg")
    image = image.resize((270, 270))
    photo = ImageTk.PhotoImage(image)
    img_display = tk.Label(signup_frame, image=photo, bg="white")
    img_display.image = photo
    img_display.place(x=10, y=70)

    tk.Label(signup_frame, text="Username :", bg="white").place(x=340, y=100)
    username_entry = tk.Entry(signup_frame, font=("Arial", 14), width=20, relief="flat", bg="white")
    username_entry.place(x=460, y=90)
    tk.Frame(signup_frame, width=200, height=1, bg="black").place(x=460, y=120)

    tk.Label(signup_frame, text="Password :", bg="white").place(x=340, y=160)
    password_entry = tk.Entry(signup_frame, font=("Arial", 14), width=25, relief="flat", bg="white", show="*")
    password_entry.place(x=460, y=150)
    tk.Frame(signup_frame, width=200, height=1, bg="black").place(x=460, y=180)

    tk.Label(signup_frame, text="Confirm-Password :", bg="white").place(x=320, y=220)
    confirm_entry = tk.Entry(signup_frame, font=("Arial", 14), width=25, relief="flat", bg="white", show="*")
    confirm_entry.place(x=460, y=210)
    tk.Frame(signup_frame, width=200, height=1, bg="black").place(x=460, y=240)

    def signup():
        userid = username_entry.get().strip()
        pwd = password_entry.get().strip()
        cpwd = confirm_entry.get().strip()
        sym = ['$', '@', '#', '%']

        if not userid or not pwd or not cpwd:
            messagebox.showerror("Error", "All fields are required!")
            return
        if len(pwd) < 6 or len(pwd) > 10 or not any(s in sym for s in pwd):
            messagebox.showerror("Error", "Password must be 6-10 chars & include $@#%")
            return
        if pwd != cpwd:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (userid,))
        if cursor.fetchone():
            messagebox.showerror("Error", "Username already exists!")
            return
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (userid, pwd))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Sign-up successful! Please sign in.")
        show_frame(signin_frame)

    tk.Button(signup_frame, text="Sign-up", font="arial 10 bold", bg="limegreen", width=15, height=2, command=signup).place(x=420, y=265)
    tk.Label(signup_frame, text="Already have an account?", bg="white").place(x=400, y=320)
    tk.Button(signup_frame, text="Sign-in", bg="white", fg="blue", relief="flat", command=lambda: show_frame(signin_frame)).place(x=540, y=318)

# ---------------------- Signin UI ------------------------
def signin_ui():
    tk.Label(signin_frame, text="Sign-in", font="arial 20", bg="white", fg="deep sky blue").place(x=20, y=10)
    image = Image.open("loginicon.jpg")
    image = image.resize((270, 270))
    photo = ImageTk.PhotoImage(image)
    img_display = tk.Label(signin_frame, image=photo, bg="white")
    img_display.image = photo
    img_display.place(x=10, y=70)

    tk.Label(signin_frame, text="Username :", bg="white").place(x=340, y=100)
    username_entry = tk.Entry(signin_frame, font=("Arial", 14), width=20, relief="flat", bg="white")
    username_entry.place(x=460, y=90)
    tk.Frame(signin_frame, width=200, height=1, bg="black").place(x=460, y=120)

    tk.Label(signin_frame, text="Password :", bg="white").place(x=340, y=160)
    password_entry = tk.Entry(signin_frame, font=("Arial", 14), width=25, relief="flat", bg="white", show="*")
    password_entry.place(x=460, y=150)
    tk.Frame(signin_frame, width=200, height=1, bg="black").place(x=460, y=180)


    def signin():
        userid = username_entry.get().strip()
        pwd = password_entry.get().strip()

        if not userid or not pwd:
            messagebox.showerror("Error", "All fields are required!")
            return

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (userid, pwd))
        user = cursor.fetchone()
        conn.close()

        if user:
            messagebox.showinfo("Success", f"Welcome, {userid}!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")

    tk.Button(signin_frame, text="Sign-in", font="arial 10 bold", bg="limegreen", width=15, height=2, command=signin).place(x=420, y=230)
    tk.Label(signin_frame, text="Don't have an account?", bg="white").place(x=400, y=300)
    tk.Button(signin_frame, text="Sign-up", bg="white", fg="blue", relief="flat", command=lambda: show_frame(signup_frame)).place(x=540, y=298)

# ------------------- Load Both Frames --------------------
signup_ui()
signin_ui()
show_frame(signin_frame)

root.mainloop()