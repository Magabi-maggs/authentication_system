import mysql.connector


connection = mysql.connector.connect(host='localhost',
                                     database='firstdatabase',
                                     user='root',
                                     password='')




def register(first_name,last_name,username, password, age,address):

    print(first_name)
    connection.is_connected()
    db_Info = connection.get_server_info()
    cursor = connection.cursor()
    sql = "INSERT INTO `users` (`id`, `first_name`, `last_name`, `username`, `password`, `age`, `address`) VALUES (NULL, '{}', '{}', '{}', '{}', '{}', '{}');".format(first_name,last_name,username, password, age,address)
    print(sql)
    cursor.execute(sql)
    connection.commit()
    print()
    cursor.close()
    connection.close()


def stored_user():
    users_list = {'username': 'joe', 'password': 12345}
    return users_list


def login(username, password):
    user = stored_user()

    if username == str(user["username"]) and password == str(user["password"]):
        print('username is ' + username + ' password is ' + password)
        print('login successefuly')
    if username != 'joe':
        print(' You are not  registered')


# user = stored_user()
# print(user['username'])

def get_user_details():
    username = input('username')
    password = input('password')

    login(username, password)


# get_user_details()

register('ken','john','kjohn', '2229', 2,'marlin')
