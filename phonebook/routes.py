from phonebook import app
from flask import render_template, redirect, url_for
from phonebook.forms import PhonebookForm, RegisterForm, LoginForm
from phonebook.models import Contact, User
from flask_login import login_user, logout_user


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        user_exists = User.query.filter((User.username == username)|(User.email == email)).all()

        if user_exists:
            print("This user already exists.")
            return redirect(url_for('register'))

        User(username=username, email=email, password=password)

        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=["GET", "POST"])   
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if not user or not user.check_password(password):
            print('Incorrect username or password.')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



@app.route('/phonebook', methods=['GET', 'POST'])
def phonebook():
    form = PhonebookForm()
    if form.validate_on_submit():
        contact = form.contact.data
        phone_number = form.phone_number.data

        # Contact(contact_name=contact, phone_number=phone_number)
        return redirect(url_for('phonebook'))

    return render_template('phonebook.html', form=form)