import tkinter as tk
from tkinter.ttk import Treeview,Combobox
from tkinter import messagebox
from database import add_student, update_student, delete_student, fetch_all_students,search_student ,update_admission_no,export_to_csv
from tkinter import*

root=tk.Tk()

root.geometry("2000x830")
root.title("Student Management System")

titlelabel = tk.Label(root, text="Student Management System", font=("gabriola",32,"bold"),fg="DeepSkyBlue4")
titlelabel.place(x=36, y=18)

frame1=tk.Frame(root,bg="DeepSkyBlue4",relief="groove",borderwidth=2)
frame1.place(x=500, y=15,height=760,width=1015)

searchframe2=tk.Frame(root,relief="groove",borderwidth=2)
searchframe2.place(x=510, y=25,height=60,width=995)


tableframe3=tk.Frame(root,relief="groove",borderwidth=2)
tableframe3.place(x=510, y=100,height=660,width=995)

## labels and entry fields

tk.Label(root, text="Admission Number :", font="gabriola 14").place(x=40, y=100) 
admission_no = tk.Entry(root, font=("Arial", 14), width=20,relief="ridge", bg="white", fg="black")
admission_no.place(x=170, y=108)

tk.Label(root, text="Full Name :", font="gabriola 14").place(x=40, y=160) 
full_name = tk.Entry(root, font=("Arial", 14), width=20, relief="ridge", bg="white", fg="black")
full_name.place(x=170, y=168)

tk.Label(root, text="Class :", font="gabriola 14").place(x=40, y=220) 
Class_no= tk.Entry(root, font=("Arial", 14), width=20, relief="ridge", bg="white", fg="black")
Class_no.place(x=170, y=228)

tk.Label(root, text="Mail-id :", font="gabriola 14").place(x=40, y=280) 
mail_id = tk.Entry(root, font=("Arial", 14), width=20, relief="ridge", bg="white", fg="black")
mail_id.place(x=170, y=288)

tk.Label(root, text="Mobile-no :", font="gabriola 14").place(x=40, y=340) 
phone_no= tk.Entry(root, font=("Arial", 14), width=20, relief="ridge", bg="white", fg="black")
phone_no.place(x=170, y=348)

tk.Label(root, text="Gender :", font="gabriola 14").place(x=40, y=400) 
gender=Combobox(root,values=['Male','Female'],font="arial 14",state='r',width=10)
gender.place(x=170, y=408)
gender.set('Male')

tk.Label(root, text="Change Admission No:", font="gabriola 14").place(x=25, y=460)
new_admission_no_entry = tk.Entry(root, font=("Arial", 14), width=20, relief="groove", bg="white", fg="black")
new_admission_no_entry.place(x=170, y=467)

searchlabel = tk.Label(root, text="Search by", font=("arial",16),fg="DeepSkyBlue4")
searchlabel.place(x=550, y=40) 

search_entry = tk.Entry(root, font=("Arial", 14), width=20, relief="raised", bg="white", fg="black")
search_entry.place(x=870, y=41)

search_combobox=Combobox(root,values=['Admission-no','Full Name','Class','mail-id','Phone-no'],font="arial 14",state='r',width=10)
search_combobox.place(x=690,y=40)
search_combobox.set('Admission-no')

#Refresh table function
def load_students():
    """Fetch students from the database and display them in the table with alternating row colors."""
    # Clear previous data
    for row in table.get_children():
        table.delete(row)
    students = fetch_all_students()

    for index, student in enumerate(students):
        tag = "evenrow" if index % 2 == 0 else "oddrow"
        
        table.insert("", "end", values=(
            student["admission_no"],
            student["full_name"],
            student["class"],
            student["mail_id"],
            student["phone_no"],
            student["gender"]
        ), tags=(tag,))

    # row colors
    table.tag_configure("evenrow", background="DeepSkyBlue4")  # Light gray for even rows


# Functions for Buttons
def add_record():
    add_student(admission_no.get(), full_name.get(), Class_no.get(), mail_id.get(), phone_no.get(), gender.get())
    messagebox.showinfo("Success", "Student added successfully!")
    
    # Clear the input fields
    admission_no.delete(0, tk.END)
    full_name.delete(0, tk.END)
    Class_no.delete(0, tk.END)
    mail_id.delete(0, tk.END)
    phone_no.delete(0, tk.END)
    gender.set('Male') 

    load_students()


