from phonebook import app

@app.route('/')
def index():
    return 'This is our index.'

@app.route('/phonebook')
def phonebook():
    return 'This is our phonebook.'