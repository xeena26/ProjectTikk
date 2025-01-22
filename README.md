# Tikk: Daily Productivity Tracking Tool

#### Video Demo: [URL HERE]
#### Description:

Project Tikk is a simple productivity tracking application designed to help individuals, manage their daily tasks and activities efficiently from a simple dashboard. Built using Flask and SQLite for local development, it offers a user-friendly interface and tools for improving productivity. The project is version-controlled using GitHub and is currently hosted on CS50 Codespace.

## Features and Functionalities

### 1. User Authentication
- **User Registration and Login**: Users can register and log in securely. User authentication is implemented using Flask and SQLite, no format requirement username or password was implemented.
- **Session Management**: Users remain logged in across sessions.

### 2. Daily Dashboard
- **Date Display**: The dashboard contains a datebox that displays the current date and time prominently to help users stay oriented.
- **To-Do List**: Users can create, edit, and manage their daily tasks. The to-do list is designed to be simple and intuitive.
- **Pomodoro Timer**: A built-in Pomodoro timer helps users manage their time effectively by breaking work into intervals, traditionally 25 minutes in length, separated by short breaks.
- **Hourly Fields**: Users can plan their day hour by hour, with fields available for each hour to input tasks and notes.

### 3. Drag-and-Drop Functionality
- **SortableJS Integration**: The application uses SortableJS to enable drag-and-drop functionality, allowing users to rearrange tasks easily. This feature enhances user experience by providing a more interactive and flexible way to manage tasks.

### 4. Future Implementations (Planned Features)
- **Task Categorization**: Implement machine learning for automatic task categorization, helping users organize tasks more efficiently.
- **Centralized Calendar**: Develop a centralized calendar system for annual, monthly, and weekly views. Ensure that tasks added to any calendar view are reflected in the daily dashboard and other views.
- **Progress Bars**: Implement progress bars for categorized tasks to give users a visual representation of their progress.
- **Automatic Task Transfer**: Schedule tasks to move unfinished tasks to the next day automatically.
- **Goals and Checklists**: Add goals and checklists for annual, monthly, and weekly views to help users set and track their goals.

## Project Structure

The project is organized into several files and folders, each serving a specific purpose:

### Main Files
- **main.py**: The main application file that initializes and runs the Flask application.
- **forms.py**: Contains form classes for user registration and login, utilizing Flask-WTF for form handling.
- **init_db.py**: A script to initialize the SQLite database, ensuring the necessary tables and data structures are in place.
- **tasks.csv**: A dataset for task categorization (planned feature).

### Templates
- **templates/index.html**: The home page with navigation links to Login and Dashboard pages.
- **templates/login.html**: The login page where users can enter their credentials to access the dashboard.
- **templates/dashboard.html**: The main dashboard page displaying the daily dashboard with date, to-do list, Pomodoro timer, and hourly fields.
- **templates/register.html**: The registration page where new users can create an account.

### Static Files
- **static/styles.css**: The CSS file for styling the application, ensuring a consistent and visually appealing interface.

## Design Choices

### Technology Stack
- **Flask**: Chosen for its simplicity and flexibility, making it easy to develop and scale the application.
- **SQLite**: Used for local development due to its lightweight nature and ease of setup.
- **JavaScript, HTML, CSS**: Frontend technologies used to create a responsive and interactive user interface.
- **SortableJS**: Integrated for its robust drag-and-drop functionality, enhancing user interaction.

### User Experience
- **Intuitive Interface**: The application is designed to be user-friendly, with a clean and straightforward interface.
- **Accessibility**: Considerations were made to ensure that the application is accessible to users with ADHD, including features like the Pomodoro timer to help with time management.

## Progress and Remaining Work

### Completed
- Project setup and basic structure.
- User authentication (registration and login).
- Basic HTML/CSS for index, login, and dashboard pages.
- Database initialization and setup.
- GitHub repository setup and initial commit.
- Deployment to CS50 Codespace.

### Remaining
- Develop the daily dashboard with all planned functionalities.
- Integrate SortableJS for drag-and-drop functionality.
- Implement machine learning for task categorization.
- Develop the centralized calendar system.
- Implement additional features like progress bars, automatic task transfer, and goals/checklists.
- Thoroughly test all features and fix any bugs.
- Final deployment to CS50 Codespace.

## Conclusion

Project Tikk aims to provide a comprehensive productivity tracking solution tailored to the needs of individuals with ADHD. With a focus on user-friendly design and essential productivity tools, Project Tikk is an ongoing project with a clear roadmap for future development and enhancements. The project leverages modern web technologies and robust design principles to deliver a valuable tool for managing daily tasks and improving productivity.
