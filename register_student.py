def register(first_name,last_name,username, password, age,address):

    print(first_name)
    connection.is_connected()
    db_Info = connection.get_server_info()
    cursor = connection.cursor()
    sql = "INSERT INTO `users` (`id`, `first_name`, `last_name`, `username`, `password`, `age`, `address`) VALUES (NULL, '{}', '{}', '{}', '{}', '{}', '{}');".format(first_name,last_name,username, password, age,address)
    print(sql)
    cursor.execute(sql)
    connection.commit()
    print('User has been added')
    cursor.close()
    connection.close()