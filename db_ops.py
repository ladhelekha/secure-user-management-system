import mysql.connector
from mysql.connector import Error
from utils.hash_password import get_password_hash, verify_password
import pandas as pd
from tabulate import tabulate


hostname = "localhost"
database = "USERS_DATABASE"
port = "3306"
username = "root"
password = "Lekha@123456"

def create_user():
    username = input("Enter username: ")
    email = input("Enter email: ")
    password =input("Enter password: ")
    first_name = input("Enter first_name: ")
    last_name = input("Enter last_name: ")
    
    hashed_password = get_password_hash(password=password)
    query = f'''INSERT INTO Users(username, email, password, first_name, last_name) VALUES ('{username}', '{email}', '{hashed_password}', '{first_name}', '{last_name}')'''
    cursor.execute(query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully in the User table")
    print("user added in the table")

def read_users_data(username):
    query = f'''SELECT username, email, first_name, last_name FROM Users WHERE username = "{username}"'''
    cursor.execute(query)
    user = cursor.fetchone()
    if user:
        print("User details: ", user)
        
    else:
        print("User Not Found")
        
# def read_users_id_data(userid):
#     # username = input("Enter username to get details of user: ")
#     query = f'''SELECT username, email, first_name, last_name FROM Users WHERE userid = "{userid}"'''
#     cursor.execute(query)
#     user = cursor.fetchone()
#     if user:
#         print("User details: ", user)
        
#     else:
#         print("User Not Found")
        

def update_user_details(user_id, column_name,value ):
    query = f'''UPDATE Users SET {column_name} = '{value}' WHERE userid = {user_id}'''
    cursor.execute(query)
    connection.commit()
    print(cursor.rowcount, f'Record updated successfully in the Users table')
    print(f"user updated in the table")

def delete_user(user_id):
    try:
        delete_cursor = connection.cursor()
        # query = f'''SET FOREIGN_KEY_CHECKS=0; DELETE FROM Users WHERE userid = {user_id};  SET FOREIGN_KEY_CHECKS=1'''
        query1 = f'''DELETE FROM users_roles WHERE user_id = {user_id}'''
        query2 = f'''DELETE FROM Users WHERE userid = {user_id}'''
        delete_cursor.execute(query1)
        delete_cursor.execute(query2)
        connection.commit()
        # user = cursor.fetchone()
        print(delete_cursor.rowcount, "record(s) deleted successfully in the Users table")
        print(f"User with ID {user_id} deleted from the Users table")
    except mysql.connector.Error as error:
        print(f"Failed to delete user: {error}")
        
def update_role(user_id, role_id):
        query = f'''UPDATE users_roles SET role_id = {role_id} WHERE user_id = {user_id}'''
        cursor.execute(query)
        connection.commit()
        print(cursor.rowcount, f'Record updated successfully in the user_roles table')
        print(f"user_roles updated in the table")
        
        
def read_all_users():
    df = pd.read_sql('SELECT * FROM Users', connection, index_col="userid")
    df.drop(["password", "is_active"], axis=1, inplace=True)
    print(tabulate(df, headers=df.columns, tablefmt="grid"))
    


try:
    connection = mysql.connector.connect(host=hostname, database=database, user=username, password=password, port=port)
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor_delete = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute("SHOW TABLES;")
        record_table = cursor.fetchall()
        print("Tables in the database: ", record_table)
        
        
        # create_user()
        # read_users_data()
        # update_user_details(user_id=11113, column_name= "email" , value="xyz@gmail.com")
        
        # delete_user(user_id=11116)
        # update_role(user_id=3, role_id=3)
        read_all_users()

except Exception as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")



    

    
    
    