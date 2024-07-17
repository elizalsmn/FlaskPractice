from flask import render_template, url_for,flash, redirect
from flblog import app, db, bcrypt
from flblog.models import User, Post
from flblog.form import RegistrationForm, LoginForm 
from flask_login import login_user, current_user, logout_user, login_required

# with app.app_context():
#     # Create the database tables
#     db.create_all()

posts = [
    {
        'author' : 'Eliza Lesmana',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'April 20, 2018'

    },
    {
        'author' : 'Cia Cia',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'March 11, 2022'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts) 
# posts=posts for html to be able to access posts
@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data , email = form.email.data, password = hashed_pass)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            return redirect(url_for('home'))
        else :
            flash("Login Usuccessful. Please check email & password", 'danger')
    return render_template('login.html', title = 'Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')

