import mysql.connector

connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Gangara4',
    database = 'social_media'
)

cursor = connection.cursor()

cursor.execute('SHOW TABLES')

tables = cursor.fetchall()
for table in tables:
    print(table[0])

    cursor.close()
    connection.close()