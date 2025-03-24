from peewee import *

db = SqliteDatabase('sqlite3.db')

class Table(Model):
    class Meta:
        database = db


class User(Table):
    username = CharField()
    full_name = CharField()
    telegramm = CharField()
    hashed_password = CharField()
    disabled = BooleanField()

class Role(Table):
    name = CharField()

class UserRole(Table):
    user = ForeignKeyField(User)
    role = ForeignKeyField(Role)

def create_tables():
    with db:
        db.create_tables([User, Role, UserRole])

if __name__ == "__main__":
    create_tables()

