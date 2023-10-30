from phonebook import app
from flask import render_template, redirect, url_for
from phonebook.forms import PhonebookForm
from phonebook.models import Contact

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/phonebook', methods=['GET', 'POST'])
def phonebook():
    form = PhonebookForm()
    if form.validate_on_submit():
        contact = form.contact.data
        phone_number = form.phone_number.data

        # Contact(contact_name=contact, phone_number=phone_number)
        return redirect(url_for('phonebook'))

    return render_template('phonebook.html', form=form)