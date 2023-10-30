from phonebook import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = generate_password_hash(kwargs['password'])
        db.session.add(self)
        db.session.commit()
    
    def __repr__(self):
        return f'User|{self.username}'
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contact_name = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(10), unique=True, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()

    def __repr__(self) -> str:
        return f"<Contact|{self.contact_name} = {self.phone_number}>"
    