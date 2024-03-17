from connect_db import Database
import login


def register():
    print("Register Page")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    password_1 = input("Password: ")
    password_2 = input("Reply Password: ")
    while password_1 != password_2:
        print("\nPasswordlar to'g'ri kelmadi\n")
        password_1 = input("Password: ")
        password_2 = input("Reply Password: ")
    headline = input("Headline: ")
    bio = input("Bio: ")
    contact_url = input("Contact URL: ")

    query = f"""INSERT INTO student(first_name, last_name, email, password, headline, bio,  contact_url)
            VALUES('{first_name}', '{last_name}', '{email}', '{password_2}', '{headline}', '{bio}', '{contact_url}')"""


    print(Database.connect(query, "insert"))
    return login.login()