import mysql.connector
import pandas as pd
from tkinter import messagebox

def connect_db():
     
     return mysql.connector.connect(
         
        host="localhost",
        user="root",
        password="mysql@12",
        database="studentmanagementdb"
    )


def add_student(admission_no, full_name, Class_no, mail_id, phone_no, gender):
    conn = connect_db()
    mycursor = conn.cursor()
    query = "insert into Students (admission_no, full_name, class, mail_id, phone_no, gender) values (%s, %s, %s, %s, %s, %s)"
    mycursor.execute(query, (admission_no, full_name, Class_no, mail_id, phone_no, gender))
    conn.commit()
    conn.close()


def update_student(admission_no, full_name=None, Class_no=None, mail_id=None, phone_no=None, gender=None):
    conn = connect_db()
    cursor = conn.cursor()
    updates = []
    values = []

    if full_name:
        updates.append("full_name = %s")
        values.append(full_name)
    
    if Class_no:
        updates.append("class = %s")
        values.append(Class_no)
    
    if mail_id:
        updates.append("mail_id = %s")
        values.append(mail_id)
    
    if phone_no:
        updates.append("phone_no = %s")
        values.append(phone_no)

    if gender:
        updates.append("gender = %s")
        values.append(gender)

    if not updates:
        messagebox.showwarning("Warning", "No fields provided to update!")
        return

    values.append(admission_no) 
    query = f"update Students set {', '.join(updates)} where admission_no = %s"
    cursor.execute(query, tuple(values))
    conn.commit()
    conn.close()

    
def update_admission_no(old_admission_no, new_admission_no):
    conn = connect_db()
    cursor = conn.cursor()
    query = "update Students set admission_no = %s where admission_no = %s"
    cursor.execute(query, (new_admission_no, old_admission_no))
    conn.commit()
    conn.close()


def reset_auto_increment():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("alter table Students auto_increment = 1")
    conn.commit()
    conn.close()


def delete_student(admission_no):
    conn = connect_db()
    mycursor = conn.cursor()
    query = "delete from Students where admission_no=%s"
    mycursor.execute(query, (admission_no,))
    conn.commit()
    conn.close()


def search_student(search_by, search_value):
    """Search students based on the selected criteria."""
    conn = connect_db()
    mycursor = conn.cursor(dictionary=True)
    search_columns = {
        "Admission-no": "admission_no",
        "Full Name": "full_name",
        "Class": "class",
        "mail-id": "mail_id",
        "Phone-no": "phone_no"
    }
    column = search_columns.get(search_by) 
    if not column: 
        return []
    
    query = f"select * from Students where {column} like %s"
    mycursor.execute(query, ('%' + search_value + '%',))
    results = mycursor.fetchall()
    conn.close()
    return results


def fetch_all_students():
    conn = connect_db()
    mycursor = conn.cursor(dictionary=True) 
    query = "select * from Students"
    mycursor.execute(query)
    students = mycursor.fetchall()
    conn.close()
    return students


def export_to_csv():
    conn = connect_db()
    mycursor = conn.cursor(dictionary=True)
    query = "select * from Students"
    mycursor.execute(query)
    students = mycursor.fetchall()
    df = pd.DataFrame(students)
    if not df.empty:
        df.to_csv("students_data.csv", index=False)
        print("CSV Downloaded Successfully!")
    else:
        print("No data found in the Students table.")
    conn.close()


