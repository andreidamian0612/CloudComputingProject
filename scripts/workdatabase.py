import mysql.connector



config = {
    'user': 'root',
    'password': '123456789',
    'host': '127.0.0.1'
}


cnx = mysql.connector.connect(**config)
