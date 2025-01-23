# Tikk: Daily Productivity Tracking Tool

#### Video Demo: [URL HERE]
#### Description:

Project Tikk is a simple productivity tracking application designed to help individuals manage their daily tasks and activities efficiently from a simple dashboard while keeping track of time. Built using Flask and SQLite for local development, it offers a user-friendly interface and tools for improving productivity. The project is version-controlled using GitHub and is currently hosted on CS50 Codespace.

## Features and Functionalities

### 1. User Authentication
- **User Registration and Login**: Users can register and log in securely. User authentication is implemented using Flask and SQLite, with no specific format requirements for usernames or passwords.
- **Session Management**: Users remain logged in across sessions, providing a seamless experience.

### 2. Daily Dashboard
- **Date Display**: The dashboard contains a date box that displays the current date, day, and time to help users stay oriented.
- **To-Do List**: Users can create, edit, and manage their daily tasks. The to-do list is kept at the top of the page and is designed to be simple and intuitive, allowing users to drop tasks in the middle of the day before sorting or scheduling them.
- **Categorized To-Do List**: Users can categorize their daily tasks into different categories by changing the category names directly from the dashboard. They can drag and drop tasks between fields to sort and schedule them.
- **Pomodoro Timer**: A built-in Pomodoro timer helps users manage their time effectively by breaking work into intervals, traditionally 25 minutes in length, separated by short breaks.
- **Hourly Fields**: Users can plan their day hour by hour, with fields available for each hour to input tasks and notes. The current hour is visually highlighted while past hours are greyed out to help keep track of time.

### 3. Drag-and-Drop Functionality
- **SortableJS Integration**: The application uses SortableJS to enable drag-and-drop functionality, allowing users to rearrange tasks easily between different sections of the dashboard. This feature enhances the user experience by providing a more interactive and flexible way to manage tasks.

### 4. Future Implementations (Planned Features)
- **Task Categorization**: Implement machine learning for automatic task categorization, helping users organize tasks more efficiently.
- **Task Storage**: Currently, tasks refresh every time the page loads. A properly structured database system with AJAX will be built to enable saving tasks across sessions.
- **Centralized Calendar**: Develop a centralized calendar system for annual, monthly, and weekly views. Ensure that tasks added to any calendar view are reflected in the daily dashboard and other views.
- **Automatic Task Transfer**: Schedule tasks to move unfinished tasks to the next day automatically.

## Project Structure

The files and folders under the project are listed below:

### Main Files
- **main.py**: The main application file that initializes and runs the Flask application.
- **forms.py**: Contains form classes for user registration and login, utilizing Flask-WTF for form handling.
- **init_db.py**: A script to initialize the SQLite database, ensuring the necessary tables and data structures are in place.
- **requirements.txt**: Contains a list of requirements to run the project.

### Templates
- **templates/index.html**: The landing page, lists all the pages within the directory.
- **templates/login.html**: The login page where users can enter their credentials to access the dashboard.
- **templates/dashboard.html**: The main dashboard page displaying the daily dashboard with the date, to-do list, Pomodoro timer, and hourly fields.
- **templates/register.html**: The registration page where new users can create an account.

### Static Files
- **static/styles.css**: The CSS file for styling the application, ensuring a consistent and visually appealing interface.
- **static/images/logo.png**: The image file for the logo of the app.

## Design Choices

### Technology Stack
- **Flask**: Chosen for its simplicity and flexibility, making it easy to develop the application.
- **SQLite**: Used for local development due to its lightweight nature and ease of setup.
- **JavaScript, HTML, CSS**: Frontend technologies used to create a responsive and interactive user interface.
- **SortableJS**: Integrated for its robust drag-and-drop functionality, enhancing user interaction.

## Conclusion

This app aims to provide a comprehensive productivity tracking solution tailored to manage daily tasks while keeping track of time. With a focus on user-friendly design and essential productivity tools, Tikk is an ongoing project with a clear roadmap for future development and enhancements. The project leverages modern web technologies and robust design principles to deliver a valuable tool for managing daily tasks and improving productivity.
