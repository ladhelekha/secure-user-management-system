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

def create_user(connection):
    cursor = connection.cursor()
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
    cursor.close()

def read_users_data(connection, username):
    cursor = connection.cursor()
    query = f'''SELECT username, email, first_name, last_name FROM Users WHERE username = "{username}"'''
    cursor.execute(query)
    user = cursor.fetchone()
    if user:
        print("User details: ", user)      
    else:
        print("User Not Found")
        cursor.close()
        

def update_user_details(connection, user_id, column_name,value ):
    cursor = connection.cursor()
    query = f'''UPDATE Users SET {column_name} = '{value}' WHERE userid = {user_id}'''
    cursor.execute(query)
    connection.commit()
    print(cursor.rowcount, f'Record updated successfully in the Users table')
    print(f"user updated in the table")
    cursor.close()

def delete_user(connection, user_id):
    delete_cursor = connection.cursor()
    # query = f'''SET FOREIGN_KEY_CHECKS=0; DELETE FROM Users WHERE userid = {user_id};  SET FOREIGN_KEY_CHECKS=1'''
    query1 = f'''DELETE FROM users_roles WHERE user_id = {user_id}'''
    query2 = f'''DELETE FROM Users WHERE userid = {user_id}'''
    delete_cursor.execute(query1)
    delete_cursor.execute(query2)
    connection.commit()
    print(delete_cursor.rowcount, "record(s) deleted successfully in the Users table")
    print(f"User with ID {user_id} deleted from the Users table")
    delete_cursor.close()
        
def update_role(connection, user_id, role_id):
    cursor = connection.cursor()
    query = f'''UPDATE users_roles SET role_id = {role_id} WHERE user_id = {user_id}'''
    cursor.execute(query)
    connection.commit()
    print(cursor.rowcount, f'Record updated successfully in the user_roles table')
    print(f"user_roles updated in the table")
    cursor.close()
    
        
def read_all_users(connection):
    cursor = connection.cursor()
    df = pd.read_sql('SELECT * FROM Users', connection, index_col="userid")
    df.drop(["password", "is_active"], axis=1, inplace=True)
    print(tabulate(df, headers=df.columns, tablefmt="grid"))
    cursor.close()
    

def connect_db():  
    try:
        connection = mysql.connector.connect(host=hostname, database=database, user=username, password=password, port=port)
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            return connection

    except Exception as e:
        print("Error while connecting to MySQL", e)
        return None



    

    
    
    