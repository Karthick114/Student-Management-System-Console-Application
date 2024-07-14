import csv
import mysql.connector

# Define MySQL connection details
db_host = 'localhost'
db_user = 'root'
db_password = ''
db_name = 'python'
table_name = 'py'

# Define global variables
student_fields = ['Admission no.', 'Name', 'Age', 'Email', 'Phone']
student_database = 'students.csv'


def display_menu():
    print("-------------------------------------")
    print(" Welcome to Student Management System")
    print("-------------------------------------")
    print("1. Add New Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Quit")


def add_student():
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    global student_fields

    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)

    # Connect to MySQL database
    connection = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    cursor = connection.cursor()

    # Insert data into the "name" column of the "py" table
    query = "INSERT INTO py (name) VALUES (%s)"
    cursor.execute(query, (student_data[1],))
    connection.commit()

    cursor.close()
    connection.close()

    print("Data saved successfully")
    input("Press any key to continue")
    return


# Rest of the code remains the same
