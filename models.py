from peewee import *

db = SqliteDatabase('sqlite3.db')

class Table(Model):
    class Meta:
        database = db


class User(Table):
    username = CharField()
    full_name = CharField()
    email = CharField()
    hashed_password = CharField()
    disabled = BooleanField()

def create_tables():
    with db:
        db.create_tables([User])

if __name__ == "__main__":
    create_tables()

