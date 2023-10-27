from phonebook import app
from flask import render_template, redirect, url_for
from phonebook.forms import PhonebookForm

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/phonebook')
def phonebook():
    form = PhonebookForm()
    return render_template('phonebook.html', form=form)