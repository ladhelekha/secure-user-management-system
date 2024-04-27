def most_active_users(connection):
    cursor = connection.cursor()
    query = f'''SELECT username FROM Users WHERE is_active = true ORDER BY created_at ASC LIMIT 20'''
    cursor.execute(query)
    username = cursor.fetchall()
    print("The top 20 most active users are as follows: ")

    for indexx, value in enumerate(username):
        print(f"{indexx+1}. {value[0]}")
    

def inactive_six_months_users(connection):
    cursor = connection.cursor()
    query = f'''Select * from Users where created_at > curdate() - interval (dayofmonth(curdate()) - 1) day - interval 6 month'''
    cursor.execute(query)
    inactive_sixmonths_users = cursor.fetchall()
    print("Inactive users onboarded in last six months are as follows: ")
    
    for i in range(len(inactive_sixmonths_users)):
        print(f'{i+1}. {inactive_sixmonths_users[i][1]}')
    
    
def get_role_name(role_id):
    if role_id == 1:
        return "user"
    elif role_id == 2:
        return "admin"
    elif role_id == 3:
        return "superuser"
    elif role_id == 4:
        return "manager"
    else:
        return 'Invalid'

def role_distribution(connection):
    cursor = connection.cursor()
    query = f'''SELECT role_id, COUNT(role_id) AS role_count FROM users_roles GROUP BY role_id'''
    cursor.execute(query)
    role_distribution = cursor.fetchall()
    print("Role count for ‘user’, ‘admin’, ‘superuser’, ‘manager’ is as follows: ")
    print(role_distribution)    
    
    for i in range(len(role_distribution)):
        role = get_role_name(role_id=role_distribution[i][0])
        print(f'{i+1}. {role_distribution[i][1]} - {role}')


def least_assigned_role(connection):
    cursor = connection.cursor()
    query = f'''SELECT role_id, COUNT(role_id) AS role_count FROM users_roles GROUP BY role_id ORDER BY role_count ASC LIMIT 1;'''
    cursor.execute(query)
    least_assigned_role = cursor.fetchall()
    print("least_assigned_role: ")
    print(least_assigned_role)   
    
    for i in range(len(least_assigned_role)):
        role = get_role_name(role_id=least_assigned_role[i][0])
        print(f'Least assigned role is: {role} with a count of {least_assigned_role[i][1]} ') 
    

def active_admins(connection):
    cursor = connection.cursor()
    query = f'''SELECT is_active, COUNT(*) AS admin_count FROM Users u INNER JOIN users_roles ur ON u.userid = ur.user_id
WHERE 
    ur.role_id = 2 
GROUP BY 
    is_active'''
    cursor.execute(query)
    no_active_admins = cursor.fetchall()
    print(no_active_admins)
    print(f" inactiveadmins = {no_active_admins[0][1]} and active admins = {no_active_admins[1][1]} ")
    
def active_users(connection):
    cursor = connection.cursor()
    query = f'''SELECT is_active, COUNT(*) as user_count FROM Users u INNER JOIN users_roles ur ON u.userid = ur.user_id
WHERE 
    ur.role_id = 1 GROUP BY is_active'''
    cursor.execute(query)
    no_active_users = cursor.fetchall()
    print(no_active_users)    
    print(f" activeusers = {no_active_users[0][1]} and inactiveusers = {no_active_users[1][1]} ")
    

def user_churn_analysis(connection):
    cursor = connection.cursor()
    query = f'''SELECT 
    ur.role_id,
    r.name,
    COUNT(CASE WHEN u.is_active = 0 THEN 1 END) AS churned_users,
    COUNT(*) AS total_users,
    (COUNT(CASE WHEN u.is_active = 0 THEN 1 END) / COUNT(*)) * 100 AS churn_rate
FROM 
    users_roles ur
INNER JOIN 
    Users u ON ur.user_id = u.userid
INNER JOIN 
    Roles r ON ur.role_id = r.id
GROUP BY 
    ur.role_id, r.name'''
    cursor.execute(query)
    user_churn = cursor.fetchall()
    print("User churn analysis: ")
    print(user_churn)
    
    for indexx, role_churnrate in enumerate(user_churn):
        print(f"{indexx+1}. For role - {role_churnrate[1]} churn_rate is {role_churnrate[4]}")   
    