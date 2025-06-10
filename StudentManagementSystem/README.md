# Student Management System
This is a Student Management System built using Python, Tkinter, and MySQL. The system allows users to manage student records efficiently through a graphical user interface (GUI). It includes features such as adding, updating, deleting, searching, exporting student data, and changing admission numbers.

## Features
### Student Registration:
Users can add new student records including details like:
Admission Number, Full Name, Class, Email ID, Phone Number, Gender

### Update Student Records:
Modify existing student data using admission number as a reference.

### Delete Records:
Remove a student’s record from the system using their admission number.

### Change Admission Number:
Easily update a student’s admission number using the “Change Admission No” feature.

### Search Functionality:
Search students based on various filters:
Admission Number, Full Name, Class, Email ID, Phone Number

### Download to CSV:
Export all student records from the database to a CSV file for offline access or reporting.

### Database Integration:
Connected with MySQL for efficient storage and retrieval of student data.

### GUI:
Fully interactive and user-friendly interface built using Tkinter with visually styled frames, buttons, and input fields.

### Table View:
All student records are shown in a scrollable Treeview table with alternating row colors for better readability.
 
### Setup & Execution
#### Clone the Repository
      git clone https://github.com/YourUsername/StudentManagementSystem
      cd StudentManagementSystem
      
### Install Required Dependencies
      pip install mysql-connector-python pandas

### Setup MySQL Database
Create a MySQL database named studentmanagementdb and add a Students table:
      CREATE DATABASE studentmanagementdb;
      
      USE studentmanagementdb;
      CREATE TABLE Students (
          admission_no VARCHAR(20) PRIMARY KEY,
          full_name VARCHAR(100),
          class VARCHAR(20),
          mail_id VARCHAR(100),
          phone_no VARCHAR(15),
          gender VARCHAR(10)
      );
### Configure Database Credentials
Update your database.py file with your MySQL credentials:
  
      host="localhost"
      user="root"
      password="your_password"
      database="studentmanagementdb"

### Run the Application

      python student_management.py
### Output:

     ![img alt](https://github.com/Kirti757/Python-Projects/blob/main/Outputimages/studentmanagementsystem.png) .
