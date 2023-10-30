from phonebook import app
from flask import render_template, redirect, url_for
from phonebook.forms import PhonebookForm, RegisterForm, LoginForm
from phonebook.models import Contact, User

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
    return redirect(url_for('register', form=form))
        



@app.route('/phonebook', methods=['GET', 'POST'])
def phonebook():
    form = PhonebookForm()
    if form.validate_on_submit():
        contact = form.contact.data
        phone_number = form.phone_number.data

        # Contact(contact_name=contact, phone_number=phone_number)
        return redirect(url_for('phonebook'))

    return render_template('phonebook.html', form=form)