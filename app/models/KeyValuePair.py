from peewee import Model, IntegerField, TextField, SqliteDatabase, Check
from app.configuration import *
db = SqliteDatabase(DB_NAME)

class KeyValuePair(Model):
    class Meta:
        database=db

    id = IntegerField(primary_key=True)
    key = TextField(unique=True, null=False)
    value = TextField(null=False)

    def __repr__(self):
        return f"<KeyValuePair(key='{self.key}', value='{self.value}')>"