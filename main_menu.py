from conn import DBconnection

db_connection = DBconnection()

def create_database():
    db_cursor = db_connection.cursor()
    db_cursor.execute("CREATE DATABASE firstdatabase")
    db_cursor.execute("SHOW DATABASES")
    for db in db_cursor:
        print(db)

def main_page():
    print('Welcome to the school management portal /n')
    student_no = input('Enter Student No:  ')

    db_student_query = db_connection.cursor()
    db_student_query.execute("Select * from students where student_id = {}".format(student_no))
    data = db_student_query.fetchone()
    if data == None:
        print('register')
    print(data[1] + data[2])
    

main_page()