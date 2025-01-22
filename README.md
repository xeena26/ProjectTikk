# ProjectTikk
#### Video Demo:  <URL HERE>
#### Description:
**ProjectTikk** is a web-based task management application designed to help users organize and track their daily activities efficiently. The project leverages Python's Flask framework for the backend and utilizes HTML, CSS, and JavaScript for the frontend. ProjectTikk incorporates features like user authentication, task management, a pomodoro timer, and a dynamic to-do list, providing users with a comprehensive tool to manage their tasks.

### Features:
1. **User Authentication**: Secure login and registration system.
2. **Task Management**: Create, edit, and delete tasks with options for due dates, categories, and priorities.
3. **Pomodoro Timer**: Integrated timer to boost productivity using the Pomodoro Technique.
4. **Dynamic To-Do List**: Add, edit, and organize tasks on the go.
5. **Real-Time Updates**: Tasks are highlighted based on the current hour and completion status.

### File Descriptions:
1. **dashboard.html**:
   - Contains the main structure of the dashboard, including the navigation bar, main content sections (date box, to-do list, pomodoro timer, hourly to-do list, and other tasks section).
   - Uses Flask templates to dynamically render tasks and handle form submissions for tasks.

2. **styles.css**:
   - Defines the overall style and appearance of the application, including colors, fonts, and layout.
   - Ensures a consistent and visually appealing design across the application.

3. **main.py**:
   - The backend logic of the application.
   - Manages routes for user authentication, task management, and real-time updates.
   - Connects to a SQLite database to store user and task data.

4. **login.html** and **register.html**:
   - Template files for user authentication (login and registration).
   - Ensures users can securely create accounts and access their personal dashboard.

### Design Choices:
- **Flask Framework**: Chosen for its simplicity and flexibility in developing web applications.
- **SQLite Database**: Lightweight and easy to integrate with Flask for handling user and task data.
- **Responsive Design**: Ensures that the application is accessible and user-friendly on various devices.
- **Pomodoro Technique**: Integrated to help users manage their time more effectively and boost productivity.

### How to Use:
1. **Clone the repository**: `git clone <repository-url>`
2. **Navigate to the project directory**: `cd project-tikk`
3. **Set up a virtual environment**: `python3 -m venv env`
4. **Activate the virtual environment**: `source env/bin/activate` (Linux/Mac) or `.\env\Scripts\activate` (Windows)
5. **Install the dependencies**: `pip install -r requirements.txt`
6. **Run the application**: `flask run`
7. **Access the application**: Open your web browser and navigate to `https://supreme-broccoli-4gx49vr946xhq7gv-5000.app.github.dev/dashboard`

### Future Improvements:
- **Collaboration Features**: Allow multiple users to collaborate on tasks.
- **Enhanced Notifications**: Integrate email or push notifications for task reminders.
- **Mobile App**: Develop a mobile version of the application
