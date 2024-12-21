from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required
from flask_migrate import Migrate
from forms import RegistrationForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
import joblib
from datetime import datetime  # Import to handle date-time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///local_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50))
    due_date = db.Column(db.DateTime)
    priority = db.Column(db.String(20))
    completed = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', tasks=tasks)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('login'))
    
    users = User.query.all()
    print(users)

    return render_template('register.html', title='Register', form=form)

@app.route('/calendar')
@login_required
def calendar():
    return render_template('calendar.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('register'))

@app.route('/add_task', methods=['POST'])
@login_required
def add_task():
    task_title = request.form['title']
    task_category = request.form['category']
    task_due_date = request.form['due_date']
    task_priority = request.form['priority']
    new_task = Task(
        title=task_title, 
        category=task_category, 
        due_date=datetime.strptime(task_due_date, '%Y-%m-%d') if task_due_date else None, 
        priority=task_priority,
        user_id=current_user.id
    )
    db.session.add(new_task)
    db.session.commit()
    flash('Task added successfully!', 'success')
    
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('task_list.html', tasks=tasks)

@app.route('/edit_task/<int:task_id>', methods=['POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.title = request.form['title']
    task.category = request.form['category']
    task.due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d') if request.form['due_date'] else task.due_date
    task.priority = request.form['priority']
    db.session.commit()
    flash('Task updated successfully!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/delete_task/<int:task_id>', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/update_tasks', methods=['POST'])
@login_required
def update_tasks():
    updated_tasks = request.json.get('tasks')
    for updated_task in updated_tasks:
        task = Task.query.get(updated_task['id'])
        if task and task.user_id == current_user.id:
            task.title = updated_task['title']
            task.completed = updated_task['completed']
    db.session.commit()
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)