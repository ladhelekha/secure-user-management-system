import db_ops 
# from db_ops import connect_db, create_user
db_connection = db_ops.connect_db()
print(db_connection)
# if db_connection is None:
#     print("connection Failed")
# else:  
#     create_user(connection=db_connection)
#     db_connection.close()

def main_menu():
    print("1.Crud Menu\n2.Data Analysis Menu\n3.Exit")
    return int(input("Enter your choice: "))
    
def crud_menu():
    print("1.Create User\n2.Get User Data\n3.Update User Details\n4.Delete User\n5.Update Role\n6.Read all users\n7.Exit")
    return int(input("Enter your choice: "))
    
def data_analysis_menu():
    print("")
    
    
while True:
    main_menu_choice = main_menu()
    if main_menu_choice == 1:
        while True:
            crud_choice = crud_menu()
            if crud_choice == 1:
                db_ops.create_user(connection=db_connection)
            elif crud_choice == 2:
                db_ops.read_users_data(connection=db_connection,username="ugrimes")
            elif crud_choice == 3:
                db_ops.update_user_details(connection=db_connection, user_id=711, column_name="email", value="raj@gmail.com")
            elif crud_choice == 4:
                db_ops.delete_user(connection=db_connection, user_id=11115)
            elif crud_choice == 5:
                db_ops.update_role(connection=db_connection, user_id=711, role_id=4)
            elif crud_choice == 6:
                db_ops.read_all_users(connection=db_connection)
            elif crud_choice == 7:
                print("Exit crud_menu")
                break
            else:
                print("Enter a valid choice. Please try again.") 
            break                 
    elif main_menu_choice == 2:
        data_analysis_menu()
    elif main_menu_choice == 3:
        print("Exit")
        break
    else:
        print("Enter a valid choice. Please try again.")
        

