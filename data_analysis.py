import db_ops
db_connection = db_ops.connect_db()
print(db_connection)


def most_active_users(connection):
    cursor = connection.cursor()
    query = f'''SELECT * FROM Users WHERE is_active = true ORDER BY created_at ASC LIMIT 20'''
    cursor.execute(query)
    username = cursor.fetchall()
    print("The top 20 most active users are as follows: ")
    print(username)
    
most_active_users(connection=db_connection)

def 