import os
import db_ops 
import data_analysis
db_connection = db_ops.connect_db()

def main_menu():
    print("1.Crud Menu\n2.Data Analysis Menu\n3.Exit")
    return int(input("Enter your choice: "))
    
def crud_menu():
    print("1.Create User\n2.Get User Data\n3.Update User Details\n4.Delete User\n5.Update Role\n6.Read all users\n7.Exit")
    return int(input("Enter your choice: "))
    
def data_analysis_menu():
    print("1.Most Active Users\n2.Inactive Users\n3.Role Distribution\n4.Least Assigned Role\n5.Active Admins\n6.Active Users\n7.User Churn Analysis\n8.Exit")
    return int(input("Enter your choice: "))
    
while True:
    main_menu_choice = main_menu()
    os.system("clear")
    if main_menu_choice == 1:
        while True:
            crud_choice = crud_menu()
            if crud_choice == 1:
                db_ops.create_user(connection=db_connection)
            elif crud_choice == 2:
                db_ops.read_users_data(connection=db_connection,username= input("Enter username: "))
            elif crud_choice == 3:
                db_ops.update_user_details(connection=db_connection, user_id=input("Enter user_id: "), column_name=input("Enter column_name: "), value=input("Enter value: "))
            elif crud_choice == 4:
                db_ops.delete_user(connection=db_connection, user_id=input("Enter user_id: "))
            elif crud_choice == 5:
                db_ops.update_role(connection=db_connection, user_id=input("Enter user_id: "), role_id=input("Enter role_id: "))
            elif crud_choice == 6:
                db_ops.read_all_users(connection=db_connection)
            elif crud_choice == 7:
                print("Exit crud_menu")
                break
            else:
                print("Enter a valid choice. Please try again.") 
            break                 
    elif main_menu_choice == 2:
        while True:
            data_analysis_choice = data_analysis_menu()
            if data_analysis_choice == 1:    
                data_analysis.most_active_users(connection=db_connection)
            elif data_analysis_choice == 2:
                data_analysis.inactive_six_months_users(connection=db_connection)
            elif data_analysis_choice == 3:
                data_analysis.role_distribution(connection=db_connection)
            elif data_analysis_choice == 4:
                data_analysis.least_assigned_role(connection=db_connection)
            elif data_analysis_choice == 5:
                data_analysis.active_admins(connection=db_connection)
            elif data_analysis_choice == 6:
                data_analysis.active_users(connection=db_connection)
            elif data_analysis_choice == 7:
                data_analysis.user_churn_analysis(connection=db_connection)              
            elif data_analysis_choice == 8:
                print("Exit Data Analysis Menu")
                break
            else:
                print("Enter a valid choice. Please try again.")       
    elif main_menu_choice == 3:
        print("Exit")
        break
    else:
        print("Enter a valid choice. Please try again.")
        

