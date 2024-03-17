from connect_db import Database
from projekt import main


def courses(email, password):
    query = "SELECT * FROM course"
    data = Database.connect(query, "select")

    for i in data:
        print(f"""
        ID: {i[0]}
        Name: {i[1]}
        Description: {i[2]}
        Price: {i[3]}
        Rating: {i[4]}
                """)
        return student_panel(email, password)


def speciality(email, password):
    query = "SELECT * FROM speciality"
    data = Database.connect(query, "select")
    for i in data: print(f"""
        ID: {i[0]}
        Name: {[1]}
        """)

    return student_panel(email, password)

def update_pro(table, column_name, old_data, new_data):
    query = f"UPDATE {table} SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"
    return Database.connect(query, "update")


def update_id(table, column_name, old_data, new_data):
    query = f"UPDATE {table} SET {column_name} = {new_data} WHERE {column_name} = '{old_data}'"
    return Database.connect(query, "update")

def student_profile(email, password):
    services = input("""
    1. Data
    2. Settings
    0. Back
    """)

    if services == "1":
        query = "SELECT * FROM student"
        data = Database.connect(query, "select")

        for i in data:
            if i[3] == email and i[4] == password:
                print(f"""
                ID: {i[0]}
                first_name: {i[1]}
                last_name: {i[2]}
                email: {i[3]}
                password: {i[4]}
                headline: {i[5]}
                bio: {i[6]}
                contact_url: {i[7]}
                """)
            else:
                print("\nError")
                return student_profile(email, password)
            return student_profile(email, password)

    elif services == "2":
        query = "SELECT * FROM student"
        data = Database.connect(query, "select")

        for i in data:
            if i[3] == email and i[4] == password:
                print(f"""
                ID: {i[0]}
                first_name: {i[1]}
                last_name: {i[2]}
                email: {i[3]}
                password: {i[4]}
                headline: {i[5]}
                bio: {i[6]}
                contact_url: {i[7]}
                """)
                ve = input("""
                1. Update
                0. Back
                    """)
                if ve == "1":
                    column_name = input("Column Name: ")
                    old_data = input("Old data ")
                    new_data = input("New data ")
                    if column_name.lower() == 'student_id':
                        print(update_id("mentor", column_name, old_data, new_data))
                    else:
                        print(update_pro("mentor", column_name, old_data, new_data))
                    return student_profile(column_name, old_data)

                elif ve == "0":
                    return student_profile(email, password)

                else:
                    print("Error")
                    return student_profile(email, password)

            else:
                return student_profile(email, password)

    elif services == "0":
        return student_panel(email, password)

    else:
        print("Error")
        return student_panel(email, password)




def student_panel(email, password):
    print("\n<<<<<<<<<<<<Student Panel>>>>>>>>>>>>")
    service = input("""
    1. Speciality
    2. Courses
    3. Profile
    4. Log out
        >>>""")

    if service == "1":
        return speciality(email, password)

    elif service == "2":
        return courses(email, password)

    elif service == "3":
        return student_profile(email, password)

    elif service == "4":
        main()

    else:
        print("\nError")
        return student_panel(email, password)
