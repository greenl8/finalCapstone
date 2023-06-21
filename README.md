# Task Management System

This task management system is a Python program that allows users to manage tasks. It provides features for user login, task assignment, task viewing, task editing, and generating reports.

## Usage

1. Clone the repository or download the source code.
2. Open the whole folder in your preferred code editor, such as Visual Studio Code.
   - Note: Make sure to open the entire folder to ensure the program can find the required files.
3. Install the necessary dependencies by running the following command: pip install -r requirements.txt
4. Run the program using the following command: python main.py

# Notes

1. Use the following username and password to access admin rights:
- Username: admin
- Password: password
2. Make sure to open the whole folder in your code editor; otherwise, the program will look in your root directory for the text files.

## Features

### Login

The program allows users to log in using their username and password. User credentials are stored in a `user.txt` file. If the file doesn't exist, a default admin account is created.

### Register User

The program provides an option to register a new user. New users can be added by providing a unique username and password.

### Add Task

Users can add tasks by providing the required information, including the assigned person's username, task title, task description, and due date.

### View All Tasks

This feature displays all the tasks in the system. It retrieves task data from the `tasks.txt` file and presents it in a formatted manner.

### View My Tasks

Users can view their assigned tasks only. They can select a task by its number and view its details. They also have options to mark a task as complete, edit the assigned username, or edit the due date.

### Generate Reports

This feature generates two reports: task overview and user overview reports. The task overview report includes information such as total tasks, completed tasks, uncompleted tasks, overdue tasks, and their respective percentages. The user overview report provides details for each user, including their assigned tasks, completion percentages, and overdue task percentages. The reports are saved as `task_overview.txt` and `user_overview.txt` files, respectively.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
