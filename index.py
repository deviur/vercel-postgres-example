import os

import sqlalchemy.exc
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

uri = os.getenv('POSTGRES_URL')
print(uri)
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = (uri or 'sqlite:///:memory:')
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)

    def __repr__(self):
        return f'<User {self.username}>'


@app.route('/')
def index():
    username = 'World'
    try:
        user = User.query.first()
        if user:
            username = user.username

    except sqlalchemy.exc.OperationalError as err:
        print(err)

    return f'Hello, {username}!'


if __name__ == '__main__':
    app.run()
