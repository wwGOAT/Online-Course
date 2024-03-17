from connect_db import Database

def create_table():
    student_table = """
        CREATE TABLE student(
            student_id SERIAL PRIMARY KEY,
            first_name VARCHAR(30),
            last_name VARCHAR(30),
            email VARCHAR(50),
            password VARCHAR(20),
            headline VARCHAR(50),
            bio TEXT,
            contact_url VARCHAR(50),
            last_update DATE DEFAULT now(),
            create_date TIMESTAMP DEFAULT now())
    """

    mentor_table = """
        CREATE TABLE mentor(
            mentor_id SERIAL PRIMARY KEY,
            first_name VARCHAR(30),
            last_name VARCHAR(30),
            email VARCHAR(50),
            password VARCHAR(20),
            headline VARCHAR(50),
            bio TEXT,
            contact_url VARCHAR(50),
            last_update DATE DEFAULT now(),
            create_date TIMESTAMP DEFAULT now())
    """

    lenguage_table = """
        CREATE TABLE language(
            language_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            last_update DATE DEFAULT now(),
            create_date TIMESTAMP DEFAULT now())
    """

    course_status_table = """
        CREATE TABLE course_status(
            course_status_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            create_date TIMESTAMP DEFAULT now())
    """

    speciality_table = """
        CREATE TABLE speciality(
            speciality_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            create_date TIMESTAMP DEFAULT now())
    """

    course_table = """
        CREATE TABLE course(
            course_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            description TEXT,
            rating FLOAT,
            active_Students INT,
            mentor_id INT REFERENCES student(student_id),
            lenguage_id INT REFERENCES language(language_id),
            price NUMERIC,
            course_status_id INT REFERENCES course_status(course_status_id),
            support_date DATE,
            last_update DATE DEFAULT now(),
            create_date TIMESTAMP DEFAULT now())
    """

    comment_table = """
        CREATE TABLE comment(
            comment_id SERIAL PRIMARY KEY,
            text TEXT,
            student_id INT REFERENCES student(student_id),
            course_id INT REFERENCES course(course_id))
    """

    payment_table = """
        CREATE TABLE payment(
            payment_id SERIAL PRIMARY KEY,
            course_id INT REFERENCES course(course_id),
            student_id INT REFERENCES student(student_id),
            amound NUMERIC,
            card_number INT,
            create_date TIMESTAMP DEFAULT now())
    """

    speciality_course_table = """
        CREATE TABLE speciality_course(
            speciality_course_id SERIAL PRIMARY KEY,
            speciality_id INT REFERENCES speciality(speciality_id),
            course_id INT REFERENCES course(course_id),
            create_date TIMESTAMP DEFAULT now())
    """

    lesson_status_table = """
        CREATE TABLE lesson_status(
            lesson_status_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            create_date TIMESTAMP DEFAULT now())
    """

    modules_table = """
        CREATE TABLE modules(
            module_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            course_id INT REFERENCES course(course_id),
            lesson_count INT,
            last_update DATE DEFAULT now(),
            create_date TIMESTAMP DEFAULT now())
    """

    lesson_table = """
        CREATE TABLE lesson(
            lesson_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            description VARCHAR(50),
            lesson_status_id INT REFERENCES lesson_status(lesson_status_id),
            module_id INT REFERENCES modules(module_id),
            create_date TIMESTAMP DEFAULT now())
    """

    data = {
        "student_table": student_table,
        "mentor_table": mentor_table,
        "lenguage_table": lenguage_table,
        "course_status_table": course_status_table,
        "speciality_table": speciality_table,
        "course_table": course_table,
        "comment_table": comment_table,
        "payment_table": payment_table,
        "speciality_course_table": speciality_course_table,
        "lesson_status_table": lesson_status_table,
        "modules_table": modules_table,
        "lesson_table": lesson_table,

    }

    for i in data:
        print(f"{i} {Database.connect(data[i], "create")}")



if __name__ == "__main__":
    create_table()