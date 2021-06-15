import mysql.connector


def DBconnection():
    connection = mysql.connector.connect(host='localhost',database='firstdatabase',
                                     user='root',
                                     password='')
    return connection



