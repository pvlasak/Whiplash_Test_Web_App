from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///whiplash_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "my_secret"

db = SQLAlchemy(app)


def create_db():
    with app.app_context():
        db.create_all()
    print('Created Database!')


def delete_result():
    with app.app_context():
        db.session.delete(Result.query.get(1))
        db.session.commit()
    print('Result deleted from Database!')


def load_pulses():
    with app.app_context():
        p1 = Pulse(id=1, severity='Low', comment='low severity pulse, trapezoid, 16 kmh delta-v')
        p2 = Pulse(id=2, severity='Medium', comment='medium severity pulse, triangular, 16 kmh delta-v')
        p3 = Pulse(id=3, severity='High', comment='high severity pulse, trapezoid, 24 kmh delta-v')

        db.session.add(p1)
        db.session.add(p2)
        db.session.add(p3)
        db.session.commit()
    print('Pulse types recorded!')


def check_all_users_db():
    with app.app_context():
        users = User.query.all()
    print(users)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from routes import *

if __name__ == '__main__':
    app.run()
