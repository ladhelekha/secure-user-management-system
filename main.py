import db_ops
from db_ops import connect_db, create_user
db_connection = connect_db()
print(db_connection)
# if db_connection is None:
#     print("connection Failed")
# else:  
#     create_user(connection=db_connection)
#     db_connection.close()

def main_menu():
    print("1.Crud Menu\n2.Data Analysis Menu\n3.Exit")
    
def crud_menu():
    print("1.Create User\n2.Get User Data\n3.Update User Details\n4.Delete User\n5.Update")
    
def data_analysis_menu():
    print("")
    
    
while True:
    main_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        crud_menu()
        
    elif choice == 2:
        data_analysis_menu()
    elif choice == 3:
        print("Exit")
        break
    else:
        print("Enter a valid choice. Please try again.")
        

