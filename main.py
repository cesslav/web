import random

from data import db_session
from flask import Flask
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
alphabet = " qwertyuiopasdfghjklzxcvbnm"


def main():
    db_session.global_init("db/blogs.db")
    # app.run()


if __name__ == '__main__':
    main()

    user = User()
    user.name = "Scott"
    user.about = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    for i in alphabet:
        user = User()
        user.name = "Scott" + i
        user.about = "Ridley" + i
        user.age = 21 + random.randint(1, 120)
        user.position = "captain" + i
        user.speciality = "research engineer" + i
        user.address = "module_1" + i
        user.email = "scott_chief@mars.org" + i
        db_sess = db_session.create_session()
        db_sess.add(user)
        db_sess.commit()
