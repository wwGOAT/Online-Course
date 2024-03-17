from connect_db import Database
import student_panel
import admin_panel


def login_2(query, status):
    email = input("Email: ")
    password = input("Password: ")

    data = Database.connect(query, "select")
    for i in data:
        if i[3] == email and i[4] == password:
            if status == "1":
                return admin_panel.admin_panel(email, password)
            else:
                return student_panel.student_panel(email, password)
        else:
            print("\nError")
            return login()


def login():
    print("\n<<<<<<<<<<<Login>>>>>>>>>>>>\n")
    status = input("""
    1. admin.uz
    2. student.uz
            >>>""")

    if status == "1":
        query = "SELECT * FROM mentor"
        return login_2(query, status)

    elif status == "2":
        query = "SELECT * FROM student"
        return login_2(query, status)
    else:
        print("\nError")
        return login()