def update_record():
    admission = admission_no.get().strip()

    if not admission:
        messagebox.showwarning("Warning", "Please enter an Admission Number!")
        return

    update_student(
        admission_no=admission,
        full_name=full_name.get().strip() or None,
        Class_no=Class_no.get().strip() or None,
        mail_id=mail_id.get().strip() or None,
        phone_no=phone_no.get().strip() or None,
        gender=gender.get().strip() or None
    )

    messagebox.showinfo("Success", "Student details updated successfully!")
    
    # Clear only the fields that were updated
    admission_no.delete(0, tk.END)
    full_name.delete(0, tk.END)
    Class_no.delete(0, tk.END)
    mail_id.delete(0, tk.END)
    phone_no.delete(0, tk.END)
    gender.set('Male')  # Reset gender to default

    load_students()  # Refresh table


def delete_record():
    delete_student(admission_no.get())
    messagebox.showinfo("Success", "Student deleted successfully!")
    load_students()


def change_admission_number():
    old_id = admission_no.get()  # Old Admission Number
    new_id = new_admission_no_entry.get()  # New Admission Number

    if old_id.strip() == "" or new_id.strip() == "":
        messagebox.showwarning("Warning", "Please enter both old and new admission numbers!")
        return
    update_admission_no(old_id, new_id)
    messagebox.showinfo("Success", f"Admission No {old_id} changed to {new_id} successfully!")
    load_students()

    
def download_csv():
    export_to_csv()
    messagebox.showinfo("Success", "CSV file downloaded successfully!")


def search_student():
    """Fetch search results based on the selected filter and display them."""
    search_by_value = search_combobox.get()
    search_text = search_entry.get()

    if search_text.strip() == "":  # Prevent empty searches
        messagebox.showwarning("Warning", "Please enter a search value!")
        return
    results = search_student(search_by_value, search_text) 

    # Clear the existing table content
    for row in table.get_children():
        table.delete(row)

    # Insert filtered records into the table
    for student in results:
        table.insert("", "end", values=(
            student["admission_no"],
            student["full_name"],
            student["class"],
            student["mail_id"],
            student["phone_no"],
            student["gender"]
        ))

    if not results:
        messagebox.showinfo("Info", "No matching records found.")


def show_all_students():
    """Reload all student records from the database."""
    load_students()


### Buttons
change_adm_button = tk.Button(root, text="Update Admission No", font="gabriola 12 bold", width=17, height=1, bg="orange2", command=change_admission_number)
change_adm_button.place(x=130, y=515)

add_button = tk.Button(root, text="Add", font="gabriola 12 bold",width=15, height=1, relief="ridge",bg="limegreen",command=add_record)
add_button.place(x=60, y=590)

update_button = tk.Button(root, text="Update", font="gabriola 12 bold",width=15, height=1, relief="ridge",bg="limegreen",command=update_record)
update_button.place(x=220, y=590)

delete_button = tk.Button(root, text="Delete", font="gabriola 12 bold",width=15, height=1, relief="ridge",bg="limegreen",command= delete_record)
delete_button.place(x=60, y=650)

download_button = tk.Button(root, text="Download", font="gabriola 12 bold",width=15, height=1, relief="ridge",bg="limegreen",command=download_csv)
download_button.place(x=220, y=650)


search_button = tk.Button(root, text="Search", font="arial 10 ", bg="white",width=15, height=1, relief="ridge",borderwidth=2,command=search_student)
search_button.place(x=1140, y=40)

show_all = tk.Button(root, text="Show All", font="arial 10 ", bg="white",width=15, height=1, relief="ridge",borderwidth=2,command=show_all_students)
show_all.place(x=1320, y=40)


# Scrollbars
x_scroll = Scrollbar(tableframe3, orient="horizontal")
x_scroll.pack(side="bottom", fill="x")

y_scroll = Scrollbar(tableframe3, orient="vertical")
y_scroll.pack(side="right", fill="y")

# Treeview Table 
table = Treeview(tableframe3, columns=("admission_no", "full_name", "class", "mail_id", "phone_no", "gender"),
                 show="headings", xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)

# scrollbars
x_scroll.config(command=table.xview)
y_scroll.config(command=table.yview)

#column headings
table.heading("admission_no", text="Admission No")
table.heading("full_name", text="Full Name")
table.heading("class", text="Class")
table.heading("mail_id", text="Mail ID")
table.heading("phone_no", text="Phone No")
table.heading("gender", text="Gender")

# Set column width
table.column("admission_no", width=100, anchor="center")
table.column("full_name", width=150, anchor="w")
table.column("class", width=80, anchor="center")
table.column("mail_id", width=180, anchor="w")
table.column("phone_no", width=120, anchor="center")
table.column("gender", width=80, anchor="center")

table.pack(fill="both", expand=True)


root.mainloop()
