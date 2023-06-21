# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date


DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]


task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)


#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

# Login logic
logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True


def reg_user():
        '''Add a new user to the user.txt file'''
        # - Request input of a new username
        new_username = input("New Username: ")

        if new_username in username_password:
            print("Username Taken.")
            return

        # - Request input of a new password
        new_password = input("New Password: ")

        # - Request input of password confirmation.
        confirm_password = input("Confirm Password: ")

        # - Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file,
            print("New user added")
            username_password[new_username] = new_password
            
            # Save user data to external file
            with open("user.txt", "w") as out_file:
                user_data = []
                for k in username_password:
                    user_data.append(f"{k};{username_password[k]}")
                out_file.write("\n".join(user_data))

        # - Error handling for mispelt password confirmation
        else:
            print("Passwords do not match")

def add_task():
        # Task input details
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
            return
        task_title = input("Title of Task: ")
        task_description = input("Description of Task: ")
        # Try date input, exception in while loop for incorrect input
        while True:
            try:
                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                break

            except ValueError:
                print("Invalid datetime format. Please use the format specified")


        # Get the current date.
        curr_date = date.today()
        ''' Add the data to the file task.txt and
            Include 'No' to indicate if the task is complete.'''
        # define dictionary with inputted values from above
        new_task = {
            "username": task_username,
            "title": task_title,
            "description": task_description,
            "due_date": due_date_time,
            "assigned_date": curr_date,
            "completed": False
        }

        # Add task to txt file
        task_list.append(new_task)
        with open("tasks.txt", "a") as task_file:
            task_list_to_write = []
            for t in task_list:
                str_attrs = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n".join(task_list_to_write))
        print("Task successfully added.")

def view_all():
    print("View All Tasks Main Area:")

    # Read the task data from the file
    with open('tasks.txt', 'r') as task_file:
        task_data = task_file.read().strip().split('\n')

    task_list.clear()

    # Parse the task data and update the task list
    for task_str in task_data:
        attrs = task_str.split(';')
        username = attrs[0]
        title = attrs[1]
        description = attrs[2]
        due_date = datetime.strptime(attrs[3], DATETIME_STRING_FORMAT)
        assigned_date = datetime.strptime(attrs[4], DATETIME_STRING_FORMAT)
        completed = True if attrs[5].lower() == 'yes' else False

        task_list.append({
            'username': username,
            'title': title,
            'description': description,
            'due_date': due_date,
            'assigned_date': assigned_date,
            'completed': completed
        })

    # Print the tasks
    if len(task_list) > 0:
        for index, task in enumerate(task_list):
            print(f"Task {index + 1}:")
            print(f"Username: {task['username']}")
            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Due Date: {task['due_date'].strftime(DATETIME_STRING_FORMAT)}")
            print(f"Assigned Date: {task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}")
            print(f"Completed: {'Yes' if task['completed'] else 'No'}")
            print()
    else:
        print("No tasks found.")

    print("View All Tasks End Area")


def view_mine():
    while True:
        print("View My Tasks Main Area:")

        # Display tasks
        for i, t in enumerate(task_list):
            if t['username'] == curr_user:
                disp_str = f"Task: \t\t {t['title']}\nTask Number: \t\t{i + 1}\n"
                disp_str += f"Assigned to: \t {t['username']}\n"
                print(disp_str)

        # Option to select task by number or return to main menu
        task_num_input = input("Enter the task number to view details (or -1 to go back to the main menu): ")
        if task_num_input == "-1":
            break

        # Selected Task
        try:
            task_num = int(task_num_input) - 1
            selected_task = task_list[task_num]
            if selected_task['username'] == curr_user:
                disp_str = f"Task: \t\t {selected_task['title']}\nTask Number: {task_num + 1}\n"
                disp_str += f"Assigned to: \t {selected_task['username']}\n"
                disp_str += f"Date Assigned: \t {selected_task['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Due Date: \t {selected_task['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
                disp_str += f"Task Description: \n{selected_task['description']}\n"
                print(disp_str)

                edit_choice = input("Do you want to mark this task as complete, edit the username, or edit the due date? (mark/username/due date/none): ")

                # Updating details of task logic
                if edit_choice.lower() == "mark":
                    if selected_task['completed'] == False:
                        selected_task['completed'] = True
                        print("Task marked as complete.")
                    else:
                        print("Task is already marked as complete.")
                elif edit_choice.lower() == "username":
                    new_username = input("Enter the new username: ")
                    selected_task['username'] = new_username
                    print("Task username updated.")
                elif edit_choice.lower() == "due date":
                    while True:
                        try:
                            new_due_date = input("Enter the new due date (YYYY-MM-DD): ")
                            due_date_time = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                            selected_task['due_date'] = due_date_time
                            print("Task due date updated.")
                            break
                        except ValueError:
                            print("Invalid datetime format. Please use the format specified.")
                elif edit_choice.lower() == "none":
                    continue
                else:
                    print("Invalid choice.")

                # Write the updated task list back to the file
                with open('tasks.txt', 'w') as task_file:
                    task_list_to_write = []
                    for t in task_list:
                        str_attrs = [
                            t['username'],
                            t['title'],
                            t['description'],
                            t['due_date'].strftime(DATETIME_STRING_FORMAT),
                            t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                            "Yes" if t['completed'] else "No"
                        ]
                        task_list_to_write.append(";".join(str_attrs))
                    task_file.write("\n".join(task_list_to_write))

            else:
                print("You are not assigned to this task.")

        except (ValueError, IndexError):
            print("Invalid at the end of the conversation.")

                

