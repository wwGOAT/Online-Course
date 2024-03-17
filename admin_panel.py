from connect_db import Database
from classes import Speciality, Course
from projekt import main


def update(column_name, old_data, new_data):
    query = f"UPDATE course SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"
    return Database.connect(query, "update")


def course_insert(email, password):
    name = input("Name: ")
    description = input("description: ")
    rating = input("rating: ")
    active_students = input("active_students: ")
    mentor_id = input("mentor_id: ")
    language_id = input("lenguage_id: ")
    price = input("price: ")
    course_status_id = input("course_status_id: ")
    spec = Course(name, description, rating, active_students, mentor_id, language_id, price, course_status_id)
    print(spec.insert("course"))
    return course(email, password)


def course_list(email, password):
    data = Course.select("course")
    for b in data:
        print(f"""
        ID: {b[0]}
        Name: {b[1]}
        Description: {b[2]}
        Rating: {b[3]}
        Admin First Name: {b[4]}
        Admin Last Name: {b[5]}
        Status: {b[6]}
        Language: {b[7]}
        Price{b[8]}
        """)
    return course(email, password)


def course_update(email, password):
    column_name = input("Column Name: ")
    old_data = input("Now Data: ")
    new_data = input("New Data: ")
    if column_name == "speciality_id":
        print(Course.update_id("course", column_name, old_data, new_data))
    else:
        print(Course.update("course", column_name, old_data, new_data))
    return course(email, password)


def course_delete(email, password):
    column_name = input("Column Name: ")
    id = input("ID: ")
    if column_name == "speciality_id":
        print(Course.delete_id("course", column_name, id))

    else:
        print(Course.delete("course", column_name, id))

    return course(email, password)


def course(email, password):
    service = input("""
    1. List
    2. Insert
    3. Update
    4. Delete
    0. Back
        >>>""")

    if service == "1":
        return course_list(email, password)

    elif service == "2":
        return course_insert(email, password)

    elif service == "3":
        return course_update(email, password)

    elif service == "4":
        return course_delete(email, password)

    elif service == "0":
        return admin_panel(email, password)


def speciality_insert(email, password):

    name = input("Name: ")
    service = Speciality(name)
    print(service.insert("speciality"))
    return speciality(email, password)


def speciality_list(email, password):
    data = Speciality.select("speciality")
    for i in data:
        print(f"""
                ID: {i[0]}
                Name: {i[1]}
            """)

    return speciality(email, password)

def speciality_update(email, password):
    column_name = input("Column Name: ")
    old_data = input("Now Data: ")
    new_data = input("New Data: ")
    if column_name == "speciality_id":
        print(Speciality.update_id("speciality", column_name, old_data, new_data))
    else:
        print(Speciality.update("speciality", column_name, old_data, new_data))
    return speciality(email, password)


def speciality_delete(email, password):
    column_name = input("Column Name: ")
    id = input("data: ")
    if column_name == "speciality_id":
        print(Speciality.delete_id("speciality", column_name, id))
    elif column_name == "name":
        data = input("Data: ")
        print(Speciality.delete("speciality", column_name, data))
    else:
        return speciality(email, password)


def speciality(email, password):
    services = input("""
            1. List
            2. Insert
            3. Update
            4. Delete
            0. back
                >>> """)

    if services == "1":
        return speciality_list(email, password)

    elif services == "2":
        return speciality_insert(email, password)

    elif services == "3":
        return speciality_update(email, password)

    elif services == "4":
        return speciality_delete(email, password)

    elif services == "0":
        return admin_panel(email, password)

    else:
        return speciality(email, password)

def update_pro(table, column_name, old_data, new_data):
    query = f"UPDATE {table} SET {column_name} = '{new_data}' WHERE {column_name} = '{old_data}'"
    return Database.connect(query, "update")


def update_id(table, column_name, old_data, new_data):
    query = f"UPDATE {table} SET {column_name} = {new_data} WHERE {column_name} = '{old_data}'"
    return Database.connect(query, "update")


def admin_profile(email, password):
    services = input("""
    1. Data
    2. Settings
    0. Back
      >>>""")

    if services == "1":
        query = "SELECT * FROM mentor"
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
                return admin_profile(email, password)

    elif services == "2":
        query = "SELECT * FROM mentor"
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
                ve = input("""
                1. Update
                0. Back
                    """)
                if ve == "1":
                    column_name = input("Column Name: ")
                    old_data = input("Old data ")
                    new_data = input("New data ")
                    if column_name.lower() == 'mentor_id':
                        print(update_id("mentor", column_name, old_data, new_data))
                    else:
                        print(update_pro("mentor", column_name, old_data, new_data))
                        return admin_panel(column_name, old_data)

                elif ve == "0":
                    return admin_profile(email, password)

                else:
                    print("Error")
                    return admin_profile(email, password)

    elif services == "0":
        return admin_panel(email, password)

    else:
        print("Error")
        return admin_panel(email, password)





def admin_panel(email, password):
    print("\n<<<<<<<<<<<<Admin Panel>>>>>>>>>>>>>")
    saw = input("""
    1. Speciality
    2. Courses
    3. Profile
    4. Log Out
        >>> """)

    if saw == "1":
        return speciality(email, password)

    elif saw == "2":
        return course(email, password)

    elif saw == "3":
        return admin_profile(email, password)

    elif saw == "4":
        return main()

    else:
        print("\nError")
        return admin_panel(email, password)