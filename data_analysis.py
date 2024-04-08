import db_ops
db_connection = db_ops.connect_db()
print(db_connection)


def most_active_users(connection):
    cursor = connection.cursor()
    query = f'''SELECT username FROM Users WHERE created_at LIKE '2016%' GROUP BY username'''
    cursor.execute(query)
    username = cursor.fetchall()
    print("Most Active users for 2016 are as follows: ")
    print(username)
    
most_active_users(connection=db_connection)