def generate_reports():
    print("Generate Report Main Area:")
    
    # Read the task data from the file
    with open('tasks.txt', 'r') as task_file:
        task_data = task_file.read().strip().split('\n')

    task_list.clear()

    # Parse the task data and update the task list
    for task_str in task_data:
        attrs = task_str.split(';')
        username = attrs[0]
        title = attrs[1]
        description = attrs[2]
        due_date = datetime.strptime(attrs[3], DATETIME_STRING_FORMAT)
        assigned_date = datetime.strptime(attrs[4], DATETIME_STRING_FORMAT)
        completed = True if attrs[5].lower() == 'yes' else False

        task_list.append({
            'username': username,
            'title': title,
            'description': description,
            'due_date': due_date,
            'assigned_date': assigned_date,
            'completed': completed
        })

    # Initialise variables for generating the report
    total_tasks = len(task_list)
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0
    users = {}
    
    # Categorise and count tasks' status
    for task in task_list:
        if task['completed']:
            completed_tasks += 1
        else:
            uncompleted_tasks += 1

        if task['due_date'] < datetime.now() and not task['completed']:
            overdue_tasks += 1

        if task['username'] in users:
            users[task['username']]['total_tasks'] += 1
            if task['completed']:
                users[task['username']]['completed_tasks'] += 1
            else:
                users[task['username']]['uncompleted_tasks'] += 1
                if task['due_date'] < datetime.now():
                    users[task['username']]['overdue_tasks'] += 1
        else:
            users[task['username']] = {
                'total_tasks': 1,
                'completed_tasks': 1 if task['completed'] else 0,
                'uncompleted_tasks': 1 if not task['completed'] else 0,
                'overdue_tasks': 1 if (not task['completed'] and task['due_date'] < datetime.now()) else 0
            }

    # Calculate percentages
    incomplete_percentage = (uncompleted_tasks / total_tasks) * 100 if total_tasks > 0 else 0
    overdue_percentage = (overdue_tasks / total_tasks) * 100 if total_tasks > 0 else 0

    # Generate task overview report
    task_overview_str = f"Total Tasks: {total_tasks}\n"
    task_overview_str += f"Completed Tasks: {completed_tasks}\n"
    task_overview_str += f"Uncompleted Tasks: {uncompleted_tasks}\n"
    task_overview_str += f"Overdue Tasks: {overdue_tasks}\n"
    task_overview_str += f"Incomplete Percentage: {incomplete_percentage:.2f}%\n"
    task_overview_str += f"Overdue Percentage: {overdue_percentage:.2f}%\n"

    with open('task_overview.txt', 'w') as task_overview_file:
        task_overview_file.write(task_overview_str)

    # Generate user overview report
    user_overview_str = f"Total Users: {len(users)}\n"
    user_overview_str += f"Total Tasks: {total_tasks}\n\n"

    for username, user_data in users.items():
        total_user_tasks = user_data['total_tasks']
        completed_user_tasks = user_data['completed_tasks']
        uncompleted_user_tasks = user_data['uncompleted_tasks']
        overdue_user_tasks = user_data['overdue_tasks']

        user_overview_str += f"User: {username}\n"
        user_overview_str += f"Total Tasks Assigned: {total_user_tasks}\n"
        user_overview_str += f"Percentage of Total Tasks: {total_user_tasks / total_tasks * 100:.2f}%\n"
        user_overview_str += f"Percentage of Completed Tasks: {completed_user_tasks / total_user_tasks * 100:.2f}%\n"
        user_overview_str += f"Percentage of Uncompleted Tasks: {uncompleted_user_tasks / total_user_tasks * 100:.2f}%\n"
        user_overview_str += f"Percentage of Overdue Tasks: {overdue_user_tasks / total_user_tasks * 100:.2f}%\n\n"

    with open('user_overview.txt', 'w') as user_overview_file:
        user_overview_file.write(user_overview_str)

    print("Reports generated successfully!")

def display_stats():
    '''If the user is an admin, they can display statistics about the number of users and tasks.'''

    # Check if the tasks.txt and user.txt files exist, and generate them if not
    if not os.path.exists('tasks.txt') or not os.path.exists('user.txt'):
        generate_reports()

    # Read data from tasks.txt and user.txt files
    with open('tasks.txt', 'r') as tasks_file, open('user.txt', 'r') as users_file:
        task_data = tasks_file.readlines()
        user_data = users_file.readlines()

    num_users = len(user_data)
    num_tasks = len(task_data)

    print("-----------------------------------")
    print(f"Number of users: \t\t {num_users}")
    print(f"Number of tasks: \t\t {num_tasks}")
    print("-----------------------------------")

while True:
    # Add optional generate reports feature for admin
    print()
    if curr_user == 'admin':
        admin_option = "gr - Generate reports"
    else:
        admin_option = ""
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    menu = input(f'''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
ds - Display statistics
{admin_option}
e - Exit
: ''').lower()

    # Program selection logic
    if menu == 'r':
        reg_user()
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all()
    elif menu == 'vm':
        view_mine()
    elif menu == 'ds' and curr_user == 'admin': 
        display_stats()
    elif menu == 'gr' and curr_user == 'admin':
        generate_reports()
    elif menu == 'e':
        print('Goodbye!')
        exit()
    else:
        print("You have made a wrong choice, Please Try again")